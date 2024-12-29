# Введение
Данное краткое руководство описывает то как осуществлять первый и последующие запуски серверной части приложения.

# Системные требования
Для работы сервера необходима система с следующими минимальными требованиями:
- ОС: Ubuntu 22.04 или Windows 10/11
- Процессор от 2x ядер
- RAM: 4GB
- 100GB HDD

# Сборка сервера
Для сборки сервера необходима система контейнеризации такая как Docker и его инструмент docker compose.

После установки перечисленных утилит, вам необходимо будет перейти в папку с проектом и выполнить следующие действия перед начальным запуском:

1. в папку irm_backend вам необходимо перенести папку static.
2. запустить команды 
```sh
docker compose up --build -d
docker exec -it irm-server python manage.py collectstatic --noinput
docker exec -it irm-server python manage.py migrate
docker exec -it irm-server python manage.py seed_all 
docker exec -it irm-server python create_superuser.py
```

# Последующие запуски
Во время последующих запусков вам необходимо будет запускать команду `docker compose up`

# Вход в админ панель
Войти в админ панель можно по адресу `http://localhost:8100/admin/`
Логин: root
Пароль: root
