# webapp-python
![webapp-python](https://github.com/matandomuertos/webapp-python/actions/workflows/dockerBuild.yaml/badge.svg)
![webapp-python-helm](https://github.com/matandomuertos/webapp-python/actions/workflows/helmChartRelease.yaml/badge.svg)

Basic web app made in Python using flask as web framework and psutil and uuid libraries to get system information.

## Running the app
### Setting up locally
1. Clone the repository: `git clone https://github.com/matandomuertos/webapp-python.git`
2. Navigate to the main folder and install requirements: `cd webapp-python/app && pip install -r requirements.txt`
3. Run the app `python main.py`
4. Go to `http://127.0.0.1:8080` in your prefered browser to use the app

### Run the app on Docker
1. [Install Docker](https://docs.docker.com/engine/install/)
2. Run `docker run -p 8080:8080 -d ghcr.io/matandomuertos/webapp-python` in your terminal
3. Go to `http://127.0.0.1:8080` in your prefered browser to use the app

### Run the app on Kubernetes (using helm)
The helm chart is released to [ghcr.io](ghcr.io) automatically by [Github actions](https://github.com/matandomuertos/webapp-python/actions).

1. Add the repo to helm `helm repo add webapp-python https://matandomuertos.github.io/webapp-python`
2. Update the repos `helm repo update`
3. Deploy to k8s `helm install webapp webapp-python/helm`
If you want to customize the deployment, please check the [values file](./charts/webapp/values.yaml).

#### Optional
- Test helm deployment: `helm test webapp`
- Uninstall deployment: `helm uninstall webapp`

## Docker image build
The Docker image is build and pushed to [ghcr.io](ghcr.io) automatically by [Github actions](https://github.com/matandomuertos/webapp-python/actions). 

### Build image manually
1. Clone the repository: `git clone https://github.com/matandomuertos/webapp-python.git`
2. Navigate to the main folder: `cd webapp-python/app`
3. Build the image: `docker build -t webapp-python .`

## Usage
- `http://127.0.0.1:8080/-/health` shows system information.
#### Example
```
{"architecture":"aarch64","health":"healthy","hostname":"webapp-python","mac-address":"01:41:wx:14:00:03","platform":"Linux","platform-release":"5.10.104-linuxkit","platform-version":"#1 SMP PREEMPT Thu Mar 17 17:05:54 UTC 2022","processor":"","ram":"12 GB"}
```
- `http://127.0.0.1:8080/api/echo?text=hello` shows the input text as key.
#### Example
```
{"key":"hello"}
```