# Minggu 5
# Bab 10
## Bab 10.1
#### os modul menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi
```bash
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python37'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

```bash
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
*shutil modul ini menyediakan antarmuka tingkat yang lebih tinggi yang lebih mudah digunakan. Contoh*
```bash
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
#### fungsi diatas digunakan untuk hubungan antarmuka dengan sistem operasi

## Bab 10.2
#### glob modul menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard
```bash
>>> import glob
>>> glob.glob('*.py')
['wildcard.py', 'interfaceso.py']
```
## Bab 10.3
#### Skrip utilitas umum sering perlu memproses argumen baris perintah. Argumen-argumen ini disimpan dalam atribut argvsys modul sebagai daftar
```bash
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
## Bab 10.4
#### sys Modul juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan
```bash
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
## Bab 10.5
#### re Modul menyediakan alat ekspresi reguler untuk pengolahan string yang canggih. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan
```bash
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
#### Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena mereka lebih mudah dibaca dan di-debug
```bash
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```
## Bab 10.6
#### math modul memberikan akses ke mendasari C library functions untuk floating point matematika
```bash
>>> import math
>>> math.cos(math.pi / 4)
0.7071067811865476
>>> math.log(1024, 2)
10.0
```
#### random Modul menyediakan alat untuk membuat pilihan acak
```bash
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'banana'
>>> random.sample(range(100), 10)
[79, 12, 29, 73, 42, 82, 52, 89, 72, 21]
>>> random.random()
0.6544689487791325
>>> random.randrange(6)
4
```
#### statisticsModul menghitung sifat dasar statistik (mean, median, varians, dll) dari data numerik
```bash
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
## Bab 10.7
#### Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email
```bash
>>> from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
...     for line in response:
...         line = line.decode('utf-8')  # Decoding the binary data to text.
...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...             print(line)

<BR>Nov. 25, 09:43:32 PM EST

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
## Bab 10.8
#### datetimeModul memasok kelas untuk memanipulasi tanggal dan waktu di kedua cara sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus dari implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi output. Modul ini juga mendukung objek yang sadar zona waktu
```bash
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```
## Bab 10.9
#### Pengarsipan data umum dan kompresi format secara langsung didukung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfiledan tarfile
```bash
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```
## Bab 10.10
#### timeit Modul cepat menunjukkan keunggulan kinerja yang sederhana
```bash
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.062455940002109855
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.027918414998566732
```
## Bab 10.11
#### doctest modul menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini. Uji konstruksi sederhana seperti memotong dan menyisipkan panggilan khas bersama dengan hasilnya ke dalam docstring
```bash
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```
#### unittestModul ini tidak mudah seperti doctestmodul, tetapi memungkinkan satu set yang lebih komprehensif dari tes untuk dipertahankan dalam file terpisah
```bash
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

# Bab 11
## Bab 11.1
#### reprlib modul menyediakan versi repr()disesuaikan untuk menampilkan disingkat kontainer besar atau sangat bersarang
```bash
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```
#### pprintModul menawarkan kontrol yang lebih canggih lebih mencetak baik built-in dan ditetapkan pengguna objek dalam cara yang dapat dibaca oleh interpreter
```bash
>>> import pprint
>>>
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
>>>
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```
#### textwrap format modul paragraf teks agar sesuai dengan lebar layar yang diberikan
```bash
>>> import textwrap
>>>
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
>>>
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
## Bab 11.2
#### string Modul termasuk serbaguna Template kelas dengan sintaks disederhanakan cocok untuk editing oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi
```bash
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```
##### substitute() Metode menimbulkan KeyError ketika pengganti tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya penggabungan surat, data yang disediakan pengguna mungkin tidak lengkap dan safe_substitute()metode ini mungkin lebih tepat - ini akan membuat placeholder tidak berubah jika data hilang
```bash
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
#### Subclass template dapat menetapkan pemisah khusus. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file
```bash
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```
## Bab 11.3
#### struct modul menyediakan pack()dan unpack()fungsi untuk bekerja dengan format rekaman biner variabel panjang
```bash
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```
## Bab 11.4
#### Threading adalah teknik untuk memisahkan tugas yang tidak tergantung secara berurutan. Thread dapat digunakan untuk meningkatkan respon dari aplikasi yang menerima input pengguna sementara tugas lain berjalan di latar belakang
```bash
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```
## Bab 11.5
#### logging Modul menawarkan sistem logging fitur dan fleksibel penuh. Pada yang paling sederhana, pesan log dikirim ke file atau ke sys.stderr
```bash
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
#### output:
```bash
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```
#### Secara default, pesan informasi dan debug ditekan dan output dikirim ke kesalahan standar. Pilihan output lainnya termasuk routing pesan melalui email, datagrams, socket, atau ke HTTP Server. Filter baru dapat memilih routing yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL
## Bab 11.6
#### weakrefModul menyediakan alat untuk objek pelacakan tanpa membuat referensi. Ketika objek tidak lagi diperlukan, secara otomatis dihapus dari tabel lemah dan callback dipicu untuk objek lemah
```bash
>>> import weakref, gc
>>>
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
81
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.7/weakref.py", line 137, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```
## Bab 11.7
#### array Modul menyediakan array()objek yang seperti daftar yang menyimpan data hanya homogen dan menyimpannya lebih kompak.
```bash
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```
#### collections modul menyediakan deque() objek yang seperti daftar dengan menambahkan lebih cepat dan muncul dari sisi kiri namun pencarian lebih lambat di tengah.
```bash
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```
#### bisect modul berfungsi untuk memanipulasi daftar yang diurutkan
```bash
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```
#### heapq modul menyediakan fungsi untuk melaksanakan tumpukan berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol
```bash
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)
>>> heappush(data, -5)
>>> [heappop(data) for i in range(3)]
[-5, 0, 1]
```
## Bab 11.8
#### decimal Modul menawarkan Decimal datatype untuk titik desimal aritmatika floating. Sebagai contoh, menghitung pajak 5% pada biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaannya menjadi signifikan jika hasilnya dibulatkan ke sen terdekat
```bash
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
#### decimal modul menyediakan aritmatika dengan sebanyak presisi yang diperlukan
```bash
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```

