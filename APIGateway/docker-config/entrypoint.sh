#!/bin/bash

# Navigate to the Laravel root directory (if not already there)
cd /var/www/html

# Check if the .env file exists, and if not, copy the example file
if [ ! -f ".env" ]; then
    cp .env.example .env
fi

# Generate application key
php artisan key:generate

# Run database migrations
# Note: Ensure your database is accessible at this point
# You might want to add checks or retries if your DB is in another container
php artisan migrate --force

# Start Apache (moved to CMD in Dockerfile)
# apache2-foreground

# Execute the main command (CMD in Dockerfile) if passed any
exec "$@"
