# ML model dockerized

We are going to build a Docker image to expose a machine learning api.
The api call takes a text as argument and predicts the personality of the person who wrote it.

The models have been build using the following dataset:

- [(MBTI) Myers-Briggs Personality Type Dataset](https://www.kaggle.com/datasnaek/mbti-type)

This is a small dataset so, we can't take too seriously the results but, it's a starting point to build more complex systems.
The Machine Learning model is serialized and included into a docker image.

## How to build the docker image:
```
docker build -t ml-api-docker:latest .
```

## How to run the docker container:

```
docker run -d -p 5000:5000 ml-api-docker:latest
```

## How to use the ML service

To test the api service is working:
http://localhost:5000

It will be possible to send a text (msg variable):
http://localhost:5000/predict?msg=very%20happy%20experience

## TODO

- Add a model to predict the sentiment of the text
- To use WSGI for production environment
- Create a serverless version (to be deployed in AWS or GCP)
