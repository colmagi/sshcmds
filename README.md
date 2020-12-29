# sshcmds
This project includes Python utilities for ssh activities

# Requirements
An installation of Python 3.8.2 or later

# Installation
Install using pip, e.g.:
Note: To find your python version, run python3 --version. Comm python executable names are python, python3.

```sh
python3 -m pip install sshcmds
```

# Setup the Hashicorp vault for storing secrets.
# Startup server: vault server -dev
```sh
vault server -dev
```
# set environment on windows 10: 
```sh
set VAULT_ADDR=http://127.0.0.1:8200
```
# login with token: Root Token:
```sh
vault login
```
# Enable path kv-v1:
```sh
vault secrets enable -path="kv-v1" kv
```
# Create secret key pairing
```sh 
vault kv put kv-v1/<PATH> <KEY>=VALUE>
```
# Read secret
```sh
vault kv get kv-v1/<PATH>
```
