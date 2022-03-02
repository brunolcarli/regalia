install:
	pip install -r regalia/requirements/common.txt

run:
	python manage.py runserver 0.0.0.0:7890 --settings=regalia.settings.${ENV_REF}

wsgi:
	gunicorn -w 3 regalia.wsgi:application -b :7890

migrate:
	python manage.py makemigrations --settings=regalia.settings.${ENV_REF}
	python manage.py migrate --settings=regalia.settings.${ENV_REF}

start_scrapping:
	python manage.py scrap --settings=regalia.settings.${ENV_REF}

target: start_scrapping wsgi

pipe:
	make install
	make migrate
	make -j2 target
