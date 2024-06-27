## Usage


```shell
python3 -m venv venv
./venv/bin/python -m pip install -r requirements.txt
```

```shell
cd tf/
# add `vault_license` to .auto.tfvars
terraform init
terraform apply
export VAULT_ADDR=$(terraform output -raw vault_addr)
```

```shell
cd ..

# wait for vault to be ready
vault status

vault operator init -key-shares=1 -key-threshold=1 -format=json > init.json
vault operator unseal $(cat init.json | jq -r .unseal_keys_hex[0])
export VAULT_TOKEN=$(cat init.json| jq -r .root_token)

# setup vault
source setup.sh

# run webapp
./venv/bin/python ./run.py
```
