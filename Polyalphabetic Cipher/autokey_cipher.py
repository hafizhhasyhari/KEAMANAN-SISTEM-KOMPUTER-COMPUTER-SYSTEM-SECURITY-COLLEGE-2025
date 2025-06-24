# Autokey Chiper
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Status : Undergraduate Student
# Mata Kuliah Keamanan Sistem Komputer
# Negara : Indonesia
# Tahun : 2025

def autokey_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper() + plain_text  # autokey: key ditambah plain
    result = ""
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            p = ord(plain_text[i]) - 65
            k = ord(key[i]) - 65
            c = (p + k) % 26
            result += chr(c + 65)
        else:
            result += plain_text[i]
    return result

def autokey_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    result = ""
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            c = ord(cipher_text[i]) - 65
            k = ord(key[i]) - 65
            p = (c - k + 26) % 26
            p_char = chr(p + 65)
            result += p_char
            key += p_char  # autokey menambah plaintext ke key
        else:
            result += cipher_text[i]
    return result

# Contoh penggunaan
if __name__ == "__main__":
    pesan = "RAHASIA NEGARA"
    kunci = "KUNCI"
    cipher = autokey_encrypt(pesan, kunci)
    print("Cipher:", cipher)
    print("Decrypt:", autokey_decrypt(cipher, kunci))
