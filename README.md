# Starkflow Celery Periodic Task using Docker

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rajeshthangaraj1/starkflow.git
$ cd starkflow
```

Run the docker compose to create a docker image using below command:

```
docker-compose run django
```

Run the docker compose to create a docker container using below command:

```
docker-compose up
```
And navigate to `http://127.0.0.1:8000/`.

Once run the container , celery periodic task will start to execute every 1 minute.

#API Flow

Method GET : Return exchange rate list fetching form db.
```
http://127.0.0.1:8000/api/v1/quotes
```

Method POST : Return exchange rate fetching from direct Live api.
```
http://127.0.0.1:8000/api/v1/quotes
```
