install:
	pip3 install -r regalia/requirements/${ENV_REF}.txt

run:
	python manage.py runserver 0.0.0.0:7890 --settings=regalia.settings.${ENV_REF}

wsgi:
	gunicorn -w 3 regalia.wsgi:application -b :8000

migrate:
	python manage.py makemigrations --settings=regalia.settings.${ENV_REF}
	python manage.py migrate --settings=regalia.settings.${ENV_REF}

start_scrapping:
	python manage.py scrap --settings=regalia.settings.${ENV_REF}

start_gas_scrapping:
	python manage.py gas_scrap --settings=regalia.settings.${ENV_REF}

start_house_scrapping:
	python manage.py house_scrap --settings=regalia.settings.${ENV_REF}

target: start_scrapping run

pipe:
	pip install -r requirements.txt
	#make install
	make migrate
	make -j2 target

shell:
	python manage.py shell --settings=regalia.settings.${ENV_REF}