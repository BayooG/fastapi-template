# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

#copy code to container
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt
