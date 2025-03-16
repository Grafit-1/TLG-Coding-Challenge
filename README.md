# TLG-Coding-Challenge

eine route die ganze liste von orten und deren wetter zurückgibt

eine route die liste von orts ids und kundenname nimmt und eine destination schedule in der db erstellt

tests für die routen

run
```
docker compose up --build
```

docker compose run django-web python manage.py migrate


docker compose run django-web python manage.py test api