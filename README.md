# drf notes app

## Project Motivation

This project is undertaken with the aim of creating and scaling online notes app to save to the cloud .With the aim of exploring new technologies and contributing to a larger cause, the project is driven by my motivation to learn python and grasp it more clearly.


## Virtual environment setup

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

## Environment variables setup

Create a `.env` file in the **root directory** and add the following variables in the .env.example file.

### NB:

The default database is **sqlite3** on local environment. If you want to use postgresql(or any other), then make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the **DB_IS_AVAIL** variable in **config.settings.local** is set to **True**.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run migrations

If you don't set the DB variables in the .env file, then the default database is sqlite3.

```bash
python manage.py migrate
```

## Run local server

```bash
python manage.py runserver
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Other Requirements

- AWS S3 bucket <https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html>
- AWS IAM user with access to the S3 bucket <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>
- Sentry account <https://sentry.io/>

### Note

Make sure you set the environment variables in the .env for the database as shown in the .env.example file so that the DATBASE_URL, AWS S3 variables & SENTRY variables are set.

```bash
python manage.py runserver
```

## Docker setup

### Note

The database being used in this project is sqlite3

### Build image and run container

```bash
docker-compose up --build
```

### List images

```bash
docker images
```

### List containers

```bash
docker ps
```
