#!/bin/bash

# setup
vault operator init -key-shares=1 -key-threshold=1 -format=json > init.json
vault operator unseal $(cat init.json | jq -r .unseal_keys_hex[0])
export VAULT_TOKEN=$(cat init.json| jq -r .root_token)



# transit
vault secrets enable transit

vault write transit/keys/example type="aes256-gcm96"



# transform
vault secrets enable transform

vault write transform/role/payments transformations=ccn

vault write transform/transformations/fpe/ccn \
  template="builtin/creditcardnumber" \
  tweak_source=internal \
  allowed_roles=payments
