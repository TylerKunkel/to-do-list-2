# to-do-list

The goal of this project is to create a command-line to-do list application that allows users to add, view, and complete tasks. The project will be written in Python, and it will utilize file input/output to store and retrieve task data.

Here's a high-level overview of the steps we'll need to take to create the to-do list:

Create a task class: We'll create a Task class that will store information about each task, such as the task name, description, and due date.

Create a to-do list class: We'll create a ToDoList class that will contain a list of Task objects. This class will allow us to add, view, and complete tasks.

Implement user input: We'll prompt the user to input their desired action, such as adding a task, viewing the to-do list, or completing a task.

Add tasks: When the user selects the "add task" option, we'll prompt them to input the task name, description, and due date. We'll then create a Task object with this information and add it to the to-do list.

View tasks: When the user selects the "view tasks" option, we'll display all of the tasks in the to-do list.

Complete tasks: When the user selects the "complete task" option, we'll prompt them to select which task they want to mark as complete. We'll then update the task object's status to "completed."

Save tasks to a file: We'll use file input/output to save the current state of the to-do list to a file, so that the user can exit the program and come back later to continue working on their tasks.

Load tasks from a file: When the user starts the program, we'll load the task data from the file and populate the to-do list with any tasks that were previously added.
