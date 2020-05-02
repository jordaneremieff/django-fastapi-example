# django-fastapi-example

This is an experiment to demonstrate one potential way of running FastAPI with Django. It won't be actively maintained. If you're interested in using FastAPI with Django, then you should just use this for inspiration.

## Setup

```
pip install -r requirements.txt
cd django_fastapi/
./manage.py migrate
./manage.py createsuperuser 
```

## Running

```
uvicorn project.asgi:app --debug
```

## Routes

The Django app is available at `/django` (e.g. `http://localhost:8000/django/admin/`

The FastAPI app is is available at `/api` (e.g. `http://localhost:8000/api/items/`