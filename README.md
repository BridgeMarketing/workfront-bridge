# workfront-bridge

Workfront Bridge is a library that let you create bridge projects in workfront
easily.

## Design

Projects and tasks in workfront have custom forms. Those custom forms have
several parameters which are fullfill when the project is created(some other
parameters are being fullfilled while the project is developed and task are
being excetuted).

The library tries to divide and group logical blocks of tasks that can be
convined to form a workfront project.
So, in order to achieve this, two main abstractions are provided:

* Project Blocks
* Blocks

### Blocks

A Block is a group of one or more task that live inside a workfront template
project.
Each particular block must knows its tasks, the parameters of them and the
dependencies among them so it can instantiate them without difficulties.
The fact that the tasks live inside a workfront template project is just a
convinient way of storing them(workfront does not allow to define a group of
template task out of a template project).

### Project Blocks

Project Blocks are associated to workfront project templates wich have custom
forms associated to them. These project blocks are typically empty (no tasks) so
that we can add blocks to them.
So, basically the idea is to create a project block, set the project block
parameters and append the blocks according to the specific requirements of each
project.

## Creating Blocks

## Creating Project Blocks

To create a project block the new block should inherit from **WFProjectBlock**.
After that, the template id of the workfront template project and the required
and optional parameters should be provided. This can be done calling the parent
constructor and the methods **_set_required_fields** and
**_set_optional_fields** (you can make use of the **template_id_from_name**
function to get the template id):

```python
def __init__(self, wf, prj_name):
    tid = template_id_from_name(wf, "My WF Template")
    super(MyWFProjectBlock, self).__init__(wf, tid, prj_name)
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

You can check the **WFProjectEmailBlock** in workfront_bridge.projects.email
for a complate example.

### Using Blocks inside a Project Block

Blocks are made to be appended to a project block. A project block can contain
one or more blocks of the same type.
When adding a block to a project block, the block is appended to the project
making this new block, dependent of the last added block. So for example, if
block1, block2, block3 are appended to the same project block in that order,
the workfront project will be created so that the first task in block2 will
only be excetuted when the last task in block1 is completed. The same happens to
block3; the first task created that belongs to block3 will only start after the
last task from block2 finishes.

The project block does not have any restriction in the order that the blocks
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
