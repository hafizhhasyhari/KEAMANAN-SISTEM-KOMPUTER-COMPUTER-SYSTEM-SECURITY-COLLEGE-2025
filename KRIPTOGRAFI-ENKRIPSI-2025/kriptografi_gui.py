# Kriptografi GUI
# Nama : Hafizh Hilman Asyhari
# Kelas : D
# Status : Undergraduate Student
# Mata Kuliah Keamanan Sistem Komputer
# Negara : Indonesia
# Tahun : 2025


import tkinter as tk
from tkinter import ttk, messagebox

# ===== Caesar Cipher Functions =====
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

# ===== Vigenère Cipher Functions =====
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

# ===== GUI Logic =====
def proses_kriptografi():
    metode = metode_var.get()
    operasi = operasi_var.get()
    pesan = entry_pesan.get()
    kunci = entry_kunci.get()

    if not pesan:
        messagebox.showwarning("Input Error", "Pesan tidak boleh kosong!")
        return

    if metode == "Caesar Cipher":
        if not kunci.isdigit():
            messagebox.showerror("Input Error", "Kunci Caesar harus berupa angka.")
            return
        shift = int(kunci)
        hasil = caesar_encrypt(pesan, shift) if operasi == "Enkripsi" else caesar_decrypt(pesan, shift)
    else:
        if not kunci.isalpha():
            messagebox.showerror("Input Error", "Kunci Vigenère harus huruf.")
            return
        hasil = vigenere_encrypt(pesan, kunci) if operasi == "Enkripsi" else vigenere_decrypt(pesan, kunci)

    text_hasil.delete("1.0", tk.END)
    text_hasil.insert(tk.END, hasil)

# ===== GUI Setup =====
root = tk.Tk()
root.title("Aplikasi Pengantar Kriptografi")
root.geometry("500x400")
root.resizable(False, False)

# Frame Input
frame_input = tk.Frame(root)
frame_input.pack(pady=_
