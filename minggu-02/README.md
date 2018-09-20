# Hasil PRAKTIK BIG DATA PERTEMUAN 2
### Pada https://docs.python.org/3/tutorial/index.html

## BAB 2
#### Pada bagian ini dijelaskan cara untuk menjalankan python 3.7.0 dengan perintah seperti dibawah ini :
```bash
python3.7
```
#### Jika python dapat berjalan maka hasilnya seperti dibawah ini :
```bash
Python 3.7.0 (default, Sep  6 2018, 15:36:24) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
### Kesimpulan
#### Pada bab ini dapat di simpulkan tatacara menjalankan python dan pengecekan apakah python dapat berjalan di komputer anda.

## BAB 3
#### Pada bagian ini merupakan perkenalan awal python, dimana python dapat digunakan untuk mengolah angka dan kata. Dapat dilihat pada contoh berikut :
#### Contoh pengolahan angka
```bash
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```
#### Contoh pengolahan angka menggunkan tipe" data
```bash
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
```
#### Contoh pengolahan angka menggunakan operator
```bash
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```
#### Contoh pengolahan angka menggunakan variabel
```bash
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
#### Contoh pengolahan kata
```bash
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
```

#### Contoh pengolahan List
```bash
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

```bash
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```
#### Python digunakan untuk proggamming
#### Contoh awal sederhana
```bash
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
````

### Kesimpulan
#### Pada bab ini di jelaskan bahwa python dapat digunakan untuk kalkulator dalam pengolahan (Numbers, Strings, Lists) dan python dapat digunakan juga untuk proggramming

