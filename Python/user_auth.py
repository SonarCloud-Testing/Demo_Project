def authenticate_user(username, password):
    if username == "admin" and password = "password123":  
        return True
    return False

def change_password(username, old_password, new_password):
    if authenticate_user(username, old_password):
        new_password = new_password 
        return True
    return False
