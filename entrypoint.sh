#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear


echo "Checking if superuser exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@admin.com').exists():
    User.objects.create_superuser(email='admin@admin.com', password='admin123', fullname='Admin')
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

if [ "$DJANGO_ENV" = "development" ]; then
    exec python manage.py runserver 0.0.0.0:8000
else
    exec gunicorn gg_car.wsgi:application --bind 0.0.0.0:8000
fi
