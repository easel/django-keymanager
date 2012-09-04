# you might recognize this code: django/contrib/auth/hashers.py
from django.utils.crypto import (pbkdf2, 
  constant_time_compare, get_random_string)

def encode(password, salt=None, iterations=10000):
    if not salt:
        salt = get_random_string()
    hash = pbkdf2(password, salt, iterations)
    hash = hash.encode('base64').strip()
    return "%s$%d$%s$%s" % ('pbkdf2', iterations, salt, hash)

def verify(password, encoded):
    algorithm, iterations, salt, hash = encoded.split('$', 3)
    encoded_2 = encode(password, salt, int(iterations))
    return constant_time_compare(encoded, encoded_2)

users = ([1, 'bob', 'secret'],[2, 'alice', 'sekrit'], [3, 'eve', 'secret'])
print users

for user in users:
    user[2] = encode(user[2])

print users
print verify('secret', users[0][2]) # but we can still verify bob knows his own
