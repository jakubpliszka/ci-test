FROM python:3.9-slim

COPY . /test
WORKDIR /test
RUN pip install pytest
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null