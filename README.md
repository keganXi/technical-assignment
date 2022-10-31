# Technical-Assignment
Technical home assignment for kartoza.

# Setup Guide
A Quick guide on how to setup the project.

## Clone Project
```$ git clone https://github.com/keganXi/technical-assignment```

## PostgreSQL Database
> NOTE: if you don't have PostgreSQL installed here is where you can get it https://www.postgresql.org/download/<br>

Create a database named technical_assignment.<br>
```$ createdb technical_assignment```

## Set Environment Variables
Create a ```.env``` file in the root of the project and copy the contents from ```.env.example``` and paste it in ```.env``` and insert all secret keys, api keys, etc.

## Virtual Environment
- In the root of the project create a virtual environment ```$ python -m venv venv```.
- Activate virtual environment ```$ source venv/bin/activate``` or if you running Windows ```>> cd venv/scripts/``` ```>> activate```.
- Install dependencies from requirements.txt file ```$ pip install -r requirements.txt```.

## Install tailwind-django
>NOTE: for more information on django-tailwind installation follow the link https://django-tailwind.readthedocs.io/en/latest/installation.html
- Install django-tailwind node modules ```$ python manage.py tailwind install```

## Run Migrations
- Run migrations ```$ python manage.py makemigrations```.
- Run migrate ```$ python manage.py migrate```.

## Running Django Server
Now you can finally run the project ```$ python manage.py runserver```.

## Running Tests.
```$ python manage.py users.tests```




