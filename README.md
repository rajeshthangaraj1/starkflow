# Starkflow Celery Task

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rajeshthangaraj1/starkflow.git
$ cd starkflow
```

Run the docker compose webapp using below command:

```
docker-compose run django
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


## Project Flow

The scope of the project is online course portal for medical representative.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test starkflow
```
