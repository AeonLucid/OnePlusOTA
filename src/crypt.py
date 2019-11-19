import string
from base64 import b64decode, b64encode
from random import randint, choices

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

keys = ["oppo1997", "baed2017", "java7865", "231uiedn", "09e32ji6",
        "0oiu3jdy", "0pej387l", "2dkliuyt", "20odiuye", "87j3id7w"]


def get_key(key: str):
    one = keys[int(key[0])]
    two = key[4:12]

    return (one + two).encode('UTF8')


def generate_key():
    key_id = str(randint(0, 10))
    key = ''.join(choices(string.ascii_letters + string.digits, k=14))

    return key_id + key


def encrypt(data_plain: str) -> str:
    key_pseudo = generate_key()
    key_real = get_key(key_pseudo)

    cipher = AES.new(key_real, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(data_plain.encode('UTF8'), AES.block_size))

    return b64encode(encrypted).decode('UTF8') + key_pseudo


def decrypt(data_encrypted: str) -> str:
    data = b64decode(data_encrypted[:-15])
    key = get_key(data_encrypted[-15:])

    cipher = AES.new(key, AES.MODE_ECB)
    plain = unpad(cipher.decrypt(data), AES.block_size)

    return plain.decode('UTF8')
