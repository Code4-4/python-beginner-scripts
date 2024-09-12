# file_encryptor.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    encrypted = cipher.encrypt(plaintext)
    with open(file_path + ".enc", 'wb') as file:
        file.write(encrypted)
    print(f"File encrypted and saved as {file_path}.enc")

if __name__ == "__main__":
    path = input("Enter the file path to encrypt: ")
    key = generate_key()
    encrypt_file(path, key)
    print(f"Encryption key: {key.decode()}")
