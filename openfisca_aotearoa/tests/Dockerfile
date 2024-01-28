FROM python:3.7.2-stretch
WORKDIR /app

COPY setup.py /app/setup.py
COPY setup.cfg /app/setup.cfg
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
  pip install numpy'<1.16,>=1.11' && \
  pip install -r /app/requirements.txt && \
  pip install -e '.[test]'

CMD [ "openfisca-run-test", "--country-package", "openfisca_aotearoa", "openfisca_aotearoa/tests" ]
