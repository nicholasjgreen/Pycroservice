# Pycroservice

This is an example micro service built with Python as a hack day experiment. 

## Features
* RESTful microservice
* API documentation in Swagger (OpenAPI)
* CQRS splitting read and update operations
* Updates are queued into RabbitMQ for eventual consistency
* Data persisted in Cassandra

## Dependencies
You will need the following dependencies
* Python 3.6
* Docker, Docker Compose

I recommend using virtualenv or similar to manage your python environment. Either way, you need to eventually pull the python packages you need which you can do by running pip
```bash
pip install -r requires.txt
```

## Getting started
The downstream dependencies (Cassandra and RabbitMQ) are hosted in containers and are defined in the docker-compose.yml file. To start the containers, simply invoke docker compose like this
```bash
docker-compose up
```

To create the message queues, cassandra key space and tables, use the following python scripts
```bash
python src/setup/cass.py
python src/setup/rabb.py
```


To start the REST api service, use connexion
```bash
connexion run swagger/recipes.yml -v --debug
```
You can then view the swagger UI at
```localhost:5050/ui```

### Things to write about still
* Update service
* Development environment in docker


### Wish list
* DI
* Unit tests
* Resilience
* Move connection settings into ENV


