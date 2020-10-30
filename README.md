# Vault and Jupyter Notebooks

## Vault
### Step 0: Generate OpenSSL certificate
This project contains with a self-signed OpenSSL ceretificate which should ONLY BE used for testing. Below are instructions to make your own
1. `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout conf/tls/<name>.key -out conf/tls/<name>.crt`

### Step 1: Spin up stack
1. `docker-compose build`
1. `docker-compose up -d`

### Step 2: Init Vault
1. Open a browser to `https://<Docker IP addr>:8443`
1. Enter `1` for Key Shares
1. Enter `1` for Key threshold
  1. Select Initialize
1. Select “Download keys”
1. Open terminal
1. `cat ~/Downloads/vault-cluster-*`
1. Back to browser
1. Select "Continue to Unseal”
1. Enter `<key from downloaded file>` into Master Key Portion
1. Select “Unseal”
1. Select “Token” for method
1. Enter `<root_token from downloaded file>` into sign in
1. Select “Sign In”

## Jupyter Notebooks
### Install/Setup
1. `virtualenv -p python3 venv`
1. `source venv/bin/activate`
1. `pip3 install -r requirements.txt`

## References
* [Github - Alpine Non-root User](https://github.com/mhart/alpine-node/issues/48)
* [Managing Secrets with Vault and Consul](https://testdriven.io/blog/managing-secrets-with-vault-and-consul/)
* [Vault - Filesystem Storage Backend](https://www.vaultproject.io/docs/configuration/storage/filesystem)
* [Resource limits, mlock, and containers, oh my](https://medium.com/@thejasongerard/resource-limits-mlock-and-containers-oh-my-cca1e5d1f259)
* [Github - Unable to build alpine-base image](https://github.com/smebberson/docker-alpine/issues/85)
* [Installing Vault](https://learn.hashicorp.com/vault/getting-started/install)
* [Github -hashicorp/docker-vault](https://github.com/hashicorp/docker-vault)
* [Github - testdrivenio/vault-consul-docker](https://github.com/testdrivenio/vault-consul-docker)
* [docker-vault/0.X/Dockerfile](https://github.com/hashicorp/docker-vault/blob/master/0.X/Dockerfile)
* [Delete Root](https://www.vaultproject.io/api-docs/secret/pki#delete-root)
* [Create a .pfx/.p12 Certificate File Using OpenSSL](https://www.ssl.com/how-to/create-a-pfx-p12-certificate-file-using-openssl/)
* [Client Authentication (mTLS)](https://docs.traefik.io/https/tls/#client-authentication-mtls)
* [docker-consul/0.X/Dockerfile](https://github.com/hashicorp/docker-consul/blob/master/0.X/Dockerfile)
* [consul-demo-tracing/datadog/consul_config/config.hcl](https://github.com/hashicorp/consul-demo-tracing/blob/master/datadog/consul_config/config.hcl)
* [Vault Configuration](https://www.vaultproject.io/docs/configuration)
* [Getting started with JupyterLab](https://jupyter.org/install)
* [Vault Agent Caching](https://www.vaultproject.io/docs/agent/caching)
* [[Vault 1.1 Beta] Vault Agent Caching](https://github.com/hashicorp/vault-guides/blob/master/identity/vault-agent-caching/README.md)
* [HashiCorp Vault with NGINX Reverse Proxy](https://www.reddit.com/r/devops/comments/asbh1g/hashicorp_vault_with_nginx_reverse_proxy/)
* []()
* []()
* []()