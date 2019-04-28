# flaskapi_test_docker
The purpose of this project is to serve as <b>test API</b> to work with some other applications.

Ex: To work with API Gateways, one needs an test API to checkout Gateways(KONG API Gateway) features like Authentication, ratelimiting, logging, analysis, etc.,


# Build the docker

docker build . -t flask:test


# Run the docker

docker run -p 5055:5055 -d flask:test


# endpoints

/api/v1/test1


/api/v1/test2


Ex: http://127.0.0.1:5055/api/v1/test1
