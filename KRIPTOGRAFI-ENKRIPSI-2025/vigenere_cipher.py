# Vigenère Cipher - Kriptografi dengan Kata Kunci
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Mata Kuliah : Keamanan Sistem Komputer 
# Negara : Indonesia
# Tahun : 2025

def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(key[key_index % len(key)]) - 65
            encrypted += chr((ord(char) - offset + k) % 26 + offset)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(key[key_index % len(key)]) - 65
            decrypted += chr((ord(char) - offset - k) % 26 + offset)
            key_index += 1
        else:
            decrypted += char
    return decrypted

# Contoh penggunaan
if __name__ == "__main__":
    pesan = "Halo Dunia!"
    kunci = "RAHASIA"
    terenkripsi = vigenere_encrypt(pesan, kunci)
    terdekripsi = vigenere_decrypt(terenkripsi, kunci)

    print("Pesan asli   :", pesan)
    print("Terenkripsi  :", terenkripsi)
    print("Terdekripsi  :", terdekripsi)
