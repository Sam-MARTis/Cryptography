import rsa
import os



with open('private.pem', 'rb') as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    

for fileToDencrypt in os.listdir('.'):
    if fileToDencrypt.endswith('.pem') or fileToDencrypt.endswith('.py'):
        continue

    try:

        with open(fileToDencrypt, 'rb') as f:
            file = f.read()

        message = rsa.decrypt(file, private_key)

        with open(fileToDencrypt, 'wb') as f:
            f.write(message)
    except:
        print("Decription failed: ", fileToDencrypt)