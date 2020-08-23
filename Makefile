test:
	@docker-compose run app sh -c "python manage.py test"

lint:
	@docker-compose run app sh -c "flake8"