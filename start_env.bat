@echo off

echo Starting Cassandra
docker run -d --name cassandra-server -p 9042:9042 --network app-tier bitnami/cassandra:latest