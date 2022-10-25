# Test entire application.
run-test:
	docker-compose run web python3 manage.py test


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


# apply all migrations and migrate
migrate:
	docker-compose run web python3 manage.py makemigrations
	docker-compose run web python3 manage.py migrate


# make migrations
docker-make-migrations:
	docker-compose run web python3 manage.py makemigrations


# apply changes to database (migrate).
docker-migrate:
	docker-compose run web python3 manage.py migrate


# create superuser.
create-super-user:
	docker-compose run web python3 manage.py createsuperuser


# start server from docker.
docker-run:
	docker-compose --env-file .env up
