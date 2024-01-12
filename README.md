
# IE-PROJECT

Purpose: Machine learning web application using Django and Yolov8

## Acknowledgements

 - [Django](https://www.djangoproject.com/)
 - [Yolov8](https://docs.ultralytics.com/)

## Installation

Install PostgresSQL
- [Python](https://www.python.org/)
- [PostgresSQL](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/)

Clone project
```bash
  git clone git@github.com:lunica101/ie-project.git
  cd ie-project
```

Activate Python environment and install python library package
```bash
  python -m venv env
  pip install -r requirements.txt
```

Migrate database for creating database
```bash
    python manage.py migrate
```

Run Django project
```bash
    python manage.py runserver
```

## API Reference

####  Show ML form input

```http
  GET /
```

#### Display ML history
```http
  GET /history
```

#### Show ML conclusion result

```http
  POST /result
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `image`        | `string` | **Required**. Image Type Jpeg and PNG |
| `description`      | `text` | String phoneNumber not blank |
