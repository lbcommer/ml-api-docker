# ML model dockerized

We are going to build a Docker image to expose a machine learning api

## How to build the docker image:

docker build -t ml-api-docker:latest .

## How to run the docker container:

docker run -d -p 5000:5000 ml-api-docker:latest

## How to use the ML service

http://localhost:5000

http://localhost:5000/predict?msg=very%20happy%20experience

## TODO

- To use WSGI for production
