release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

release: python manage.py makemigrations users_app --no-input
release: python manage.py migrate users_app --no-input

web: gunicorn sabores_de_mi_tierra.wsgi

