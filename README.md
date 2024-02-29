# Usage

An overview of the project.

## Env configuration

Create `.env` file and fill data:

```shell
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*
CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
POSTGRES_DB=test
POSTGRES_USER=test
POSTGRES_PASSWORD=test
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

## Instructions on how to build and run your application using Docker Compose

1. Run Docker Compose command:

    ```
    docker-compose up -d --build
    ```
   
2. Run Unit tests:

    ```
    docker-compose exec app pytest
    ```

## Work with app

1. Swagger UI `http://localhost:8000/docs`.

2. ReDoc `http://localhost:8000/redoc`.

3. Admin panel Jazzmin `http://localhost:8000/admin`. 

## How to use the API

To use API I set IsAuthenticatedOrReadOnly permission, which means you must 
be authenticated to Create, Edit or Delete in Database.

To create user follow instructions in swagger:

- Send email, password and password2 to `/register/` endpoint
- Send this email and password to `/login/` endpoint to obtain token
- Add this token with prefix "Token" to Authorization header
- After you can fully use CRUD

# Validation

To Establishement API I set validation:

- Field `location` must contain real address in Bishkek city on russian language
- Fields `opening_hour` and `closing_hour` use format "%H:%M" and should be `10:00`
- Field `opening_hours` is concatenation or two fields `opening_hour` and `closing_hour`
