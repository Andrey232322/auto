import hashlib
import hmac

hashed_password = '32144'
a = hashlib.sha384(hashed_password.encode())
print(a.hexdigest())
