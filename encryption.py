##Develop a script to encrypt files on the system for security purposes.
from cryptography.fernet import Fernet
import os
import datetime


def generate_key():
    return Fernet.generate_key()


def load_key_from_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def save_key_to_file(key, file_path):
    with open(file_path, 'wb') as file:
        file.write(key)


def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path + ".encrypted", 'wb') as file:
        file.write(encrypted_data)

def update_encryption_details(file_path, key, txt_file):
    with open(txt_file, 'a') as f:
        f.write(f"File Name: {os.path.basename(file_path)}\n")
        f.write(f"File Path: {os.path.abspath(file_path)}\n")
        f.write(f"Encryption Date: {datetime.datetime.now()}\n")
        f.write(f"Encryption Key: {key.decode('utf-8')}\n\n")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to encrypt: ")
    
    if not os.path.exists(file_path):
        print("File not found.")
        exit()

    
    key = generate_key()
    
    key_file_path = "encryption_key.key"
    save_key_to_file(key, key_file_path)
    
   
    encrypt_file(file_path, key)
    
    
    txt_file = "encryption_details.txt"
    update_encryption_details(file_path, key, txt_file)
    
    print(f"File '{file_path}' encrypted successfully.")
