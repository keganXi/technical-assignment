# Test entire application.
run-test:
	python3 manage.py test


# Start django server.
run:
	python3 manage.py runserver 0.0.0.0:8000


# Copy all dependencies into requirements.txt file.
copy-deps:
	pip freeze > requirements.txt


# Install packages listed in requirements.txt file.
install-reqs:
	pip install -r requirements.txt


# django shell.
shell:
	docker-compose run web python3 manage.py shell


# create superuser.
create-super-user:
	python3 manage.py createsuperuser


# runserver
run:
	python3 manage.py runserver
