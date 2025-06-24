# Caesar Cipher - Kriptografi Sederhana
# Hafizh Hilman Asyhari
# Indonesia 2025

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Contoh penggunaan
if __name__ == "__main__":
    pesan = "Halo Dunia!"
    shift = 3
    encrypted = caesar_encrypt(pesan, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("Pesan asli   :", pesan)
    print("Terenkripsi  :", encrypted)
    print("Terdekripsi  :", decrypted)
