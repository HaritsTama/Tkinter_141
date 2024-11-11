import tkinter as tk

def hasil_prediksi():
    # Menampilkan hasil prediksi
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat input untuk nilai mata pelajaran
input_labels = []
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:")
    label.grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    input_labels.append(entry)

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()