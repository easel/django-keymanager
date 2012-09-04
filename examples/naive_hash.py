from hashlib import sha224

users = ([1, 'bob', 'secret'],[2, 'alice', 'sekrit'], [3, 'eve', 'secret'])

for user in users:
    user[2] = sha224(user[2]).hexdigest()[:8]

print users
