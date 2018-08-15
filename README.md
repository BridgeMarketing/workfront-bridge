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

### Using Blocks inside a Project Block


## Using Project Builders
