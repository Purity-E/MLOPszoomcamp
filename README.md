# MLOPszoomcamp
This repo contains my work and projects from the MLOPs-zoomcamp

## Module 1
Introduction and set up

## Module 2
Experiment tracking

## Module 3
Workflow orchestration

## Module 4
Model deployment
- Used 'docker build -t duration-prediction-service .' to build the docker container
- Used 'docker run -it --rm duration-prediction-service 2021 4' to run the docker container

## Module 5
Model monitoring

## Module 6
Best practices
Writing tests
command for creating local stack - (aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration)
command for checking if the bucket was created - (aws --endpoint-url=http://localhost:4566 s3 ls)
command for checking created file on mock s3 - (aws --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration/in/)