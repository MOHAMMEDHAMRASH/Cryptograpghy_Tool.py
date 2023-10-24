# Cryptograpghy_Tool.py
 
The Python code I provided for the Cryptography Toolkit uses the Fernet encryption scheme, which is a symmetric key encryption algorithm. Fernet is a simple and secure way to perform symmetric (or "shared key") encryption, where the same key is used for both encryption and decryption.

Here's a brief explanation of how Fernet encryption works:

1. A random secret key is generated, which is used to both encrypt and decrypt data.

2. This secret key is used to create a Fernet key object.

3. To encrypt data, you use this key object to perform encryption, and to decrypt data, you use the same key object to perform decryption.

Fernet encryption is a part of the `cryptography` library in Python, which is a powerful library for various cryptographic operations. In the code I provided, Fernet is used for encrypting and decrypting messages.

Please note that Fernet is a symmetric encryption algorithm, meaning that the same key is used for both encryption and decryption. In more complex scenarios, such as public-key cryptography, asymmetric encryption algorithms like RSA may be used, where different keys are used for encryption and decryption. However, the provided code uses Fernet for simplicity and ease of use.
