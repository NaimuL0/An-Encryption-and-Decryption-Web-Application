# aes_encryption.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 16-byte key (must be 16, 24, or 32 bytes long)
KEY = b'0172791540609876'

def encrypt(plain_text):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct}

def decrypt(iv, cipher_text):
    iv = base64.b64decode(iv)
    cipher_text = base64.b64decode(cipher_text)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return pt.decode('utf-8')
