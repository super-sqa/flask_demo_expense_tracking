FROM ubuntu:latest


# install required packages
RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev vim

# create a dicrectory for our app
RUN mkdir /my_flask_app
COPY . /my_flask_app