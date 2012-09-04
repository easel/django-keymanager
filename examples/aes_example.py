from base64 import b64encode, b64decode
from M2Crypto.EVP import Cipher

from django.utils.crypto import get_random_string
from django.db.models import Model
from django.db.models.fields import TextField

class AESTextField(TextField):

class CryptoModel(Model)
    def _encrypt(key, iv, cleartext):
        cipher = Cipher(alg='aes_256_cbc', key=key, iv=iv, op=1) # 1=encode
        v = cipher.update(cleartext) + cipher.final()
        del cipher # clean up c libraries
        return b64encode(v)

    def _decrypt(key, iv, ciphertext):
        data = b64decode(ciphertext)
        cipher = Cipher(alg='aes_256_cbc', key=key, iv=iv, op=0) # 0=decode
        v = cipher.update(data) + cipher.final()
        del cipher  # clean up c libraries
        return v

(key, iv) = ('nicelongsekretkey', get_random_string(16))
ciphertext = encrypt(key, iv, 'a very long secret  1message')
print ciphertext
cleartext = _decrypt(key, iv, ciphertext)
print cleartext



