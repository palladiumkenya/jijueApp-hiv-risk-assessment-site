# jijue application

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/palladiumkenya/jijueApp-hiv-risk-assessment-site.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Update database credentials save and run migrations:

```
(env)$ nano settings
(env)$ cd ..
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

Run the server:

```
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/

ALL SET.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:

```sh
(env)$ python manage.py test
```

## Docker set up
```sh
https://github.com/palladiumkenya/jijueApp-hiv-risk-assessment-site.git
docker-compose up -d
```
You can now access the server at http://localhost:8000
