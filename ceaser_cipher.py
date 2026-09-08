def caesar_encryption(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                new_pos = (ord(char) - ord('a') + shift) % 26
                encrypted += chr(new_pos + ord('a'))
            else:
                new_pos = (ord(char) - ord('A') + shift) % 26
                encrypted += chr(new_pos + ord('A'))
        else:
            encrypted += char

    return encrypted


def caesar_decryption(text, shift):
    return caesar_encryption(text, -shift)


plaintext = "Network Security"
shift = 3

ciphertext = caesar_encryption(plaintext, shift)
decrypted = caesar_decryption(ciphertext, shift)

print("Plaintext :", plaintext)
print("Encrypted :", ciphertext)
print("Decrypted :", decrypted)