FROM python:3.12.8-alpine3.21

LABEL maintainer="neyranievesjonathan@gmail.com"

WORKDIR /application
COPY requirements.txt /tmp/requirements.txt
COPY app.py ./
COPY infrastructure ./infrastructure

EXPOSE 5000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -Rf /tmp

ENV PATH="/py/bin/:$PATH"

CMD ["python", "app.py"]
