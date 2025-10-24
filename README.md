# Bot Otomatisasi Pengecekan Harian

Ini adalah beberapa skrip Python yang menggunakan Playwright untuk melakukan otomatisasi proses pengecekan data (misalnya omset, piutang, dan log pengiriman email reminder) dari sebuah situs web dan menyimpannya ke dalam file Excel (`.xlsx`).

---

## ⚙️ Kebutuhan Sistem

Sebelum memulai, pastikan perangkat Anda telah terpasang:

- **Python** (versi 3.8 atau lebih baru)
- **Git** (untuk mengkloning repositori)

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

- **Untuk Windows:**

  ```cmd
  .\.venv\Scripts\activate
  ```

- **Untuk macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Setelah aktif, Anda akan melihat `(.venv)` di awal baris terminal Anda.

### 3. Install Semua Dependensi

Gunakan file `requirements.txt` untuk meng-install semua library Python yang dibutuhkan dengan satu perintah.

```bash
pip install -r requirements.txt
```

Jika Anda menambahkan paket baru (mis. `openpyxl`, `python-dotenv`), pastikan `requirements.txt` sudah ter-update. Paket penting yang digunakan di repo ini antara lain:

- playwright
- openpyxl
- python-dotenv

### 4. Install Browser untuk Playwright

Playwright membutuhkan browser khusus untuk bisa berjalan. Jalankan perintah berikut untuk mengunduh browser yang diperlukan (seperti Chromium, Firefox, WebKit).

```bash
playwright install
```

Perintah ini hanya perlu dijalankan sekali saat pertama kali melakukan setup.

---

### 5. Konfigurasi Kredensial / Variabel Lingkungan

Proyek ini menggunakan file `.env` untuk menyimpan kredensial dan URL cabang. Contoh variabel yang dipakai (lihat juga file `.env` yang ada di repo):

- `TRUCKING_USERNAME` — username untuk sistem trucking
- `TRUCKING_PASSWORD` — password untuk sistem trucking
- `URL_MEDAN`, `URL_JAKT`, `URL_SBY`, `URL_MKS` — base URL untuk tiap cabang

Salin file contoh `.env.example` menjadi file baru bernama `.env` lalu isi nilai yang sesuai.

Contoh (Windows Command Prompt):

```cmd
copy .env.example .env
```

atau (macOS / Linux):

```bash
cp .env.example .env
```

---

## ▶️ Skrip yang Tersedia & Cara Menjalankan

Repository ini sekarang berisi beberapa skrip utama:

- `omset_piutang.py` — (existing) mengambil data omset dan piutang dan menyimpan ke `cek_harian.xlsx`.
- `logemailreminder.py` — (baru) memeriksa log pengiriman email reminder di beberapa cabang dan menyimpan hasil ke `cek_log_email_reminder.xlsx`.

Cara menjalankan (pastikan virtualenv aktif):

- Menjalankan pemeriksaan omset/piutang:

```bash
python omset_piutang.py
```

- Menjalankan pemeriksaan log email reminder:

```bash
python logemailreminder.py
```

Catatan: kedua skrip menggunakan Playwright untuk mengotomasi browser. Pastikan `playwright install` telah dijalankan dan variabel `.env` sudah diisi.

---

## ✅ Output / Hasil

- `cek_harian.xlsx` — output dari `omset_piutang.py` (data omset/piutang).
- `cek_log_email_reminder.xlsx` — output dari `logemailreminder.py` (waktu pengiriman email reminder per cabang; sheet baru dibuat per tanggal).

## Tips & Troubleshooting

- Jika Playwright gagal membuka browser di environment server/headless, coba jalankan dengan `headless=False` (untuk debugging) di file skrip.
- Jika terjadi error terkait variabel `.env`, cek kembali nama variabel (harus sama dengan yang dipakai di skrip): `TRUCKING_USERNAME`, `TRUCKING_PASSWORD`, `URL_MEDAN`, `URL_JAKT`, `URL_SBY`, `URL_MKS`.
- Untuk menambah cabang baru, tambahkan entry URL di `.env` dan update dictionary `BASE_URLS` pada `logemailreminder.py`.

---

Jika Anda ingin, saya bisa juga memperbarui `requirements.txt` agar mencantumkan paket tambahan yang dipakai oleh `logemailreminder.py` (mis. `openpyxl`, `python-dotenv`) dan menambahkan contoh `.env.example` jika belum tersedia.
