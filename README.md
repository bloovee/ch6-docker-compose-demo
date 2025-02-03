docker-compose up -d
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py collectstatic --noinput
docker-compose run --rm web python manage.py createsuperuser
docker-compose restart
docker-compose down -v --rmi all