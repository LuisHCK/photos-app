#!/bin/sh

until cd /opt/app
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A backend worker --loglevel=info --concurrency 1 -E
