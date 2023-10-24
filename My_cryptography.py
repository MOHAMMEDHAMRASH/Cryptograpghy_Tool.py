from cryptography.fernet import Fernet

# Generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key from a file
def load_key():
    try:
        with open("encryption_key.key", "rb") as key_file:
            key = key_file.read()
            return key
    except FileNotFoundError:
        print("Encryption key not found. Generate one first.")
        return None

# Encrypt a message
def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted message
def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Example usage
if __name__ == "__main__":
    action = input("Choose an action : \n 1.generate  \n 2.encrypt  \n 3.decrypt \n")

    if action == "generate" or action == "1":
    # Your code here
        generate_key()
        print("Encryption key generated.")
    elif action == "encrypt" or action == "2":
        key = load_key()
        if key:
            message = input("Enter a message to encrypt: ")
            encrypted_message = encrypt_message(key, message)
            print("Encrypted message:", encrypted_message)
    elif action == "decrypt" or action == "3":
        key = load_key()
        if key:
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(key, encrypted_message.encode())
            print("Decrypted message:", decrypted_message)
    else:
        print("Invalid action. Use 'generate', 'encrypt', or 'decrypt'.")
