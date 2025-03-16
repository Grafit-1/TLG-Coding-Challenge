# TLG-Coding-Challenge

run
```
docker compose up --build
```

migrate
```
docker compose run django-web python manage.py migrate
```

execute tests
```
docker compose run django-web python manage.py test api
```