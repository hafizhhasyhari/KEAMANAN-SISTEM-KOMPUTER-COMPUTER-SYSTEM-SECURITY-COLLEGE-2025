# Kriptografi GUI
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Status : Undergraduate Student
# Mata Kuliah Keamanan Sistem Komputer
# Negara : Indonesia
# Tahun : 2025

elif metode == "Beaufort Cipher":
    hasil = beaufort_cipher(pesan, kunci)
elif metode == "Autokey Cipher":
    if operasi == "Enkripsi":
        hasil = autokey_encrypt(pesan, kunci)
    else:
        hasil = autokey_decrypt(pesan, kunci)
