FROM ubuntu:latest


# install required packages
RUN apt-get update && apt-get install --no-install-recommends -y python3.8 python3-pip python3.8-dev vim


# create a dicrectory for our app
RUN mkdir /my_flask_app
COPY . /my_flask_app

# change working directory
WORKDIR /my_flask_app

# install requirements
RUN python3 -m pip install -r requirements.txt


# expose the port being used by the app
EXPOSE 8889

# run this command when container starts
CMD python3 /my_flask_app/run.py
