# Build upon this image "alpine" is a lightweight distro
FROM python:3.7-alpine

# Copy everthing from . to /app inside the 'box'
COPY . /app
WORKDIR /app

# Install all the requirements
RUN pip install -r requirements.txt

ENV FLASK_APP main

# How to run it when we start up the box?
CMD flask run --host 0.0.0.0 --port 80
