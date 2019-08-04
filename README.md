# ToDoList
Todo list server in python for running e.g. on raspberry pi.

## Settings
Generate a secret key by running in terminal:

```python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])'```

In python_ToDoList/settings.py:
  ALLOWED_HOSTS = ["<server-ip_or_dns-name>"]
  SECRET_KEY = '<generated_key>'

## Usage

### Autostart
To run on a server automatically, enter the following code in user's crontab (run in terminal: `crontab -e`)

```@reboot python2.7 /opt/scripts/python_ToDoList/manage.py runserver 0.0.0.0:8001```

### Open ToDo List with browser
To open your ToDo List open in browser `<ip_or_servername>:8001/reportone/`

### Open ToDo List with browser, sorted by room
To open your ToDo List, sorted by room, open in browser `<ip_or_servername>:8001/report/`

### Open admin site with browser
To open the admin site open in browser `<ip_or_servername>:8001/admin/`
