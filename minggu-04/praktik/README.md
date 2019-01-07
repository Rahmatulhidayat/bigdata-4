# Hasil PRAKTIK BIG DATA PERTEMUAN 4
### Pada https://docs.python.org/3/tutorial/index.html

## BAB 6 - Modul
#### modul fibo
```bash
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
#### latihan modul
```bash
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'

>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1 More on Modules
```bash
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1.1. Executing modules as scripts
## Bab 6.1.1
```bash
$ python3.7 fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
## Bab 6.1.2

## Bab 6.1.3

## Bab 6.2

*Python mempunyai kumpulan pustaka modul standart dari python. Kumpulan modul tersebut merupakan salah satu alternatif konfigurasi yang juga bergantung pada platform yang mendasarinya. Contoh*
```bash
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C>
```
*Dari contoh diatas merupakan salah satu modul yang digunakan untuk mengganti intepreter default dari python. Variabel sys.pathadalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkunganPYTHONPATH, atau dari bawaan bawaan jika PYTHONPATH tidak diatur. Anda dapat memodifikasinya menggunakan operasi daftar standar seperti contoh berikut*
```bash
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## Bab 6.3
```bash
>>> import fibo, sys
>>> dir(fibo)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook','dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
```

## Bab 6.4
```bash 
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

```bash
import sound.effects.echo
```
*alternatif yang lain untuk import submodul dengan contoh dibawah ini*
```bash
from sound.effects import echo
```

## Bab 6.4.1
```bash
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

## BAB 7 - Input dan Output

```bash
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

```bash
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

```bash
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>>
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
...
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>>
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
...
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"x
```

## Bab 7.1.1

```bash
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>>
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

```bash
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
## Bab 7.1.2

```bash
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

```bash
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

```bash
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

```bash
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
The story of Bill, Manfred, and Georg.
```

```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>>
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

```bash
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
```bash
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
## Bab 7.1.3
```bash
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```
## Bab 7.1.4
```bash
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
## Bab 7.2
```bash
>>> f = open('workfile', 'w')
```
```bash
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
```
```bash
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
*f.readline()membaca satu baris dari file; karakter baris baru ( \n) dibiarkan di ujung string, dan hanya dihilangkan pada baris terakhir file jika file tidak berakhir di baris baru.Contoh*
```bash
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
```bash
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
## Bab 7.2.2
```bash
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
```
## BAB 8 - Kesalahan dan Pengecualian
## Bab 8.1

```bash
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
## Bab 8.2

```bash
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
## Bab 8.3

```bash
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
Please enter a number: l
Oops!  That was no valid number.  Try again...
``` 
## Bab 8.4

```bash
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
## Bab 8.5

```bash
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```
## Bab 8.6

```bash
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
>>> KeyboardInterrupt
<class 'KeyboardInterrupt'>
```
## Bab 8.7
```bash
for line in open("myfile.txt"):
    print(line, end="")
```

## BAB 9 - Kelas (belum)

##### [source code](https://github.com/rodesta2212/bigdata/tree/master/minggu-04/praktik/src)
