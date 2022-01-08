from Crypto.Cipher import AES
import binascii
import hashlib
from cryptography.hazmat.primitives import padding

class Signer24pay:

    def __init__(self, mid, key):
        self.iv = mid + mid[::-1]
        self.key = binascii.unhexlify(key)
	
#    def __pad(self, s):
#        return s + b" " * (AES.block_size - len(s) % AES.block_size)

    def sign(self, plaintext):
        message = hashlib.sha1(plaintext.encode('utf-8')).digest()
#       message = self.__pad(message)
        padder = padding.PKCS7(128).padder()
        message = padder.update(message) + padder.finalize()
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv.encode("utf8"))
        return binascii.hexlify(cipher.encrypt(message))[:32].upper()
