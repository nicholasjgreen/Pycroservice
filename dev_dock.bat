docker run -ti -p8080:8080 --network=pycroservice_app-tier -v c:/dev/pycroservice/src:/usr/src/app -w /usr/src/app -e rabb_hostname=pycroservice_rabbitmq_1 -e cass_hostname=pycroservice_cassandra_1 mypy /bin/sh