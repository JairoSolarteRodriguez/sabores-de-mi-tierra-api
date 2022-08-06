release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn sabores_de_mi_tierra.wsgi

