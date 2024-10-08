#!/bin/sh

#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $POSTGRES_HOST 5432; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

exec "$@"
