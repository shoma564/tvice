#!/bin/bash
rm -rf ./db/data
chmod 711 ./db/my.cnf
sleep 1
docker-compose down --rmi all --volumes --remove-orphans
docker-compose down -v
sleep 1
docker-compose build
docker-compose up
