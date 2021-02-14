FROM python:3.8.7-slim-buster

WORKDIR /code
ADD setup.py README.rst MANIFEST.in .
ADD dgp dgp
ADD tests tests
RUN apt-get update && apt-get install -y g++\
        && pip install . \
        && rm -rf setup.py requirements tests README.rst MANIFEST.in

WORKDIR /usr/src/app
ENTRYPOINT ["/usr/local/bin/dgp"]


