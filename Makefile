install:
	pip install -r regalia/requirements/common.txt

run:
	python manage.py runserver 0.0.0.0:7890 --settings=regalia.settings.development

migrate:
	python manage.py makemigrations --settings=regalia.settings.development
	python manage.py migrate --settings=regalia.settings.development

start_scrapping:
	python manage.py scrap --settings=regalia.settings.development

pipe:
	make install
	make migrate
	make start_scrapping
	make run
