# Hasil PRAKTIK BIG DATA PERTEMUAN 3
### Pada https://docs.python.org/3/tutorial/index.html

## BAB 5 - Struktur data
#### 5.1 More on Lists :
* list.append(x)
* list.extend(iterable)
* list.insert(i, x)
* list.remove(x)
* list.pop([i])
* list.clear()
* list.index(x[, start[, end]])
* list.count(x)
* list.sort(key=None, reverse=False)
* list.reverse()
* list.copy()
#### Contoh penggunaan
```bash
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```
#### 5.1.1 Using Lists as Stacks
```bash
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
#### 5.1.2 Using Lists as Queues
```bash
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

##### [source code](https://github.com/rodesta2212/bigdata/tree/master/minggu-03/praktik/src)
