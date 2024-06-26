import base64
import hvac
import os

# demo purposes, use identity-based access in prod
VAULT_ADDR = os.getenv('VAULT_ADDR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')


class Vault:
    def __init__(self):
        self.cl = hvac.Client(VAULT_ADDR, VAULT_TOKEN)
        self.transit_mount = "transit"
        self.transit_key = "example"
        self.transform_mount = "transform"
        self.transform_role = "payments"

    def _b64e(self, m):
        return base64.b64encode(m.encode()).decode()

    def _b64d(self, m):
        return base64.b64decode(m).decode()

    def encrypt(self, m):
        r = self.cl.secrets.transit.encrypt_data(
            mount_point=self.transit_mount,
            name=self.transit_key,
            plaintext=self._b64e(m)
        )
        return r["data"]["ciphertext"]

    def decrypt(self, m):
        r = self.cl.secrets.transit.decrypt_data(
            mount_point=self.transit_mount,
            name=self.transit_key,
            ciphertext=m
        )
        return self._b64d(r["data"]["plaintext"])

    def encode(self, m, transformation):
        r = self.cl.secrets.transform.encode(
            mount_point=self.transform_mount,
            role_name=self.transform_role,
            transformation=transformation,
            value=m,
        )
        return r["data"]["encoded_value"]

    def decode(self, m, transformation):
        r = self.cl.secrets.transform.decode(
            mount_point=self.transform_mount,
            role_name=self.transform_role,
            transformation=transformation,
            value=m,
        )
        return r["data"]["decoded_value"]
