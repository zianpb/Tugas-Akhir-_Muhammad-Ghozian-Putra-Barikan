<div align="center">

# 🥗 MoodMeal
**Smart Food Recommendation System Based on Mood, Budget & Nutrition**

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge&logo=gui&logoColor=white)
![Logic](https://img.shields.io/badge/Algorithm-Triple%20Filtering-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Final_Project-success?style=for-the-badge)

<p align="center">
  <img src="https://via.placeholder.com/600x400.png?text=Preview+Dashboard+MoodMeal" alt="MoodMeal Dashboard" width="600">
  <br>
  <i>(Aplikasi MoodMeal: Solusi Makan Sehat, Hemat, dan Sesuai Perasaan)</i>
</p>

</div>

---

## 📌 Deskripsi

**MoodMeal** adalah aplikasi asisten kesehatan digital berbasis desktop yang dirancang untuk mengatasi masalah *"Decision Fatigue"* (kebingungan memilih makanan) yang sering dialami mahasiswa.

Aplikasi ini bukan sekadar daftar menu, melainkan sebuah **Sistem Pendukung Keputusan (Decision Support System)** sederhana. MoodMeal menggunakan algoritma cerdas yang menggabungkan tiga parameter sekaligus untuk memberikan rekomendasi:
1.  **Biologis:** Kebutuhan nutrisi tubuh (*Cutting/Bulking*) berdasarkan rumus BMR.
2.  **Ekonomis:** Ketersediaan dana (*Budget*).
3.  **Psikologis:** Kondisi emosional (*Mood*) saat ini.

Project ini disusun sebagai **Tugas Akhir Praktikum Pemrograman Dasar**, dengan penerapan **Modul 1–8** secara komprehensif.

---

## ✨ Fitur Unggulan

🧠 **Smart Fitness Logic**
Menghitung BMR & TDEE (Total Daily Energy Expenditure) menggunakan rumus *Mifflin-St Jeor*. Sistem otomatis menyarankan strategi diet (misal: "Kurangi Karbo" untuk Cutting).

🔍 **Triple Layer Filtering**
Algoritma penyaringan bertingkat. Makanan hanya akan muncul jika:
* Nutrisinya cocok dengan Goal.
* Harganya masuk Budget.
* Kategorinya sesuai Mood.

⚡ **Real-time Nutrition Tracker**
Memantau asupan kalori harian. Status bar akan berubah warna menjadi **MERAH (Overlimit)** jika kalori melebihi batas harian.

↩️ **Undo & Redo System**
Salah pencet tombol makan? Tenang, fitur ini menggunakan struktur data **Stack** (LIFO) untuk membatalkan atau mengulang aksi makan.

➕ **Dynamic Menu Management**
Pengguna dapat menambahkan menu baru secara *runtime*. Sistem otomatis menganalisa nutrisi menu baru tersebut dan memberikan label kategori (Cutting/Bulking) tanpa input manual.

---

## 🛠️ Teknologi & Konsep

Project ini dibangun menggunakan teknologi dan paradigma berikut:

| Komponen | Detail |
| :--- | :--- |
| **Bahasa** | Python 3.12+ |
| **GUI Framework** | Tkinter (Standard Library) |
| **Algoritma** | Multi-condition Filtering |
| **Struktur Data** | List (Database), Stack (Undo/Redo) |
| **Paradigma** | Object-Oriented Programming (OOP) |

### 📚 Implementasi Modul Praktikum
Program ini mencakup penerapan modul:
- [x] **Modul 1:** Variabel & Tipe Data (Integer, String, List)
- [x] **Modul 2:** Pengkondisian (Logika Filter & Overlimit)
- [x] **Modul 3:** Perulangan (Scanning Database & Widget Loop)
- [x] **Modul 4:** Fungsi & Method Modular
- [x] **Modul 5:** Class & Object (OOP: Class Makanan & UserTracker)
- [x] **Modul 6:** Struktur Data Stack (Undo/Redo)
- [x] **Modul 8:** GUI Programming dengan Tkinter

---
