## Teori 10 Intro To Data Structures

#### 1. Perilaku mendasar tentang tipe data
#### 2. Pengindeksan
#### 3. Pelebelan

### Import NumPy pada Jupyter notebook :
```bash
In : import numpy as np
In : import pandas as pd
```

#### Prinsip dasar : penyelarasan data bersifat intrinsik yang artinya tautan antara lebel dan data tindak akan rusak kecuali dilakukan secara eksplisit oleh anda.

### Series, merupakan larik berlebel satu dimensi yang mampu menyimpan tipe data apa pun.
#### contoh : >>> s = pd.Series(data, index=index)
#### ket : 
#### 1. data = banyak hal (Python, ndarray, nilai skalar)
#### 2. indek = daftar lebel sumbu

### Serial seperti ndarray, merupakan argumen yang valid untuk sebagian besar fungsi NumPy
#### contoh :
```bash
In : s[0]
Out : 0.46911229990718628
```
