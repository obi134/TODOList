# ToDoList
Todo list server, written in python by using django, for running e.g. on raspberry pi.
The ToDo List provides an overview over your ToDos sorted by e.g. priority.

Supported fields:
- Taskname
- Listname
- Priority
- Time estimation
- Remaining Time 	

## Settings
Generate a secret key by running in terminal:

```python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'```

In python_ToDoList/settings.py:
  - ALLOWED_HOSTS = ["<server-ip_or_dns-name>"]
  - SECRET_KEY = '<generated_key>'
  
## First Start
To create the database and a superuser call the following commands:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Then follow the instructions to create the superuser and start the server by running
```
python manage.py runserver 0.0.0.0:8001
```
Now the server should be started and you can call in browser `127.0.0.1:8001/admin/` and authenticate with your previously created credentials. You can now create the first list by clicking on the add-symbol next to "Lists", enter the list name and click on save. Now you have the first list, which can be filled. Call in browser `127.0.0.1:8001/reportone/` and find the empty todo list. It's now ready to create yout first entry.
  
## Autostart
To run on a server automatically, enter the following code in user's crontab (run in terminal: `crontab -e`)

```@reboot python2.7 /absolute_path_to_script/manage.py runserver 0.0.0.0:8001```

## Usage

### Open ToDo List with browser
To open your ToDo List open in browser `<ip_or_servername>:8001/reportone/`

### Open ToDo List with browser, sorted by room
To open your ToDo List, sorted by room, open in browser `<ip_or_servername>:8001/report/`

### Open admin site with browser
To open the admin site open in browser `<ip_or_servername>:8001/admin/`
