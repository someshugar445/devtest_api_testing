FROM python:3.8
MAINTAINER someshugar@gmail.com
COPY . /devtest
WORKDIR /devtest
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]