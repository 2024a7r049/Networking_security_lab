def vigenere_encryption(text, key):
    encrypted = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord("a")

            if char.islower():
                new_pos = (ord(char) - ord("a") + shift) % 26
                encrypted += chr(new_pos + ord("a"))
            else:
                new_pos = (ord(char) - ord("A") + shift) % 26
                encrypted += chr(new_pos + ord("A"))

            key_index += 1
        else:
            encrypted += char

    return encrypted


def vigenere_decryption(text, key):
    decrypted = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord("a")

            if char.islower():
                new_pos = (ord(char) - ord("a") - shift) % 26
                decrypted += chr(new_pos + ord("a"))
            else:
                new_pos = (ord(char) - ord("A") - shift) % 26
                decrypted += chr(new_pos + ord("A"))

            key_index += 1
        else:
            decrypted += char

    return decrypted


plaintext = input()
key = input()

ciphertext = vigenere_encryption(plaintext, key)
decrypted = vigenere_decryption(ciphertext, key)

print("Plaintext :", plaintext)
print("Encrypted :", ciphertext)
print("Decrypted :", decrypted)








