# django-learn

Create Workspace Folder and go to it

# md Workspace
# cd Workspace

Create VirtualEnvironment

# Virtualenv venv

Activate Virtual Environment

# venv\Scripts\Activate

Copy Downloaded Project folder in to workspace and rename it to django-learn and go to it

# cd django-learn

Create DB named in settings file from Mysql named : djangolearndb

Now first migrate your migrations

# python manage.py migrate

Now apply fixtures(Preconfigured data) from Deply folder two files

# python manage.py loaddata deploy\Appsettings.json
# python manage.py loaddata deploy\Student.json

Now create SuperUser

# python manage.py createsuperuser

Finally Run the project

# python manage.py runserver


