from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # DES key must be 8 bytes
cipher = DES.new(key, DES.MODE_CBC)
plaintext = b'Hello World!'

padded_text = pad(plaintext, DES.block_size)
ciphertext = cipher.encrypt(padded_text)
print(f"Ciphertext: {ciphertext}")

# Decrypt
decipher = DES.new(key, DES.MODE_CBC, cipher.iv)
decrypted_text = unpad(decipher.decrypt(ciphertext), DES.block_size)
print(f"Decrypted text: {decrypted_text.decode()}")
