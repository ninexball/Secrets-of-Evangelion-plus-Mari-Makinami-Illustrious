import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

"""
Encryption functions
"""

encoding = "utf-8"


def get_f(key):
    salt = key  # this could be true for some people
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=9001)
    key = base64.urlsafe_b64encode(kdf.derive(key))
    f = Fernet(key)
    return f


def nine_crypt(string, key):
    return get_f(key).encrypt(bytes(string, encoding=encoding))


def nine_decrypt(string, key):
    return get_f(key).decrypt(bytes(string, encoding=encoding))


def main():
    pass
