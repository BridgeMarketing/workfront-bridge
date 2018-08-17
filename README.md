# workfront-bridge

Workfront Bridge is a library that make the creation of bridge projects in
workfront easily.

## Design

Projects and tasks in workfront have custom forms. Those custom forms have
several parameters which are fullfill when the project is created(some other
parameters are being fullfilled while the project is developed and task are
being excetuted).

The library tries to divide and group logical blocks of tasks that can be
convined to build a workfront project.
So, in order to achieve this, two main abstractions are provided:

* Project Containers
* Blocks

### Workfront Blocks

A Block is a group of one or more task that live inside a workfront template
project.
Each particular block must knows its tasks, the parameters of them and the
dependencies among them so it can instantiate and configure them without
difficulties.
The fact that the tasks live inside a workfront template project is just a
convinient way of storing them(workfront does not allow to define a group of
template task out of a template project).

### Workfront Project Containers

Project Containers represents empty workfront project templates associated with
one or more custom forms that can allocate different blocks.
The idea of these project containers is to build different project types by
adding different type of blocks to it.
So, basically a workfront project will be constructed by creating a project
container, setting the corresponding parameters to it and appending blocks to
the project container according to the behaviour that is needed for that
project. In this process, the parameters for the different blocks will be also
set.

## Creating Blocks

Inherit from **WFBlock** class to create a new specific block. A Workfront
service and a template id needs to be provided to the WFBlock constructor. The
template id must have only the tasks that belongs to this block.
Also fields can be marked as optional and required to be automatically validated
when a new project is being constructed with this block.

For example, supose you want to add a block with 1 task:
* My task : which has 2 parameters; name (required) and age (optional)

Here it is an example of how you would make the block representing that task:

```python
class MyWFBlock(WFBlock):
    def __init__(self, wf):
        template_id = template_id_from_name(wf, "My block template")
        super(WFEmailTestSeedBlock, self).__init__(wf, template_id)
        self._set_required_fields(["name"])
        self._set_optional_fields(["age"])
```

In order to set the concrete values for those parameters the
**set_task_param_value** method must be used.
The **set_task_param_value** receives a **task identifier** (that can be an
integer, indicating the number of the task in the template project, or a string
for the name of the task).
Properties can be utilize for a clean design:

```python
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self.name = value
    self.set_task_param_value("My task", "name", value)
```

The purpose of using the **set_task_param_value** is that when the block is used
inside a project container and a workfront project is build, the block knows
how to configure the value in the group of task represented by this block.

### Starter task

Each block has as default starter task the first task. However this can be
changed by using the **_set_starter_task(task_identifier)** method when
inheriting from WFBlock.
This can be handy when having indentation task that only organize task. So, for
example if you have the following tasks in the block:

* Grouping Task
  * Task 1
  * Task 2

You should set the Task 1 as a starter task skipping the Grouping Task that only
gives some visual clarity indenting Task 1 and 2.
Why ? This is required when for example Task 1 is Automatic. The workfront proxy
only starts Automatic tasks when they are a direct predecessor of a completed
task.
So, in this case, when the predecessor of Grouping task is complete (and
starter task is the Grouping Task), Task 1 will not start (because Grouping Task
predecessor is an indirect predecessor of Task 1). So to avoid that, Task 1
must be set as starter task.
This can be achieved in the constructor of the block like this :

```python
    def __init(...)
        # Other blcok stuff...
        self._set_starter_task(2) # Task 1 is the second task
        # or you can set it by name
        self._set_starter_task("Task 1")
```

## Creating Project Containers

To create a project container the new block should inherit from
**WFProjectContainer**.
After that, the template id of the workfront template project and the required
and optional parameters should be provided. This can be done calling the parent
constructor and the methods **_set_required_fields** and
**_set_optional_fields** (you can make use of the **template_id_from_name**
function to get the template id):

```python
class MyWFProjectContainer(WFProjectContainer)
    def __init__(self, wf, prj_name):
        tid = template_id_from_name(wf, "My WF Template")
        super(MyWFProjectContainer, self).__init__(wf, tid, prj_name)
        self._set_required_fields(["workfront_param_value_req"])
        self._set_optional_fields(["workfront_param_value_optional"])
```

Then you can set the variables that will fullfill the parameter values of the
project calling the **set_param_value** method. For example:

```python
@property
def my_param_value(self):
    return self._my_param_value

@email_subject.setter
def my_param_value(self, v):
    self._my_param_value = v
    self.set_param_value("workfront_param_value_req", v)
```

You can check the **WFProjectEmailContainer** in workfront_bridge.projects.email
for a complete example.

### Using Blocks inside a Project Container

Blocks are made to be appended to a project container. A project container can
have one or more blocks of the same type.
When adding a block to a project container, the block is appended to the project
making this new block, dependent of the last added block. So for example, if
block1, block2, block3 are appended to the same project block in that order,
the workfront project will be created so that the starter task in block2 will
only be excetuted when the last task in block1 is completed. The same happens to
block3; the starter task created that belongs to block3 will only start after
the last task from block2 finishes.

The project container does not have any restriction in the order that the blocks
are added to the project block, it is the user responsability to add the blocks
in an order that has some logic.

We recommend using project builders in order to make life easier for those who
want to create workfront projects using this library. This allows user to
re-use the code logic used to create particular workfront projects.

## Using Project Builders

To easily create projects you can use project builders. Project builders provide
a simple interface with setters to create different projects structures.

So for example, to create a simple email project with 2 test list and 1 seed
list you will do something similar to this:

```python
from workfront.workfront import Workfront
from workfront_bridge.projects.email_builder import EmailProjectBuilder

# Create a Workfront Service object (using the workfront-sdk)
wf = Workfront("email@wf.bridgemarketing.com", "pass***")
wf.login()

# A project builder needs a Workfront service and a name to be constructed
builder = EmailProjectBuilder(wf, "Project Test Name")

# Then, the subject and a html is needed to be validated:
builder.set_html("s3://some/s3/path/creative.html")
       .set_subject("This is the subject!")
# In the case of email builder you can use a zip to construct the html. In that
# case you will use this:
# b.set_html_zip("s3://some/s3/path/creative.zip")

# Then, add two test list and a live seed list
builder.add_test_list("s3://some/s3/test_list1.csv")
       .add_test_list("s3://some/s3/test_list2.csv")
       .set_seed_list("s3://some/s3/live_seed_list.csv)

# Finally, build and obtain the Workfront project
wf_project = b.build()
# When calling build a WFBrigeException can arise telling you if some
# parameters are missing, or something is wrong.
```
