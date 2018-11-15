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


```python
import pandas as pd
import numpy as np
```


```python
pd.set_option('max_columns', 8, 'max_rows', 10)
```


```python
movie = pd.read_csv('bigdata/pandas-cookbook/data/movie.csv')
movie.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>director_name</th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>...</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Color</td>
      <td>James Cameron</td>
      <td>723.0</td>
      <td>178.0</td>
      <td>...</td>
      <td>936.0</td>
      <td>7.9</td>
      <td>1.78</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Color</td>
      <td>Gore Verbinski</td>
      <td>302.0</td>
      <td>169.0</td>
      <td>...</td>
      <td>5000.0</td>
      <td>7.1</td>
      <td>2.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Color</td>
      <td>Sam Mendes</td>
      <td>602.0</td>
      <td>148.0</td>
      <td>...</td>
      <td>393.0</td>
      <td>6.8</td>
      <td>2.35</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Color</td>
      <td>Christopher Nolan</td>
      <td>813.0</td>
      <td>164.0</td>
      <td>...</td>
      <td>23000.0</td>
      <td>8.5</td>
      <td>2.35</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Doug Walker</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>12.0</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>




```python

```
