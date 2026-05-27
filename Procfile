release: python manage.py migrate
web: gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT
