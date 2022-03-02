install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:7890 --settings=regalia.settings.development

migrate:
	python manage.py makemigrations --settings=regalia.settings.development
	python manage.py migrate --settings=regalia.settings.development

start_scraping:
	python manage.py scrap --settings=regalia.settings.development

pipe:
	make install
	make migrate
	make start_scrapping
	make run
