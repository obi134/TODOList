# ToDoList
Todo list server in python for running e.g. on raspberry pi.

## Usage
To run on a server automatically, enter the following code in user's crontab (run in terminal: `crontab -e`)

```@reboot python2.7 /opt/scripts/python_ToDoList/manage.py runserver 0.0.0.0:8001```
