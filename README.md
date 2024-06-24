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

# setup vault
source setup.sh

# run webapp
./venv/bin/python ./run.py
```
