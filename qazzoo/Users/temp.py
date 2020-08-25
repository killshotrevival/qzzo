from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random


def new_keys(key_size):
   random_generator = Random.new().read
   key = RSA.generate(key_size, random_generator)
   private, public = key, key.publickey()
   return public, private

def import_key(externKey):
   return RSA.importKey(externKey)

def export_private_key(private_key):
       with open("private_key", "wb") as f:
            f.write(private_key.exportKey())

def export_public_key(public_key):
       with open("public_key", "wb") as f:
            f.write(public_key.exportKey())

def getpublickey(priv_key):
   return priv_key.publickey()

def encrypt(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)

def verify_data(data,priv_key,ciphertext):
   print('data ', type(data))
   d = decrypt(ciphertext, priv_key)
   print('decrp',type(d.decode('ASCII')) )
   return d.decode('ASCII') == data


# if __name__ == "__main__":
    
#     pb_k, pr_k = new_keys(1024)

#     export_private_key(pr_k)
#     export_public_key(pb_k)


