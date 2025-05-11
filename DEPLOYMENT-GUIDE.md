# Panduan Deployment di cPanel

Panduan ini akan membantu Anda men-deploy aplikasi FastAPI Restaurant API di shared hosting cPanel.

## Langkah-langkah Deployment

### 1. Upload Project ke cPanel

1. Login ke cPanel
2. Buka File Manager
3. Buat folder baru, misal: `restaurant_be_2025`
4. Upload semua file project ke folder tersebut menggunakan:
   - File Manager (Upload), atau
   - FTP client seperti FileZilla, atau
   - Git deployment jika tersedia

### 2. Setup Python Application di cPanel

1. Di dashboard cPanel, cari dan klik "Setup Python App"
2. Klik "Create Application"
3. Isi formulir dengan informasi berikut:
   - Python version: 3.10 (atau versi yang tersedia)
   - Application root: /restaurant_be_2025 (sesuai lokasi upload)
   - Application URL: domain.com atau subdomain.domain.com
   - Application startup file: passenger_wsgi.py
   - Application Entry point: application
   - Restart applikasi setelah deployment

### 3. Setup Database di cPanel

1. Di dashboard cPanel, cari dan klik "MySQL Databases"
2. Buat database baru, misal: `houselab_restaurant_be_2025`
3. Buat user database baru, misal: `houselab_restaurant`
4. Tambahkan user ke database dan berikan semua hak akses

### 4. Install Dependencies

Setelah aplikasi dibuat, jalankan perintah berikut di terminal cPanel:

```bash
cd ~/restaurant_be_2025
pip3 install --user -r requirements.txt
```

### 5. Jalankan Migrasi Database

Jalankan migrasi Alembic untuk membuat tabel:

```bash
cd ~/restaurant_be_2025/db-migrations
python -m alembic upgrade head
```

### 6. Pengaturan File .htaccess

Pastikan file .htaccess sudah benar. File ini digunakan untuk me-redirect semua permintaan ke passenger_wsgi.py:

```
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /passenger_wsgi.py/$1 [QSA,L]
```

### 7. Restart Aplikasi Python

Setelah semua setup selesai, restart aplikasi Python dari panel "Setup Python App" di cPanel.

### 8. Testing Koneksi Database

Jika Anda mengalami masalah koneksi database, jalankan script berikut untuk diagnostik:

```bash
cd ~/restaurant_be_2025
python test_db_connection.py
```

## Catatan Penting

1. Pastikan versi Python di cPanel kompatibel dengan aplikasi Anda
2. Perbarui kredensial database di `models/__init__.py` sesuai dengan informasi cPanel
3. Perbarui path Python di `passenger_wsgi.py` sesuai dengan path di server cPanel
4. Untuk produksi, ubah `allow_origins=["*"]` di `main.py` menjadi domain spesifik
5. Jika mengalami masalah, periksa log error di cPanel untuk informasi lebih lanjut

## Troubleshooting

1. **Error "Module not found"**: Pastikan semua dependencies terinstall
2. **Error koneksi database**: Periksa kredensial database dan pastikan user memiliki akses ke database
3. **Error 500**: Periksa log error di cPanel untuk informasi lebih detail
