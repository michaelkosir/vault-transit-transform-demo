#!/bin/bash

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
