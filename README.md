# sofokustest

Assignment:

Write a simple CRUD application that provides a REST API for a "TODO" application.

Requirements:

 * The "TODO" list consists of text items that have a "done/not done" tick. [v]
 * The user must be able to add new lines to the end of the list [v]
 * The user must be able to edit the text content of individual lines [v]
 * The user must be able to reorder the lines [v]
 * The "done/not done" state of a line must be changeable [v]
 * The user must be able to delete individual lines [v]

The API should return the list in JSON format. It's okay to implement the API endpoints as normal Django views. SQLite is enough for the database.

Extra points will be awarded for:

 * Use of Django Rest Framework [v]
 * Setting up the Django admin interface
 * User authentication [v]
 * A working Dockerfile [v]
