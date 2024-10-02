#!/bin/bash

echo "🚀 Starting deployment..."

# Name of the service to restart (e.g., service name in the docker-compose file)
SERVICE_NAME="photos"
# Docker Compose file (adjust if necessary)
COMPOSE_FILE="docker-compose.prod.yml"
# Time to wait between restarting each replica (e.g., 30 seconds)
RESTART_DELAY="30s"

# Check if there are any running containers for the service
CONTAINER_IDS=$(docker compose -f $COMPOSE_FILE ps -q $SERVICE_NAME)

TOTAL_CONTAINERS=$(echo "$CONTAINER_IDS" | wc -w)

if [ -z "$CONTAINER_IDS" ]; then
    echo "⚠️ No containers found for the service '$SERVICE_NAME'. Starting the service."
    docker compose -f $COMPOSE_FILE up -d
    exit 0
fi

# # Restart each container one at a time
INDEX=0

for CONTAINER_ID in $CONTAINER_IDS; do
    INDEX=$((INDEX + 1))

    # Restart the container
    echo "🔄 Restarting container $CONTAINER_ID..."
    docker stop $CONTAINER_ID
    docker start $CONTAINER_ID

    # Check if the current container is the last one
    if [ $INDEX -eq $TOTAL_CONTAINERS ]; then
        echo "✅ All containers for the service '$SERVICE_NAME' have been restarted."
        exit 0
    fi

    echo "✅ Container $CONTAINER_ID has been restarted."
    echo "⏳ Waiting for $RESTART_DELAY before restarting the next container..."

    # Wait for the specified delay before restarting the next container
    sleep $RESTART_DELAY
done

echo "✅ All containers for the service '$SERVICE_NAME' have been restarted."

echo "🚀 Deployment completed."
