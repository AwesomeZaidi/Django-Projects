
# Django Notes

`django-admin startproject mysite`

Auto-generates some code that establishes a Django project – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

Then go into project

`venv virtualenv`

Creates folder in directory for virtual environment.

Activate virtualenv when i wanna start developing.

If its a new proj, pip install django

Then, runserve command here,

If you're making changes to any models or views then you have to migrate command. 

The outer mysite/ root directory is just a container for your project.

manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package.

mysite/settings.py: Settings/configuration for this Django project

mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.

mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

`migrate` command

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies.

Each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.

let’s hop into the interactive Python shell and play around with the free API Django gives you. To invoke the Python shell, use this command:


`python manage.py shell`
We’re using this instead of simply typing “python”, because manage.py sets the DJANGO_SETTINGS_MODULE environment variable, which gives Django the Python import path to your mysite/settings.py file.

