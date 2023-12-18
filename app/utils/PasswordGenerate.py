from app import bcrypt
def setPassword(password):
    return bcrypt.generate_password_hash(password)

def checkPassword(pw_hash, password):
    return bcrypt.check_password_hash(pw_hash, password)

