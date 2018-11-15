# [Jupyter Notebook Quickstart](https://jupyter.readthedocs.io/en/latest/content-quickstart.html)
### Try Jupyter
#### Pada bagian ini kita dapat mencoba Jupyter tanpa installasi dengan mengunjungi link [https://jupyter.org/try](https://jupyter.org/try)
### Installing Jupyter Notebook
#### Untuk installasi Jupyter notebook telah saya bahas pada bagian [teori](https://github.com/rodesta2212/bigdata/tree/master/minggu-09/teori)
### Optional: Installing Kernels
#### Bagian ini membahas installasi kernels namun tidak wajib, kita dapat mengistall python 2 dan python 3 dan dapat pula mengistall bahasa pemrograman tambahan seperti R dan Julia
### Running the Notebook
#### Menjalankan Jupyter Notebook dengan perintah :
```bash
jupyter notebook
```
#### kemudian akan mengaktifkan server, dimana jupyter dapat di akses melalui localhost browser.
### Migrating from IPython Notebook
#### Bagian ini akan membahas tentang [The Big Split](https://blog.jupyter.org/the-big-split-9d7b88a031a7) memindahkan berbagai komponen bahasa-agnostik IPython di bawah payung Jupyter. Ke depan, Jupyter akan memuat proyek-proyek bahasa-agnostik yang melayani banyak bahasa. IPython akan terus fokus pada Python dan penggunaannya dengan Jupyter.

#### Dokumen ini menjelaskan apa yang telah berubah, dan bagaimana Anda mungkin perlu memodifikasi kode atau konfigurasi Anda ketika bermigrasi dari IPython versi 3 ke Jupyter.

# Chapter 1 - Pandas Foundation pada buku Pandas Cookbook
#### download data yang akan digunakan pada [Pandas-Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)
#### data yang saya dowload saya letakkan pada "pandas-cookbook/data"
```bash
import pandas as pd
import numpy as np
```
### Dissecting the anatomy of a DataFrame
```bash
pd.set_option('max_columns', 8, 'max_rows', 10)
```
```bash
movie = pd.read_csv('bigdata/pandas-cookbook/data/movie.csv')
movie.head()
```
#### output
[gambar tabel](https://github.com/rodesta2212/bigdata/praktik09/src/outpu1.png)