# Build upon this image "alpine" is a lightweight distro
FROM python:3.7-alpine

# Copy requirements.txt
COPY ./requirements.txt /app/requirements.txt

# Install all the requirements
RUN pip install -r /app/requirements.txt

# Copy everthing from . to /app inside the 'box'
COPY . /app
WORKDIR /app

# How to run it when we start up the box?
CMD ["./factor_worker.py"]
