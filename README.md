# 🛡️ Proxy Checker

**Proxy Checker** adalah tool Python ringan untuk memverifikasi daftar proxy (HTTP/HTTPS) secara cepat dan efisien. Tool ini membaca daftar dari file `proxies.txt`, menguji koneksi ke sebuah URL, dan menyimpan proxy yang berfungsi ke `results.txt`.

---

## 📦 Instalasi

Pastikan kamu sudah menginstal [`uv`](https://github.com/astral-sh/uv), alternatif `pip` dan `venv` yang lebih cepat.

```bash
git clone https://github.com/fdjrr/proxy-checker.git
cd proxy-checker
uv pip install -r requirements.txt
```

---

## ▶️ Cara Menjalankan

```bash
uv run main.py
```

---

## 🗂️ Struktur Direktori

```
proxy-checker/
├── main.py              # Script utama untuk cek proxy
├── proxies.txt          # Daftar proxy yang ingin dicek (format ip:port)
├── results.txt  # Proxy yang lolos pengecekan
├── requirements.txt     # Dependensi Python
└── README.md            # Dokumentasi proyek
```

---

## 📝 Format File Proxy

**`proxies.txt`**

Masukkan proxy dengan format satu baris per proxy:

```
103.123.45.67:8080
190.61.88.147:3128
45.77.76.200:8000
```

---

## 📤 Output

Hasil proxy yang valid akan ditulis secara otomatis ke:

**`results.txt`**

---

## 🛠️ Dependensi

- Python 3.8+
- requests
- concurrent.futures (builtin)

Instalasi otomatis saat menjalankan:

```bash
uv pip install -r requirements.txt
```

---

## 📄 Lisensi

MIT License © 2025 [`fdjrr`](https://github.com/fdjrr)
