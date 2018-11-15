## Cara Install Miniconda di Linux Ubuntu 18.04

### 1. Download package miniconda sesuai dengan kebutuhan melalui alamat [https://conda.io/miniconda.html](https://conda.io/miniconda.html)
### 2. Buka Terminal, kemudian masuk ke dalam folder Downloads dengan menggunakan perintah *cd Downloads/*
### 3. Ubahlah hak akses package miniconda dengan menggunakan perintah *chmod +x Miniconda3-latest-Linux-x86_64.sh*
### 4. Kemudian Installisasi menggunakan perintah *./Miniconda3-latest-Linux-x86_64.sh*
### 5. Ikuti petunjuk penginstalan dan pengaturan.
### 6. Berikan persetujuan pada proses installasi dan pengaturan.
### 7. Tunggu proses installasi sampai selesai.
### 8. Untuk pengecekan gunakan perintah *conda List*. Jika terdapat enviroment conda berarti installasi sukses.  

## Cara Install Apache Airflow

### 1. Setelah miniconda berhasil di install, kemudian masukkan perintah :
```bash
pip install apache-airflow
```
### 2. Ikuti proses instruksi installasi dan tunggu proses installasi selesai
### 3. Jika terjadi error pada unidecode coba pastikan script dibawah ini telah ada di sistem :
```bash
export SLUGIFY_USES_TEXT_UNIDECODE=yes
```

## Tutorial Apache Airflow
