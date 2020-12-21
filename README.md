# devtest_api_testing

#command to build docker container
sudo docker build -t devtest_image .

#command to run docker image with test_restapis.py
docker run -it devtest_image test_restapis.py
