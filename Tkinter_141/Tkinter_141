import tkinter as tk # Import tkinter dan di kasih alias tk
from tkinter import messagebox # Import messagebox dari tkinter

def hasil_prediksi() : # Membuat fungsi bernama hasil_prediksi untuk mengolah hasil prediksi berdasarkan input nilai mata pelajaran
    try : # Try untuk mengetes kalau ada error
        for entry in entries : # Loop untuk memeriksa setiap nilai yang diinput oleh pengguna
            nilai = int(entry.get()) # Mengambil nilai dari entry dan mengubahnya menjadi integer
            if not (0 <= nilai <= 100) : # Memeriksa apakah nilai berada di rentang 0 hingga 100
                raise ValueError("Nilai Harus antara 0 dan 100") # Jika tidak, tampilkan "Nilai Harus antara 0 dan 100"
        hasil_label.config(text="Prediksi Prodi : Teknologi Informasi")  # Jika semua input valid, tampilkan teks prediksi
    except ValueError as ve : # Menampilkan pesan kesalahan jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan Semua input adalah 0 - 100")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") # Judul jendela aplikasi
root.geometry("700x800") # Ukuran jendela aplikasi
root.configure(bg="#f0f0f0") # Warna latar belakang aplikasi

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0") #Spesifikasi Judul
judul_label.pack(pady=30) # Letakkan label judul dengan padding vertikal 20 piksel

# Frame untuk menampung input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# Daftar untuk menyimpan objek entry input nilai mata pelajaran
entries = []
for i in range(10) : # Loop untuk 10 kali

    # Label untuk masing-masing mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    # Entry untuk input nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry) # Tambahkan entry ke dalam daftar entries


# Tombol untuk menjalankan fungsi hasil_prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#f0f0f0")
prediksi_button.pack(padx=30)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)

root.mainloop()# Menjalankan loop utama aplikasi