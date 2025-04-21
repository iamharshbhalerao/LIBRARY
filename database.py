def authenticate(username, password):
    if username == 'admin' and password == 'password':
        return True
    else:
        return False
