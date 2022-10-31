# Technical-Assignment
Technical home assignment for kartoza.

# Setup Guide
A Quick guide on how to setup the project.

## Clone Project
```$ git clone https://github.com/keganXi/technical-assignment.git```

## PostgreSQL Database
> NOTE: if you don't have PostgreSQL installed here is where you can get it https://www.postgresql.org/download/<br>

Create a database named technical_assignment.<br>
```$ createdb technical_assignment```

## Set Environment Variables
Create a ```.env``` file in the root of the project and copy the contents from ```.env.example``` and paste it in ```.env``` and insert all secret keys, api keys, etc.

## Virtual Environment
> NOTE: if any errors occure with the database try changing ```DATABASE_HOST="db"``` to ```DATABASE_HOST="localhost"```.
- In the root of the project create a virtual environment ```$ python -m venv venv```.
- Activate virtual environment ```$ source venv/bin/activate``` or if you running Windows ```>> cd venv/scripts/``` ```>> activate```.
- Install dependencies from requirements.txt file ```$ pip install -r requirements.txt```.

## Install tailwind-django
>NOTE: for more information on django-tailwind installation follow the link https://django-tailwind.readthedocs.io/en/latest/installation.html
- Install django-tailwind node modules ```$ python manage.py tailwind install```

There is a common error installing django-tailwind on windows because the npm executable cannot be found so I listed the solution below.<br>
- Add this to the base.py file in settings folder ```NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"```.
- To find NPM path type this in the terminal ```$ which npm```.

## Run Migrations
- Run migrations ```$ python manage.py makemigrations```.
- Run migrate ```$ python manage.py migrate```.

## Running Django Server
Now you can finally run the project ```$ python manage.py runserver```.

## Running Tests.
```$ python manage.py users.tests```




