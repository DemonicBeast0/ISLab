from hashlib import sha1

hash_object = sha1(b'Hello World')
print(f"SHA-1 Hash: {hash_object.hexdigest()}")
