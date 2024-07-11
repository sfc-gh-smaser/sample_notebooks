from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
def get_private_key(keyfile):
    return get_private_key_passwd(keyfile, None)

def get_private_key_passwd(keyfile,passwd):
  with open(keyfile, "rb") as key:
    p_key= serialization.load_pem_private_key(key.read(),password=passwd,backend=default_backend())
    pkb = p_key.private_bytes(
      encoding=serialization.Encoding.DER,
      format=serialization.PrivateFormat.PKCS8,
      encryption_algorithm=serialization.NoEncryption()
    )
    return pkb
