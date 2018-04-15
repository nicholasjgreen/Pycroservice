@echo off

@echo Preparing cassandra
python setup\cass.py

@echo Preparing rabbitmq
python setup\rabb.py