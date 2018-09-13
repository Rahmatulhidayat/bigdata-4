Install Python 3.7 di ubuntu 18.04

Langkah 1 - Prasyarat
Gunakan perintah berikut untuk menginstal prasyarat untuk Python sebelum menginstalnya.

$ sudo apt-get install build-essential checkinstall
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Langkah 2 - Unduh Python 3.7
Unduh Python menggunakan perintah berikut dari situs resmi python. Anda juga dapat mengunduh versi terbaru di tempat yang ditentukan di bawah ini.

$ cd /usr/src
$ wget wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

Sekarang ekstrak paket yang diunduh.

$ sudo tar xzf Python-3.7.0.tgz

Langkah 3 - Kumpulkan Python Source
Gunakan set perintah di bawah ini untuk mengkompilasi kode sumber python pada sistem Anda menggunakan altinstall.

$ cd Python-3.7.0
$ sudo ./configure --enable-optimizations
$ sudo make altinstall

membuat altinstall digunakan untuk mencegah mengganti file biner python default / usr / bin / python.

Langkah 4 - Periksa Versi Python
Periksa versi terbaru menginstal python menggunakan perintah di bawah ini

$ python3.7 -V

sumber : https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
diakses pada 06 September 2018
