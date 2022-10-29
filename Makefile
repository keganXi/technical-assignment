# Test entire application.
run-test:
	python3 manage.py test


# Copy all dependencies into requirements.txt file.
copy-deps:
	pip freeze > requirements.txt


# Install packages listed in requirements.txt file.
install-reqs:
	pip install -r requirements.txt


# django shell.
shell:
	python3 manage.py shell


# create superuser.
create-super-user:
	python3 manage.py createsuperuser


# runserver
run:
	python3 manage.py runserver


# run tailwind dev server.
run-tailwind:
	python3 manage.py tailwind start


# run makemigrations.
run-makemigrations:
	python3 manage.py makemigrations


# apply changes.
run-migrate:
	python manage.py migrate
