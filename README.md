<h1 align="center">FastAPI + Prometheus + Grafana :tada:</h1>

This is a minimal setup that you can build to monitor your FastAPI microservice.

## Installation

There are only two prerequisites:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Having both, you'll need to clone the repository:

``` bash
git clone https://github.com/pythoninthegrass/fastapi-prometheus-grafana.git
```

## Usage

You'll need to run the docker containers:

``` bash
docker compose up -d
```

Now you have access to those three containers and their respective ports:

* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000/
* FastAPI: http://localhost:8000/

On the FastAPI, you can access `/metrics` endpoint to see the data Prometheus is scraping from it.

To logi into Grafana, the default credentials are:
`admin` / `pass@123` with the password set in [config.monitoring](grafana/config.monitoring).

## How it looks like

<p align="center">
  <img src="./static/dashboard.jpeg">
</p>

## References

* [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
* [Generate and Track Metrics for Flask API Applications Using Prometheus and Grafana](https://medium.com/swlh/generate-and-track-metrics-for-flask-api-applications-using-prometheus-and-grafana-55ddd39866f0)
* [PromQL for Humans](https://timber.io/blog/promql-for-humans/)
* [Sign in to Grafana | Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/sign-in-to-grafana/)
* [Configure a Grafana Docker image | Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/)
* [Configure Grafana | Grafana documentation](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/)
* [Install Loki with Docker or Docker Compose | Grafana Loki documentation](https://grafana.com/docs/loki/latest/setup/install/docker/#install-with-docker-compose)
