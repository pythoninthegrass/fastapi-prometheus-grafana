ARG PYTHON_VERSION=3.11.9

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]
