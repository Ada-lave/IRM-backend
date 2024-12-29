docker compose up --build -d
docker exec -it irm-server python manage.py collectstatic --noinput
docker exec -it irm-server python manage.py migrate
docker exec -it irm-server python manage.py seed_all 