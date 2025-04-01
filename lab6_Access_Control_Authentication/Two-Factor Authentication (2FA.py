# pip install pyotp //First install library

import pyotp
import hashlib

# User database (for demonstration)
users = {"Alice": {"password": hashlib.sha256("secure123".encode()).hexdigest(), "secret": pyotp.random_base32()}}

# Function to authenticate user with password
def authenticate_password(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username]["password"] == hashed_password:
            return True
    return False

# Function to authenticate user with OTP
def authenticate_otp(username):
    totp = pyotp.TOTP(users[username]["secret"])
    otp = totp.now()
    print(f"Generated OTP: {otp}")
    user_otp = input("Enter the OTP: ")
    return totp.verify(user_otp)

# Main authentication function
def two_factor_auth():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if authenticate_password(username, password):
        print("Password verified!")
        if authenticate_otp(username):
            print("Two-Factor Authentication Successful!")
        else:
            print("OTP Verification Failed!")
    else:
        print("Incorrect Username or Password!")

# Run 2FA system
two_factor_auth()
