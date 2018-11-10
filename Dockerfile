FROM python:2-stretch
COPY . /openfisca
WORKDIR /openfisca
RUN pip install -e .
CMD [ "/usr/local/bin/openfisca", "serve", "--port", "5000" ]
