import base64
import rsa
from Crypto.PublicKey import RSA
from temp import *

# pub,priv = new_keys(2048)
# export_private_key(priv)
# export_public_key(pub)

if __name__ == '__main__':
    with open("public_key", "rb") as f:
        pub = f.read()
    pub = import_key(pub)
    print(pub)

    b = base64.b64encode(encrypt(b'twelcon', pub))

    print(b)