FROM python:3.6

MAINTAINER Vasista Reddy "vasista.1245@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential python3-dev nginx
RUN pip install -U gunicorn

# Make working directory
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app

# Install ldap requirements
RUN pip install -r requirements.txt

# Copy project to docker work directory
ADD . /app

EXPOSE 5055

# Run using gunicorn
CMD ["gunicorn", "--name=test", "--bind=0.0.0.0:5055", "--log-level=DEBUG", "--workers=3", "--timeout=6000" ,"wsgi:app"]
