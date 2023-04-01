import random

def generate_key(length):
    """Generates a random key of the given length"""
    key = ''
    for i in range(length):
        key += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return key

def encrypt(plaintext, key):
    """Encrypts the plaintext using the given key"""
    ciphertext = ''
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

def decrypt(ciphertext, key):
    """Decrypts the ciphertext using the given key"""
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))
    return plaintext

# get the plaintext from the user
plaintext = input("Enter the plaintext to encrypt: ")

# generate a random key of the same length as the plaintext
key = generate_key(len(plaintext))

# encrypt the plaintext using the key
ciphertext = encrypt(plaintext, key)

print("Key: " + key)
print("Ciphertext: " + ciphertext)

# decrypt the ciphertext using the key
decrypted_plaintext = decrypt(ciphertext, key)

print("Decrypted plaintext: " + decrypted_plaintext)
