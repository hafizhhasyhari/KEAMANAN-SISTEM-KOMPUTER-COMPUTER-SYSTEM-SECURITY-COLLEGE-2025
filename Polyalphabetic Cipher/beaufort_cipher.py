# Beaufort Chiper
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Status : Undergraduate Student
# Mata Kuliah Keamanan Sistem Komputer
# Negara : Indonesia
# Tahun : 2025

def beaufort_cipher(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            t = ord(char) - 65
            k = ord(key[key_index % len(key)]) - 65
            c = (k - t + 26) % 26
            result += chr(c + 65)
            key_index += 1
        else:
            result += char
    return result

# Contoh penggunaan
if __name__ == "__main__":
    pesan = "INFORMASI RAHASIA"
    kunci = "KEY"
    hasil = beaufort_cipher(pesan, kunci)
    print("Pesan:", pesan)
    print("Cipher:", hasil)
    print("Decrypt (Beaufort bersifat reversible):", beaufort_cipher(hasil, kunci))
