install:
	pip install -r regalia/requirements/${ENV_REF}.txt

run:
	python manage.py runserver 0.0.0.0:7890 --settings=regalia.settings.${ENV_REF}

wsgi:
	gunicorn -w 3 regalia.wsgi:application -b :8000

migrate:
	python manage.py makemigrations --settings=regalia.settings.${ENV_REF}
	python manage.py migrate --settings=regalia.settings.${ENV_REF}

start_scrapping:
	python manage.py scrap --settings=regalia.settings.${ENV_REF}

target: start_scrapping run

pipe:
	make install
	make migrate
	make -j2 target
