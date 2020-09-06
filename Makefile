start:
	@docker-compose up --build --remove-orphans

stop:
	@docker-compose stop && docker-compose rm -f

test:
	@docker-compose run app sh -c "python manage.py test"

lint:
	@docker-compose run app sh -c "flake8"

super:
	@docker-compose run app sh -c "python manage.py createsuperuser"