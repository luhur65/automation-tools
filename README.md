# Bot Otomatisasi Pengecekan Harian

Ini adalah sebuah skrip Python yang menggunakan Playwright untuk melakukan otomatisasi proses pengecekan data (misalnya omset dan piutang) dari sebuah situs web dan menyimpannya ke dalam file Excel (`.xlsx`).

---

## ⚙️ Kebutuhan Sistem

Sebelum memulai, pastikan perangkat Anda telah terpasang:
* **Python** (versi 3.8 atau lebih baru)
* **Git** (untuk mengkloning repositori)

---

## 🚀 Instalasi & Konfigurasi

Ikuti langkah-langkah berikut untuk menyiapkan dan menjalankan proyek ini di komputer Anda.

### 1. Dapatkan Kode Proyek
Buka terminal atau command prompt, lalu kloning repositori ini:
```bash
git clone https://github.com/luhur65/automation-tools.git
cd BOT-CEK-HARIAN
```

### 2. Buat dan Aktifkan Virtual Environment
Sangat disarankan untuk menggunakan virtual environment agar dependensi proyek tidak tercampur dengan proyek lain.

```bash
# Membuat virtual environment
python -m venv .venv
```

Selanjutnya, aktifkan virtual environment tersebut:

* **Untuk Windows:**
    ```cmd
    .\.venv\Scripts\activate
    ```

* **Untuk macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```
Setelah aktif, Anda akan melihat `(.venv)` di awal baris terminal Anda.

### 3. Install Semua Dependensi
Gunakan file `requirements.txt` untuk meng-install semua library Python yang dibutuhkan dengan satu perintah.
```bash
pip install -r requirements.txt
```

### 4. Install Browser untuk Playwright
Playwright membutuhkan browser khusus untuk bisa berjalan. Jalankan perintah berikut untuk mengunduh browser yang diperlukan (seperti Chromium, Firefox, WebKit).
```bash
playwright install
```
Perintah ini hanya perlu dijalankan sekali saat pertama kali melakukan setup.

---

### 5. Konfigurasi Kredensial
Proyek ini memerlukan kredensial (username dan password) untuk login.

1.  Salin file contoh `.env.example` menjadi file baru bernama `.env`.
    * **Untuk Windows (Command Prompt):**
        ```cmd
        copy .env.example .env
        ```
    * **Untuk macOS / Linux:**
        ```bash
        cp .env.example .env
        ```
2.  Buka file `.env` yang baru dibuat dan isi nilai username serta password Anda. File ini sudah otomatis diabaikan oleh Git, jadi informasinya akan tetap aman di komputer lokal Anda.

## ▶️ Cara Menjalankan Skrip

Setelah semua langkah instalasi selesai, Anda bisa langsung menjalankan skrip utama.

1.  Pastikan virtual environment Anda masih **aktif**.
2.  Jalankan skrip Python berikut di terminal:
    ```bash
    python omset_piutang.py
    ```

---

## ✅ Hasil

Setelah skrip berhasil dijalankan, file `cek_harian.xlsx` akan secara otomatis diperbarui dengan data terbaru yang diambil oleh bot.