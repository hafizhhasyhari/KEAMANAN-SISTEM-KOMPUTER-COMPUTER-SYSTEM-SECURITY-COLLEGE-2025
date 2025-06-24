# Program Kriptografi GUI 02
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Status : Undergraduate Student
# Mata Kuliah Keamanan Sistem Komputer
# Negara : Indonesia
# Tahun : 2025

import tkinter as tk
from tkinter import ttk, messagebox

# ===== Caesar Cipher =====
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ===== Vigenère Cipher =====
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

def vigenere_decrypt(text, key):
    decrypted = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            k = ord(key[key_index % len(key)]) - 65
            decrypted += chr((ord(char) - offset - k) % 26 + offset)
            key_index += 1
        else:
            decrypted += char
    return decrypted

# ===== Beaufort Cipher =====
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
    return result  # reversible, gunakan fungsi yang sama untuk dekripsi

# ===== Autokey Cipher =====
def autokey_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = (key + plain_text).upper()
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
            key += p_char  # Autokey: plaintext jadi bagian key
        else:
            result += cipher_text[i]
    return result

# ===== GUI Function =====
def proses_kriptografi():
    metode = metode_var.get()
    operasi = operasi_var.get()
    pesan = entry_pesan.get()
    kunci = entry_kunci.get()

    if not pesan:
        messagebox.showwarning("Input Error", "Pesan tidak boleh kosong!")
        return

    hasil = ""
    try:
        if metode == "Caesar Cipher":
            if not kunci.isdigit():
                messagebox.showerror("Kunci Salah", "Kunci Caesar harus berupa angka.")
                return
            shift = int(kunci)
            hasil = caesar_encrypt(pesan, shift) if operasi == "Enkripsi" else caesar_decrypt(pesan, shift)

        elif metode == "Vigenère Cipher":
            if not kunci.isalpha():
                messagebox.showerror("Kunci Salah", "Kunci Vigenère harus huruf.")
                return
            hasil = vigenere_encrypt(pesan, kunci) if operasi == "Enkripsi" else vigenere_decrypt(pesan, kunci)

        elif metode == "Beaufort Cipher":
            if not kunci.isalpha():
                messagebox.showerror("Kunci Salah", "Kunci Beaufort harus huruf.")
                return
            hasil = beaufort_cipher(pesan, kunci)

        elif metode == "Autokey Cipher":
            if not kunci.isalpha():
                messagebox.showerror("Kunci Salah", "Kunci Autokey harus huruf.")
                return
            hasil = autokey_encrypt(pesan, kunci) if operasi == "Enkripsi" else autokey_decrypt(pesan, kunci)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    text_hasil.delete("1.0", tk.END)
    text_hasil.insert(tk.END, hasil)

# ===== GUI Setup =====
root = tk.Tk()
root.title("Aplikasi Pengantar Kriptografi")
root.geometry("520x420")
root.resizable(False, False)

# Frame Input
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Pilihan Metode
metode_var = tk.StringVar(value="Caesar Cipher")
ttk.Label(frame_input, text="Metode:").grid(row=0, column=0, sticky="w")
ttk.Combobox(frame_input, textvariable=metode_var, width=25, values=[
    "Caesar Cipher",
    "Vigenère Cipher",
    "Beaufort Cipher",
    "Autokey Cipher"
]).grid(row=0, column=1)

# Pilihan Operasi
operasi_var = tk.StringVar(value="Enkripsi")
ttk.Label(frame_input, text="Operasi:").grid(row=1, column=0, sticky="w")
ttk.Combobox(frame_input, textvariable=operasi_var, width=25, values=["Enkripsi", "Dekripsi"]).grid(row=1, column=1)

# Entry Pesan
ttk.Label(frame_input, text="Pesan:").grid(row=2, column=0, sticky="w")
entry_pesan = ttk.Entry(frame_input, width=40)
entry_pesan.grid(row=2, column=1)

# Entry Kunci
ttk.Label(frame_input, text="Kunci:").grid(row=3, column=0, sticky="w")
entry_kunci = ttk.Entry(frame_input, width=40)
entry_kunci.grid(row=3, column=1)

# Tombol Proses
ttk.Button(root, text="Proses", command=proses_kriptografi).pack(pady=10)

# Hasil
ttk.Label(root, text="Hasil:").pack()
text_hasil = tk.Text(root, height=5, width=60)
text_hasil.pack()

# Jalankan Aplikasi
root.mainloop()
