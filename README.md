## Key Commands for deployment

### Start the Application in Detached Mode
docker-compose up -d

### Apply Database Migrations
docker-compose run --rm web python manage.py migrate

### Collect Static Files for Production
docker-compose run --rm web python manage.py collectstatic --noinput

### Create a Django Superuser
docker-compose run --rm web python manage.py createsuperuser

### Restart All Running Containers
docker-compose restart

### Stop and Remove All Containers and Volumes
docker-compose down -v

### Stop and Remove All Containers, Volumes, and Images
docker-compose down -v --rmi all