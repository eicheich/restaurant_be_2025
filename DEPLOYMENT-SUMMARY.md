# Persiapan Deployment untuk cPanel

## File yang Diperbarui:

1. `passenger_wsgi.py` - File utama yang digunakan cPanel untuk menjalankan aplikasi FastAPI
2. `models/__init__.py` - Konfigurasi database yang mendukung lingkungan development dan production
3. `.htaccess` - Konfigurasi Apache untuk routing dan keamanan
4. `requirements.txt` - Dependensi yang dibutuhkan untuk aplikasi
5. `db-migrations/alembic.ini` - URL koneksi database untuk migrasi

## File Baru yang Dibuat:

1. `.cpanel.yml` - File konfigurasi untuk deployment otomatis di cPanel
2. `DEPLOYMENT-GUIDE.md` - Panduan lengkap untuk deployment di cPanel
3. `test_db_connection.py` - Script pengujian koneksi database
4. `passenger_wsgi_debug.py` - Script diagnosa untuk passenger_wsgi
5. `run_seeder.py` - Script untuk menjalankan seeder database
6. `wsgi.py` - Wrapper WSGI standar (untuk Apache atau Gunicorn)
7. `Procfile` - Konfigurasi untuk deployment alternatif (jika diperlukan)
8. `sample_response.json` - Contoh response API untuk testing

## Langkah Selanjutnya:

1. Upload semua file ke direktori cPanel
2. Buat database MySQL di cPanel
3. Buat Python application via cPanel interface
4. Install dependencies via pip
5. Jalankan migrasi database
6. Restart aplikasi Python

Perhatikan untuk mengganti informasi kredensial database di `models/__init__.py` dan path Python di `passenger_wsgi.py` sesuai dengan environment cPanel Anda.
