ARG PYTHON_VERSION=3.11.9

FROM python:${PYTHON_VERSION}-slim-bullseye

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]
