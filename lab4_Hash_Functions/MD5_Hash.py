from hashlib import md5

hash_object = md5(b'Hello World')
print(f"MD5 Hash: {hash_object.hexdigest()}")
