from hashlib import sha224

salt = 'aNiceLongSecret'
users = ([1, 'bob', '123456789'],[2, 'alice', '123456780'], [3, 'eve', '123456781'])

for user in users:
    user[2] = sha224(salt + user[2]).hexdigest()[:8]

print users

# if you don't have the secret salt, you can't
print sha224('123456789').hexdigest()[:8]
