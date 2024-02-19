import rsa

pub_key, priv_key = rsa.newkeys(512)
print(priv_key.save_pkcs1())
with open('private.pem', 'wb') as f:
    f.write(priv_key.save_pkcs1())
with open('public.pem', 'wb') as f:
    f.write(pub_key.save_pkcs1())

