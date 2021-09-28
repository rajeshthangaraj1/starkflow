# Starkflow Celery Periodic Task using Docker

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/rajeshthangaraj1/starkflow.git
$ cd starkflow
```

From the project root, create the images and spin up the Docker containers:

```
docker-compose up -d --build
```

Run the docker compose to create a docker container using below command

```
docker-compose up
```
And navigate to `http://127.0.0.1:8000/`.

Once run the container , celery periodic tasks will start to execute every 1 minute.

## API Flow

Method GET : Return exchange rate list fetching from db.
```
http://127.0.0.1:8000/api/v1/quotes
```

Method POST : Return exchange rate fetching from direct Live API.
```
http://127.0.0.1:8000/api/v1/quotes
```
## API ACCESS TOKEN KEY

To access the API key token method,we need to create a super user, so just go to view.py and uncomment the line number 30 and navigate to `http://127.0.0.1:8000/`.

We need to create a api key token using superuser creaditial through below api link

```
http://127.0.0.1:8000/api/token/

```
Once the token api key is created, just use that access token to authentication Bearer token method to access the get and post API.
