#Text Encryption and Decryption using AES (Symmetric Key)

from cryptography.fernet import Fernet

# Generate a key (only needs to be done once)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_text(text):
    encoded_text = text.encode()
    encrypted_text = cipher.encrypt(encoded_text)
    return encrypted_text

def decrypt_text(encrypted_text):
    decrypted_text = cipher.decrypt(encrypted_text)
    return decrypted_text.decode()

# Usage
text = "Hello, World!"
encrypted_text = encrypt_text(text)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt_text(encrypted_text)
print("Decrypted Text:", decrypted_text)

#This requires the cryptography library; install it via pip install cryptography.
