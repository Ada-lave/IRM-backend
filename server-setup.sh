docker compose up --build -d
docker exec -it irm-server python manage.py collectstatic --noinput