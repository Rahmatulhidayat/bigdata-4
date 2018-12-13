# Chapter 8 - Pandas Foundation pada buku Pandas Cookbook
#### download data yang akan digunakan pada [Pandas-Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)
#### data yang saya dowload saya letakkan pada "/data"

# Pembahasan Praktik :
## Chapter 8
#### Tidying variable values as column names with stack


```python
import pandas as pd
import numpy as np
```


```python
state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
state_fruit
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
      <th>Apple</th>
      <th>Orange</th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Texas</th>
      <td>12</td>
      <td>10</td>
      <td>40</td>
    </tr>
    <tr>
      <th>Arizona</th>
      <td>9</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Florida</th>
      <td>0</td>
      <td>14</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit.stack()
```




    Texas    Apple      12
             Orange     10
             Banana     40
    Arizona  Apple       9
             Orange      7
             Banana     12
    Florida  Apple       0
             Orange     14
             Banana    190
    dtype: int64




```python
state_fruit_tidy = state_fruit.stack().reset_index()
state_fruit_tidy
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
      <th>level_0</th>
      <th>level_1</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit_tidy.columns = ['state', 'fruit', 'weight']
state_fruit_tidy
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
      <th>state</th>
      <th>fruit</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit.stack()\
           .rename_axis(['state', 'fruit'])\
```




    state    fruit 
    Texas    Apple      12
             Orange     10
             Banana     40
    Arizona  Apple       9
             Orange      7
             Banana     12
    Florida  Apple       0
             Orange     14
             Banana    190
    dtype: int64




```python
state_fruit.stack()\
           .rename_axis(['state', 'fruit'])\
           .reset_index(name='weight')
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
      <th>state</th>
      <th>fruit</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2
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
      <th>State</th>
      <th>Apple</th>
      <th>Orange</th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>12</td>
      <td>10</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>9</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>0</td>
      <td>14</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.stack()
```




    0  State       Texas
       Apple          12
       Orange         10
       Banana         40
    1  State     Arizona
       Apple           9
       Orange          7
       Banana         12
    2  State     Florida
       Apple           0
       Orange         14
       Banana        190
    dtype: object




```python
state_fruit2.set_index('State').stack()
```




    State          
    Texas    Apple      12
             Orange     10
             Banana     40
    Arizona  Apple       9
             Orange      7
             Banana     12
    Florida  Apple       0
             Orange     14
             Banana    190
    dtype: int64




```python

```

#### Tidying variable values as column names with melt


```python
import pandas as pd
import numpy as np
```


```python
state_fruit2 = pd.read_csv('data/state_fruit2.csv')
state_fruit2
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
      <th>State</th>
      <th>Apple</th>
      <th>Orange</th>
      <th>Banana</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>12</td>
      <td>10</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>9</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>0</td>
      <td>14</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.melt(id_vars=['State'],
                 value_vars=['Apple', 'Orange', 'Banana'])
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
      <th>State</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.index=list('abc')
state_fruit2.index.name = 'letter'
```


```python
state_fruit2
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
      <th>State</th>
      <th>Apple</th>
      <th>Orange</th>
      <th>Banana</th>
    </tr>
    <tr>
      <th>letter</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>Texas</td>
      <td>12</td>
      <td>10</td>
      <td>40</td>
    </tr>
    <tr>
      <th>b</th>
      <td>Arizona</td>
      <td>9</td>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <th>c</th>
      <td>Florida</td>
      <td>0</td>
      <td>14</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.melt(id_vars=['State'],
                 value_vars=['Apple', 'Orange', 'Banana'],
                 var_name='Fruit',
                 value_name='Weight')
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
      <th>State</th>
      <th>Fruit</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.melt()
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
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>State</td>
      <td>Texas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>State</td>
      <td>Arizona</td>
    </tr>
    <tr>
      <th>2</th>
      <td>State</td>
      <td>Florida</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python
state_fruit2.melt(id_vars='State')
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
      <th>State</th>
      <th>variable</th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Texas</td>
      <td>Apple</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona</td>
      <td>Apple</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florida</td>
      <td>Apple</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Texas</td>
      <td>Orange</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Arizona</td>
      <td>Orange</td>
      <td>7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Florida</td>
      <td>Orange</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Texas</td>
      <td>Banana</td>
      <td>40</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Arizona</td>
      <td>Banana</td>
      <td>12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Florida</td>
      <td>Banana</td>
      <td>190</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### Stacking multiple groups of variables simultaneously


```python
import pandas as pd
import numpy as np
```


```python
movie = pd.read_csv('data/movie.csv')
actor = movie[['movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name', 
               'actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes']]
actor.head()
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
      <th>movie_title</th>
      <th>actor_1_name</th>
      <th>actor_2_name</th>
      <th>actor_3_name</th>
      <th>actor_1_facebook_likes</th>
      <th>actor_2_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>CCH Pounder</td>
      <td>Joel David Moore</td>
      <td>Wes Studi</td>
      <td>1000.0</td>
      <td>936.0</td>
      <td>855.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>Johnny Depp</td>
      <td>Orlando Bloom</td>
      <td>Jack Davenport</td>
      <td>40000.0</td>
      <td>5000.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>Christoph Waltz</td>
      <td>Rory Kinnear</td>
      <td>Stephanie Sigman</td>
      <td>11000.0</td>
      <td>393.0</td>
      <td>161.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>Tom Hardy</td>
      <td>Christian Bale</td>
      <td>Joseph Gordon-Levitt</td>
      <td>27000.0</td>
      <td>23000.0</td>
      <td>23000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>Doug Walker</td>
      <td>Rob Walker</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>12.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
def change_col_name(col_name):
    col_name = col_name.replace('_name', '')
    if 'facebook' in col_name:
        fb_idx = col_name.find('facebook')
        col_name = col_name[:5] + col_name[fb_idx - 1:] + col_name[5:fb_idx-1]
    return col_name
```


```python
actor2 = actor.rename(columns=change_col_name)
actor2.head()
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
      <th>movie_title</th>
      <th>actor_1</th>
      <th>actor_2</th>
      <th>actor_3</th>
      <th>actor_facebook_likes_1</th>
      <th>actor_facebook_likes_2</th>
      <th>actor_facebook_likes_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>CCH Pounder</td>
      <td>Joel David Moore</td>
      <td>Wes Studi</td>
      <td>1000.0</td>
      <td>936.0</td>
      <td>855.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>Johnny Depp</td>
      <td>Orlando Bloom</td>
      <td>Jack Davenport</td>
      <td>40000.0</td>
      <td>5000.0</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>Christoph Waltz</td>
      <td>Rory Kinnear</td>
      <td>Stephanie Sigman</td>
      <td>11000.0</td>
      <td>393.0</td>
      <td>161.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>Tom Hardy</td>
      <td>Christian Bale</td>
      <td>Joseph Gordon-Levitt</td>
      <td>27000.0</td>
      <td>23000.0</td>
      <td>23000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>Doug Walker</td>
      <td>Rob Walker</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>12.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
stubs = ['actor', 'actor_facebook_likes']
actor2_tidy = pd.wide_to_long(actor2, 
                              stubnames=stubs, 
                              i=['movie_title'], 
                              j='actor_num', 
                              sep='_').reset_index()
actor2_tidy.head()
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
      <th>movie_title</th>
      <th>actor_num</th>
      <th>actor</th>
      <th>actor_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>1</td>
      <td>CCH Pounder</td>
      <td>1000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>1</td>
      <td>Johnny Depp</td>
      <td>40000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>1</td>
      <td>Christoph Waltz</td>
      <td>11000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>1</td>
      <td>Tom Hardy</td>
      <td>27000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>1</td>
      <td>Doug Walker</td>
      <td>131.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('data/stackme.csv')
df
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
      <th>State</th>
      <th>Country</th>
      <th>a1</th>
      <th>b2</th>
      <th>Test</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TX</td>
      <td>US</td>
      <td>0.45</td>
      <td>0.3</td>
      <td>Test1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MA</td>
      <td>US</td>
      <td>0.03</td>
      <td>1.2</td>
      <td>Test2</td>
      <td>9</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ON</td>
      <td>CAN</td>
      <td>0.70</td>
      <td>4.2</td>
      <td>Test3</td>
      <td>4</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df.rename(columns = {'a1':'group1_a1', 'b2':'group1_b2',
                           'd':'group2_a1', 'e':'group2_b2'})
df2
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
      <th>State</th>
      <th>Country</th>
      <th>group1_a1</th>
      <th>group1_b2</th>
      <th>Test</th>
      <th>group2_a1</th>
      <th>group2_b2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TX</td>
      <td>US</td>
      <td>0.45</td>
      <td>0.3</td>
      <td>Test1</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MA</td>
      <td>US</td>
      <td>0.03</td>
      <td>1.2</td>
      <td>Test2</td>
      <td>9</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ON</td>
      <td>CAN</td>
      <td>0.70</td>
      <td>4.2</td>
      <td>Test3</td>
      <td>4</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.wide_to_long(df2, 
                stubnames=['group1', 'group2'], 
                i=['State', 'Country', 'Test'], 
                j='Label', 
                suffix='.+', 
                sep='_')
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
      <th></th>
      <th></th>
      <th></th>
      <th>group1</th>
      <th>group2</th>
    </tr>
    <tr>
      <th>State</th>
      <th>Country</th>
      <th>Test</th>
      <th>Label</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">TX</th>
      <th rowspan="2" valign="top">US</th>
      <th rowspan="2" valign="top">Test1</th>
      <th>a1</th>
      <td>0.45</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b2</th>
      <td>0.30</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">MA</th>
      <th rowspan="2" valign="top">US</th>
      <th rowspan="2" valign="top">Test2</th>
      <th>a1</th>
      <td>0.03</td>
      <td>9</td>
    </tr>
    <tr>
      <th>b2</th>
      <td>1.20</td>
      <td>7</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">ON</th>
      <th rowspan="2" valign="top">CAN</th>
      <th rowspan="2" valign="top">Test3</th>
      <th>a1</th>
      <td>0.70</td>
      <td>4</td>
    </tr>
    <tr>
      <th>b2</th>
      <td>4.20</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### Inverting stacked data


```python
import pandas as pd
import numpy as np
```


```python
usecol_func = lambda x: 'UGDS_' in x or x == 'INSTNM'
college = pd.read_csv('data/college.csv', 
                          index_col='INSTNM', 
                          usecols=usecol_func)
college.head()
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_stacked = college.stack()
college_stacked.head(18)
```




    INSTNM                                         
    Alabama A & M University             UGDS_WHITE    0.0333
                                         UGDS_BLACK    0.9353
                                         UGDS_HISP     0.0055
                                         UGDS_ASIAN    0.0019
                                         UGDS_AIAN     0.0024
                                         UGDS_NHPI     0.0019
                                         UGDS_2MOR     0.0000
                                         UGDS_NRA      0.0059
                                         UGDS_UNKN     0.0138
    University of Alabama at Birmingham  UGDS_WHITE    0.5922
                                         UGDS_BLACK    0.2600
                                         UGDS_HISP     0.0283
                                         UGDS_ASIAN    0.0518
                                         UGDS_AIAN     0.0022
                                         UGDS_NHPI     0.0007
                                         UGDS_2MOR     0.0368
                                         UGDS_NRA      0.0179
                                         UGDS_UNKN     0.0100
    dtype: float64




```python
college_stacked.unstack().head()
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college2 = pd.read_csv('data/college.csv', 
                      usecols=usecol_func)
college2.head()
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
      <th>INSTNM</th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama A &amp; M University</td>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>1</th>
      <td>University of Alabama at Birmingham</td>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Amridge University</td>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of Alabama in Huntsville</td>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alabama State University</td>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_melted = college2.melt(id_vars='INSTNM', 
                               var_name='Race',
                               value_name='Percentage')
college_melted.head()
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
      <th>INSTNM</th>
      <th>Race</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama A &amp; M University</td>
      <td>UGDS_WHITE</td>
      <td>0.0333</td>
    </tr>
    <tr>
      <th>1</th>
      <td>University of Alabama at Birmingham</td>
      <td>UGDS_WHITE</td>
      <td>0.5922</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Amridge University</td>
      <td>UGDS_WHITE</td>
      <td>0.2990</td>
    </tr>
    <tr>
      <th>3</th>
      <td>University of Alabama in Huntsville</td>
      <td>UGDS_WHITE</td>
      <td>0.6988</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Alabama State University</td>
      <td>UGDS_WHITE</td>
      <td>0.0158</td>
    </tr>
  </tbody>
</table>
</div>




```python
melted_inv = college_melted.pivot(index='INSTNM',
                                  columns='Race',
                                  values='Percentage')
melted_inv.head()
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
      <th>Race</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>UGDS_WHITE</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A &amp; W Healthcare Educators</th>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.9750</td>
      <td>0.0250</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>A T Still University of Health Sciences</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ABC Beauty Academy</th>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.9333</td>
      <td>0.0333</td>
      <td>0.0333</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>ABC Beauty College Inc</th>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.6579</td>
      <td>0.0526</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2895</td>
    </tr>
    <tr>
      <th>AI Miami International University of Art and Design</th>
      <td>0.0018</td>
      <td>0.0</td>
      <td>0.0018</td>
      <td>0.0198</td>
      <td>0.4773</td>
      <td>0.0</td>
      <td>0.0025</td>
      <td>0.4644</td>
      <td>0.0324</td>
    </tr>
  </tbody>
</table>
</div>




```python
college2_replication = melted_inv.loc[college2['INSTNM'], 
                                      college2.columns[1:]]\
                                         .reset_index()
college2.equals(college2_replication)
```




    True




```python
college.stack().unstack(0)
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
      <th>INSTNM</th>
      <th>Alabama A &amp; M University</th>
      <th>University of Alabama at Birmingham</th>
      <th>Amridge University</th>
      <th>University of Alabama in Huntsville</th>
      <th>Alabama State University</th>
      <th>The University of Alabama</th>
      <th>Central Alabama Community College</th>
      <th>Athens State University</th>
      <th>Auburn University at Montgomery</th>
      <th>Auburn University</th>
      <th>...</th>
      <th>MCI Institute of Technology-Boca Raton</th>
      <th>West Coast University-Miami</th>
      <th>National American University-Houston</th>
      <th>Aparicio-Levy Technical College</th>
      <th>Fred D. Learey Technical College</th>
      <th>Hollywood Institute of Beauty Careers-West Palm Beach</th>
      <th>Hollywood Institute of Beauty Careers-Casselberry</th>
      <th>Coachella Valley Beauty College-Beaumont</th>
      <th>Dewey University-Mayaguez</th>
      <th>Coastal Pines Technical College</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UGDS_WHITE</th>
      <td>0.0333</td>
      <td>0.5922</td>
      <td>0.2990</td>
      <td>0.6988</td>
      <td>0.0158</td>
      <td>0.7825</td>
      <td>0.7255</td>
      <td>0.7823</td>
      <td>0.5328</td>
      <td>0.8507</td>
      <td>...</td>
      <td>0.0199</td>
      <td>0.1522</td>
      <td>0.1858</td>
      <td>0.2431</td>
      <td>0.3731</td>
      <td>0.2182</td>
      <td>0.1200</td>
      <td>0.3284</td>
      <td>0.0</td>
      <td>0.6762</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>0.9353</td>
      <td>0.2600</td>
      <td>0.4192</td>
      <td>0.1255</td>
      <td>0.9208</td>
      <td>0.1119</td>
      <td>0.2613</td>
      <td>0.1200</td>
      <td>0.3376</td>
      <td>0.0704</td>
      <td>...</td>
      <td>0.2815</td>
      <td>0.1739</td>
      <td>0.6443</td>
      <td>0.1215</td>
      <td>0.1388</td>
      <td>0.4182</td>
      <td>0.3333</td>
      <td>0.1045</td>
      <td>0.0</td>
      <td>0.2508</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>0.0055</td>
      <td>0.0283</td>
      <td>0.0069</td>
      <td>0.0382</td>
      <td>0.0121</td>
      <td>0.0348</td>
      <td>0.0044</td>
      <td>0.0191</td>
      <td>0.0074</td>
      <td>0.0248</td>
      <td>...</td>
      <td>0.6854</td>
      <td>0.6087</td>
      <td>0.0672</td>
      <td>0.6243</td>
      <td>0.3080</td>
      <td>0.2364</td>
      <td>0.4400</td>
      <td>0.4925</td>
      <td>1.0</td>
      <td>0.0359</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>0.0019</td>
      <td>0.0518</td>
      <td>0.0034</td>
      <td>0.0376</td>
      <td>0.0019</td>
      <td>0.0106</td>
      <td>0.0025</td>
      <td>0.0053</td>
      <td>0.0221</td>
      <td>0.0227</td>
      <td>...</td>
      <td>0.0132</td>
      <td>0.0217</td>
      <td>0.0079</td>
      <td>0.0055</td>
      <td>0.0000</td>
      <td>0.0182</td>
      <td>0.0000</td>
      <td>0.0149</td>
      <td>0.0</td>
      <td>0.0045</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>0.0024</td>
      <td>0.0022</td>
      <td>0.0000</td>
      <td>0.0143</td>
      <td>0.0010</td>
      <td>0.0038</td>
      <td>0.0044</td>
      <td>0.0157</td>
      <td>0.0044</td>
      <td>0.0074</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0079</td>
      <td>0.0055</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0299</td>
      <td>0.0</td>
      <td>0.0034</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>0.0019</td>
      <td>0.0007</td>
      <td>0.0000</td>
      <td>0.0002</td>
      <td>0.0006</td>
      <td>0.0009</td>
      <td>0.0000</td>
      <td>0.0010</td>
      <td>0.0016</td>
      <td>0.0000</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0149</td>
      <td>0.0</td>
      <td>0.0017</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>0.0000</td>
      <td>0.0368</td>
      <td>0.0000</td>
      <td>0.0172</td>
      <td>0.0098</td>
      <td>0.0261</td>
      <td>0.0000</td>
      <td>0.0174</td>
      <td>0.0297</td>
      <td>0.0000</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0435</td>
      <td>0.0751</td>
      <td>0.0000</td>
      <td>0.0022</td>
      <td>0.0000</td>
      <td>0.0400</td>
      <td>0.0149</td>
      <td>0.0</td>
      <td>0.0191</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>0.0059</td>
      <td>0.0179</td>
      <td>0.0000</td>
      <td>0.0332</td>
      <td>0.0243</td>
      <td>0.0268</td>
      <td>0.0000</td>
      <td>0.0057</td>
      <td>0.0397</td>
      <td>0.0100</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0182</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0028</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>0.0138</td>
      <td>0.0100</td>
      <td>0.2715</td>
      <td>0.0350</td>
      <td>0.0137</td>
      <td>0.0026</td>
      <td>0.0019</td>
      <td>0.0334</td>
      <td>0.0246</td>
      <td>0.0140</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0119</td>
      <td>0.0000</td>
      <td>0.1779</td>
      <td>0.0909</td>
      <td>0.0667</td>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0056</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 6874 columns</p>
</div>




```python
college.T
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
      <th>INSTNM</th>
      <th>Alabama A &amp; M University</th>
      <th>University of Alabama at Birmingham</th>
      <th>Amridge University</th>
      <th>University of Alabama in Huntsville</th>
      <th>Alabama State University</th>
      <th>The University of Alabama</th>
      <th>Central Alabama Community College</th>
      <th>Athens State University</th>
      <th>Auburn University at Montgomery</th>
      <th>Auburn University</th>
      <th>...</th>
      <th>Strayer University-North Dallas</th>
      <th>Strayer University-San Antonio</th>
      <th>Strayer University-Stafford</th>
      <th>WestMed College - Merced</th>
      <th>Vantage College</th>
      <th>SAE Institute of Technology  San Francisco</th>
      <th>Rasmussen College - Overland Park</th>
      <th>National Personal Training Institute of Cleveland</th>
      <th>Bay Area Medical Academy - San Jose Satellite Location</th>
      <th>Excel Learning Center-San Antonio South</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UGDS_WHITE</th>
      <td>0.0333</td>
      <td>0.5922</td>
      <td>0.2990</td>
      <td>0.6988</td>
      <td>0.0158</td>
      <td>0.7825</td>
      <td>0.7255</td>
      <td>0.7823</td>
      <td>0.5328</td>
      <td>0.8507</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>0.9353</td>
      <td>0.2600</td>
      <td>0.4192</td>
      <td>0.1255</td>
      <td>0.9208</td>
      <td>0.1119</td>
      <td>0.2613</td>
      <td>0.1200</td>
      <td>0.3376</td>
      <td>0.0704</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>0.0055</td>
      <td>0.0283</td>
      <td>0.0069</td>
      <td>0.0382</td>
      <td>0.0121</td>
      <td>0.0348</td>
      <td>0.0044</td>
      <td>0.0191</td>
      <td>0.0074</td>
      <td>0.0248</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>0.0019</td>
      <td>0.0518</td>
      <td>0.0034</td>
      <td>0.0376</td>
      <td>0.0019</td>
      <td>0.0106</td>
      <td>0.0025</td>
      <td>0.0053</td>
      <td>0.0221</td>
      <td>0.0227</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>0.0024</td>
      <td>0.0022</td>
      <td>0.0000</td>
      <td>0.0143</td>
      <td>0.0010</td>
      <td>0.0038</td>
      <td>0.0044</td>
      <td>0.0157</td>
      <td>0.0044</td>
      <td>0.0074</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>0.0019</td>
      <td>0.0007</td>
      <td>0.0000</td>
      <td>0.0002</td>
      <td>0.0006</td>
      <td>0.0009</td>
      <td>0.0000</td>
      <td>0.0010</td>
      <td>0.0016</td>
      <td>0.0000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>0.0000</td>
      <td>0.0368</td>
      <td>0.0000</td>
      <td>0.0172</td>
      <td>0.0098</td>
      <td>0.0261</td>
      <td>0.0000</td>
      <td>0.0174</td>
      <td>0.0297</td>
      <td>0.0000</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>0.0059</td>
      <td>0.0179</td>
      <td>0.0000</td>
      <td>0.0332</td>
      <td>0.0243</td>
      <td>0.0268</td>
      <td>0.0000</td>
      <td>0.0057</td>
      <td>0.0397</td>
      <td>0.0100</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>0.0138</td>
      <td>0.0100</td>
      <td>0.2715</td>
      <td>0.0350</td>
      <td>0.0137</td>
      <td>0.0026</td>
      <td>0.0019</td>
      <td>0.0334</td>
      <td>0.0246</td>
      <td>0.0140</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>9 rows × 7535 columns</p>
</div>




```python

```

#### Unstacking after a groupby aggregation


```python
import pandas as pd
import numpy as np
```


```python
employee = pd.read_csv('data/employee.csv')
```


```python
employee.groupby('RACE')['BASE_SALARY'].mean().astype(int)
```




    RACE
    American Indian or Alaskan Native    60272
    Asian/Pacific Islander               61660
    Black or African American            50137
    Hispanic/Latino                      52345
    Others                               51278
    White                                64419
    Name: BASE_SALARY, dtype: int64




```python
agg = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].mean().astype(int)
agg
```




    RACE                               GENDER
    American Indian or Alaskan Native  Female    60238
                                       Male      60305
    Asian/Pacific Islander             Female    63226
                                       Male      61033
    Black or African American          Female    48915
                                       Male      51082
    Hispanic/Latino                    Female    46503
                                       Male      54782
    Others                             Female    63785
                                       Male      38771
    White                              Female    66793
                                       Male      63940
    Name: BASE_SALARY, dtype: int64




```python
agg.unstack('GENDER')
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
      <th>GENDER</th>
      <th>Female</th>
      <th>Male</th>
    </tr>
    <tr>
      <th>RACE</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>American Indian or Alaskan Native</th>
      <td>60238</td>
      <td>60305</td>
    </tr>
    <tr>
      <th>Asian/Pacific Islander</th>
      <td>63226</td>
      <td>61033</td>
    </tr>
    <tr>
      <th>Black or African American</th>
      <td>48915</td>
      <td>51082</td>
    </tr>
    <tr>
      <th>Hispanic/Latino</th>
      <td>46503</td>
      <td>54782</td>
    </tr>
    <tr>
      <th>Others</th>
      <td>63785</td>
      <td>38771</td>
    </tr>
    <tr>
      <th>White</th>
      <td>66793</td>
      <td>63940</td>
    </tr>
  </tbody>
</table>
</div>




```python
agg.unstack('RACE')
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
      <th>RACE</th>
      <th>American Indian or Alaskan Native</th>
      <th>Asian/Pacific Islander</th>
      <th>Black or African American</th>
      <th>Hispanic/Latino</th>
      <th>Others</th>
      <th>White</th>
    </tr>
    <tr>
      <th>GENDER</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>60238</td>
      <td>63226</td>
      <td>48915</td>
      <td>46503</td>
      <td>63785</td>
      <td>66793</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>60305</td>
      <td>61033</td>
      <td>51082</td>
      <td>54782</td>
      <td>38771</td>
      <td>63940</td>
    </tr>
  </tbody>
</table>
</div>




```python
agg2 = employee.groupby(['RACE', 'GENDER'])['BASE_SALARY'].agg(['mean', 'max', 'min']).astype(int)
agg2
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
      <th></th>
      <th>mean</th>
      <th>max</th>
      <th>min</th>
    </tr>
    <tr>
      <th>RACE</th>
      <th>GENDER</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">American Indian or Alaskan Native</th>
      <th>Female</th>
      <td>60238</td>
      <td>98536</td>
      <td>26125</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>60305</td>
      <td>81239</td>
      <td>26125</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Asian/Pacific Islander</th>
      <th>Female</th>
      <td>63226</td>
      <td>130416</td>
      <td>26125</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>61033</td>
      <td>163228</td>
      <td>27914</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Black or African American</th>
      <th>Female</th>
      <td>48915</td>
      <td>150416</td>
      <td>24960</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>51082</td>
      <td>275000</td>
      <td>26125</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Hispanic/Latino</th>
      <th>Female</th>
      <td>46503</td>
      <td>126115</td>
      <td>26125</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>54782</td>
      <td>165216</td>
      <td>26104</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Others</th>
      <th>Female</th>
      <td>63785</td>
      <td>63785</td>
      <td>63785</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>38771</td>
      <td>38771</td>
      <td>38771</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">White</th>
      <th>Female</th>
      <td>66793</td>
      <td>178331</td>
      <td>27955</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>63940</td>
      <td>210588</td>
      <td>26125</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### Replicating pivot_table with a groupby aggregation


```python
import pandas as pd
import numpy as np
```


```python
flights = pd.read_csv('data/flights.csv')
flights.head()
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
      <th>MONTH</th>
      <th>DAY</th>
      <th>WEEKDAY</th>
      <th>AIRLINE</th>
      <th>ORG_AIR</th>
      <th>DEST_AIR</th>
      <th>SCHED_DEP</th>
      <th>DEP_DELAY</th>
      <th>AIR_TIME</th>
      <th>DIST</th>
      <th>SCHED_ARR</th>
      <th>ARR_DELAY</th>
      <th>DIVERTED</th>
      <th>CANCELLED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>WN</td>
      <td>LAX</td>
      <td>SLC</td>
      <td>1625</td>
      <td>58.0</td>
      <td>94.0</td>
      <td>590</td>
      <td>1905</td>
      <td>65.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>UA</td>
      <td>DEN</td>
      <td>IAD</td>
      <td>823</td>
      <td>7.0</td>
      <td>154.0</td>
      <td>1452</td>
      <td>1333</td>
      <td>-13.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>MQ</td>
      <td>DFW</td>
      <td>VPS</td>
      <td>1305</td>
      <td>36.0</td>
      <td>85.0</td>
      <td>641</td>
      <td>1453</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>AA</td>
      <td>DFW</td>
      <td>DCA</td>
      <td>1555</td>
      <td>7.0</td>
      <td>126.0</td>
      <td>1192</td>
      <td>1935</td>
      <td>-7.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>WN</td>
      <td>LAX</td>
      <td>MCI</td>
      <td>1720</td>
      <td>48.0</td>
      <td>166.0</td>
      <td>1363</td>
      <td>2225</td>
      <td>39.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
fp = flights.pivot_table(index='AIRLINE', 
                         columns='ORG_AIR', 
                         values='CANCELLED', 
                         aggfunc='sum',
                         fill_value=0).round(2)
fp.head()
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
      <th>ORG_AIR</th>
      <th>ATL</th>
      <th>DEN</th>
      <th>DFW</th>
      <th>IAH</th>
      <th>LAS</th>
      <th>LAX</th>
      <th>MSP</th>
      <th>ORD</th>
      <th>PHX</th>
      <th>SFO</th>
    </tr>
    <tr>
      <th>AIRLINE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AA</th>
      <td>3</td>
      <td>4</td>
      <td>86</td>
      <td>3</td>
      <td>3</td>
      <td>11</td>
      <td>3</td>
      <td>35</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>AS</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>B6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>DL</th>
      <td>28</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>EV</th>
      <td>18</td>
      <td>6</td>
      <td>27</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
fg = flights.groupby(['AIRLINE', 'ORG_AIR'])['CANCELLED'].sum()
fg.head()
```




    AIRLINE  ORG_AIR
    AA       ATL         3
             DEN         4
             DFW        86
             IAH         3
             LAS         3
    Name: CANCELLED, dtype: int64




```python
fg_unstack = fg.unstack('ORG_AIR', fill_value=0)
fg_unstack.head()
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
      <th>ORG_AIR</th>
      <th>ATL</th>
      <th>DEN</th>
      <th>DFW</th>
      <th>IAH</th>
      <th>LAS</th>
      <th>LAX</th>
      <th>MSP</th>
      <th>ORD</th>
      <th>PHX</th>
      <th>SFO</th>
    </tr>
    <tr>
      <th>AIRLINE</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AA</th>
      <td>3</td>
      <td>4</td>
      <td>86</td>
      <td>3</td>
      <td>3</td>
      <td>11</td>
      <td>3</td>
      <td>35</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>AS</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>B6</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>DL</th>
      <td>28</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>EV</th>
      <td>18</td>
      <td>6</td>
      <td>27</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>53</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
fp.equals(fg_unstack)
```




    True




```python
fp2 = flights.pivot_table(index=['AIRLINE', 'MONTH'],
                          columns=['ORG_AIR', 'CANCELLED'],
                          values=['DEP_DELAY', 'DIST'],
                          aggfunc=[np.mean, np.sum],
                          fill_value=0)
fp2.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="10" halign="left">mean</th>
      <th>...</th>
      <th colspan="10" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="10" halign="left">DEP_DELAY</th>
      <th>...</th>
      <th colspan="10" halign="left">DIST</th>
    </tr>
    <tr>
      <th></th>
      <th>ORG_AIR</th>
      <th colspan="2" halign="left">ATL</th>
      <th colspan="2" halign="left">DEN</th>
      <th colspan="2" halign="left">DFW</th>
      <th colspan="2" halign="left">IAH</th>
      <th colspan="2" halign="left">LAS</th>
      <th>...</th>
      <th colspan="2" halign="left">LAX</th>
      <th colspan="2" halign="left">MSP</th>
      <th colspan="2" halign="left">ORD</th>
      <th colspan="2" halign="left">PHX</th>
      <th colspan="2" halign="left">SFO</th>
    </tr>
    <tr>
      <th></th>
      <th>CANCELLED</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>...</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>AIRLINE</th>
      <th>MONTH</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">AA</th>
      <th>1</th>
      <td>-3.250000</td>
      <td>0</td>
      <td>7.062500</td>
      <td>0</td>
      <td>11.977591</td>
      <td>-3.0</td>
      <td>9.750000</td>
      <td>0</td>
      <td>32.375000</td>
      <td>0</td>
      <td>...</td>
      <td>135921</td>
      <td>2475</td>
      <td>7281</td>
      <td>0</td>
      <td>129334</td>
      <td>0</td>
      <td>21018</td>
      <td>0</td>
      <td>33483</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-3.000000</td>
      <td>0</td>
      <td>5.461538</td>
      <td>0</td>
      <td>8.756579</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>0</td>
      <td>-3.055556</td>
      <td>0</td>
      <td>...</td>
      <td>113483</td>
      <td>5454</td>
      <td>5040</td>
      <td>0</td>
      <td>120572</td>
      <td>5398</td>
      <td>17049</td>
      <td>868</td>
      <td>32110</td>
      <td>2586</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.166667</td>
      <td>0</td>
      <td>7.666667</td>
      <td>0</td>
      <td>15.383784</td>
      <td>0.0</td>
      <td>10.900000</td>
      <td>0</td>
      <td>12.074074</td>
      <td>0</td>
      <td>...</td>
      <td>131836</td>
      <td>1744</td>
      <td>14471</td>
      <td>0</td>
      <td>127072</td>
      <td>802</td>
      <td>25770</td>
      <td>0</td>
      <td>43580</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.071429</td>
      <td>0</td>
      <td>20.266667</td>
      <td>0</td>
      <td>10.501493</td>
      <td>0.0</td>
      <td>6.933333</td>
      <td>0</td>
      <td>27.241379</td>
      <td>0</td>
      <td>...</td>
      <td>170285</td>
      <td>0</td>
      <td>4541</td>
      <td>0</td>
      <td>152154</td>
      <td>4718</td>
      <td>17727</td>
      <td>0</td>
      <td>51054</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.777778</td>
      <td>0</td>
      <td>23.466667</td>
      <td>0</td>
      <td>16.798780</td>
      <td>0.0</td>
      <td>3.055556</td>
      <td>0</td>
      <td>2.818182</td>
      <td>0</td>
      <td>...</td>
      <td>167484</td>
      <td>0</td>
      <td>6298</td>
      <td>0</td>
      <td>110864</td>
      <td>1999</td>
      <td>11164</td>
      <td>0</td>
      <td>40233</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 80 columns</p>
</div>




```python
flights.groupby(['AIRLINE', 'MONTH', 'ORG_AIR', 'CANCELLED'])['DEP_DELAY', 'DIST'] \
       .agg(['mean', 'sum']) \
       .unstack(['ORG_AIR', 'CANCELLED'], fill_value=0) \
       .swaplevel(0, 1, axis='columns') \
       .head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="10" halign="left">mean</th>
      <th>...</th>
      <th colspan="10" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="10" halign="left">DEP_DELAY</th>
      <th>...</th>
      <th colspan="10" halign="left">DIST</th>
    </tr>
    <tr>
      <th></th>
      <th>ORG_AIR</th>
      <th colspan="2" halign="left">ATL</th>
      <th colspan="2" halign="left">DEN</th>
      <th colspan="2" halign="left">DFW</th>
      <th colspan="2" halign="left">IAH</th>
      <th colspan="2" halign="left">LAS</th>
      <th>...</th>
      <th colspan="2" halign="left">LAX</th>
      <th colspan="2" halign="left">MSP</th>
      <th colspan="2" halign="left">ORD</th>
      <th colspan="2" halign="left">PHX</th>
      <th colspan="2" halign="left">SFO</th>
    </tr>
    <tr>
      <th></th>
      <th>CANCELLED</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>...</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>AIRLINE</th>
      <th>MONTH</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">AA</th>
      <th>1</th>
      <td>-3.250000</td>
      <td>NaN</td>
      <td>7.062500</td>
      <td>NaN</td>
      <td>11.977591</td>
      <td>-3.0</td>
      <td>9.750000</td>
      <td>NaN</td>
      <td>32.375000</td>
      <td>NaN</td>
      <td>...</td>
      <td>135921.0</td>
      <td>2475.0</td>
      <td>7281.0</td>
      <td>NaN</td>
      <td>129334.0</td>
      <td>NaN</td>
      <td>21018.0</td>
      <td>NaN</td>
      <td>33483.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-3.000000</td>
      <td>NaN</td>
      <td>5.461538</td>
      <td>NaN</td>
      <td>8.756579</td>
      <td>NaN</td>
      <td>1.000000</td>
      <td>NaN</td>
      <td>-3.055556</td>
      <td>NaN</td>
      <td>...</td>
      <td>113483.0</td>
      <td>5454.0</td>
      <td>5040.0</td>
      <td>NaN</td>
      <td>120572.0</td>
      <td>5398.0</td>
      <td>17049.0</td>
      <td>868.0</td>
      <td>32110.0</td>
      <td>2586.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.166667</td>
      <td>NaN</td>
      <td>7.666667</td>
      <td>NaN</td>
      <td>15.383784</td>
      <td>NaN</td>
      <td>10.900000</td>
      <td>NaN</td>
      <td>12.074074</td>
      <td>NaN</td>
      <td>...</td>
      <td>131836.0</td>
      <td>1744.0</td>
      <td>14471.0</td>
      <td>NaN</td>
      <td>127072.0</td>
      <td>802.0</td>
      <td>25770.0</td>
      <td>NaN</td>
      <td>43580.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.071429</td>
      <td>NaN</td>
      <td>20.266667</td>
      <td>NaN</td>
      <td>10.501493</td>
      <td>NaN</td>
      <td>6.933333</td>
      <td>NaN</td>
      <td>27.241379</td>
      <td>NaN</td>
      <td>...</td>
      <td>170285.0</td>
      <td>NaN</td>
      <td>4541.0</td>
      <td>NaN</td>
      <td>152154.0</td>
      <td>4718.0</td>
      <td>17727.0</td>
      <td>NaN</td>
      <td>51054.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.777778</td>
      <td>NaN</td>
      <td>23.466667</td>
      <td>NaN</td>
      <td>16.798780</td>
      <td>NaN</td>
      <td>3.055556</td>
      <td>NaN</td>
      <td>2.818182</td>
      <td>NaN</td>
      <td>...</td>
      <td>167484.0</td>
      <td>NaN</td>
      <td>6298.0</td>
      <td>NaN</td>
      <td>110864.0</td>
      <td>1999.0</td>
      <td>11164.0</td>
      <td>NaN</td>
      <td>40233.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 80 columns</p>
</div>




```python

```

#### Renaming axis levels for easy reshaping


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv')
```


```python
cg = college.groupby(['STABBR', 'RELAFFIL'])['UGDS', 'SATMTMID'] \
            .agg(['count', 'min', 'max']).head(6)
```


```python
cg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">UGDS</th>
      <th colspan="3" halign="left">SATMTMID</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
    </tr>
    <tr>
      <th>STABBR</th>
      <th>RELAFFIL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">AK</th>
      <th>0</th>
      <td>7</td>
      <td>109.0</td>
      <td>12865.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>27.0</td>
      <td>275.0</td>
      <td>1</td>
      <td>503.0</td>
      <td>503.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AL</th>
      <th>0</th>
      <td>71</td>
      <td>12.0</td>
      <td>29851.0</td>
      <td>13</td>
      <td>420.0</td>
      <td>590.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>13.0</td>
      <td>3033.0</td>
      <td>8</td>
      <td>400.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AR</th>
      <th>0</th>
      <td>68</td>
      <td>18.0</td>
      <td>21405.0</td>
      <td>9</td>
      <td>427.0</td>
      <td>565.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>20.0</td>
      <td>4485.0</td>
      <td>7</td>
      <td>495.0</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg = cg.rename_axis(['AGG_COLS', 'AGG_FUNCS'], axis='columns')
cg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>AGG_COLS</th>
      <th colspan="3" halign="left">UGDS</th>
      <th colspan="3" halign="left">SATMTMID</th>
    </tr>
    <tr>
      <th></th>
      <th>AGG_FUNCS</th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
    </tr>
    <tr>
      <th>STABBR</th>
      <th>RELAFFIL</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">AK</th>
      <th>0</th>
      <td>7</td>
      <td>109.0</td>
      <td>12865.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>27.0</td>
      <td>275.0</td>
      <td>1</td>
      <td>503.0</td>
      <td>503.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AL</th>
      <th>0</th>
      <td>71</td>
      <td>12.0</td>
      <td>29851.0</td>
      <td>13</td>
      <td>420.0</td>
      <td>590.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>13.0</td>
      <td>3033.0</td>
      <td>8</td>
      <td>400.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AR</th>
      <th>0</th>
      <td>68</td>
      <td>18.0</td>
      <td>21405.0</td>
      <td>9</td>
      <td>427.0</td>
      <td>565.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>20.0</td>
      <td>4485.0</td>
      <td>7</td>
      <td>495.0</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg.stack('AGG_FUNCS').head()
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
      <th></th>
      <th>AGG_COLS</th>
      <th>UGDS</th>
      <th>SATMTMID</th>
    </tr>
    <tr>
      <th>STABBR</th>
      <th>RELAFFIL</th>
      <th>AGG_FUNCS</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">AK</th>
      <th rowspan="3" valign="top">0</th>
      <th>count</th>
      <td>7.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>109.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12865.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>count</th>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>27.0</td>
      <td>503.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg.stack('AGG_FUNCS').swaplevel('AGG_FUNCS', 'STABBR', axis='index').head()
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
      <th></th>
      <th>AGG_COLS</th>
      <th>UGDS</th>
      <th>SATMTMID</th>
    </tr>
    <tr>
      <th>AGG_FUNCS</th>
      <th>RELAFFIL</th>
      <th>STABBR</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <th>0</th>
      <th>AK</th>
      <td>7.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>min</th>
      <th>0</th>
      <th>AK</th>
      <td>109.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <th>0</th>
      <th>AK</th>
      <td>12865.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>count</th>
      <th>1</th>
      <th>AK</th>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>min</th>
      <th>1</th>
      <th>AK</th>
      <td>27.0</td>
      <td>503.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg.stack('AGG_FUNCS') \
  .swaplevel('AGG_FUNCS', 'STABBR', axis='index') \
  .sort_index(level='RELAFFIL', axis='index') \
  .sort_index(level='AGG_COLS', axis='columns').head(6)
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
      <th></th>
      <th>AGG_COLS</th>
      <th>SATMTMID</th>
      <th>UGDS</th>
    </tr>
    <tr>
      <th>AGG_FUNCS</th>
      <th>RELAFFIL</th>
      <th>STABBR</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">count</th>
      <th rowspan="3" valign="top">0</th>
      <th>AK</th>
      <td>0.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>AL</th>
      <td>13.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>AR</th>
      <td>9.0</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">max</th>
      <th rowspan="3" valign="top">0</th>
      <th>AK</th>
      <td>NaN</td>
      <td>12865.0</td>
    </tr>
    <tr>
      <th>AL</th>
      <td>590.0</td>
      <td>29851.0</td>
    </tr>
    <tr>
      <th>AR</th>
      <td>565.0</td>
      <td>21405.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg.stack('AGG_FUNCS').unstack(['RELAFFIL', 'STABBR'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>AGG_COLS</th>
      <th colspan="6" halign="left">UGDS</th>
      <th colspan="6" halign="left">SATMTMID</th>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>STABBR</th>
      <th>AK</th>
      <th>AK</th>
      <th>AL</th>
      <th>AL</th>
      <th>AR</th>
      <th>AR</th>
      <th>AK</th>
      <th>AK</th>
      <th>AL</th>
      <th>AL</th>
      <th>AR</th>
      <th>AR</th>
    </tr>
    <tr>
      <th>AGG_FUNCS</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>71.0</td>
      <td>18.0</td>
      <td>68.0</td>
      <td>14.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>13.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>109.0</td>
      <td>27.0</td>
      <td>12.0</td>
      <td>13.0</td>
      <td>18.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>503.0</td>
      <td>420.0</td>
      <td>400.0</td>
      <td>427.0</td>
      <td>495.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12865.0</td>
      <td>275.0</td>
      <td>29851.0</td>
      <td>3033.0</td>
      <td>21405.0</td>
      <td>4485.0</td>
      <td>NaN</td>
      <td>503.0</td>
      <td>590.0</td>
      <td>560.0</td>
      <td>565.0</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
cg.stack(['AGG_FUNCS', 'AGG_COLS']).head(12)
```




    STABBR  RELAFFIL  AGG_FUNCS  AGG_COLS
    AK      0         count      UGDS            7.0
                                 SATMTMID        0.0
                      min        UGDS          109.0
                      max        UGDS        12865.0
            1         count      UGDS            3.0
                                 SATMTMID        1.0
                      min        UGDS           27.0
                                 SATMTMID      503.0
                      max        UGDS          275.0
                                 SATMTMID      503.0
    AL      0         count      UGDS           71.0
                                 SATMTMID       13.0
    dtype: float64




```python
cg.rename_axis([None, None], axis='index').rename_axis([None, None], axis='columns')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">UGDS</th>
      <th colspan="3" halign="left">SATMTMID</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">AK</th>
      <th>0</th>
      <td>7</td>
      <td>109.0</td>
      <td>12865.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>27.0</td>
      <td>275.0</td>
      <td>1</td>
      <td>503.0</td>
      <td>503.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AL</th>
      <th>0</th>
      <td>71</td>
      <td>12.0</td>
      <td>29851.0</td>
      <td>13</td>
      <td>420.0</td>
      <td>590.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>13.0</td>
      <td>3033.0</td>
      <td>8</td>
      <td>400.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">AR</th>
      <th>0</th>
      <td>68</td>
      <td>18.0</td>
      <td>21405.0</td>
      <td>9</td>
      <td>427.0</td>
      <td>565.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14</td>
      <td>20.0</td>
      <td>4485.0</td>
      <td>7</td>
      <td>495.0</td>
      <td>600.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### Tidying when multiple variables are stored as column names


```python
import pandas as pd
import numpy as np
```


```python
weightlifting = pd.read_csv('data/weightlifting_men.csv')
weightlifting
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
      <th>Weight Category</th>
      <th>M35 35-39</th>
      <th>M40 40-44</th>
      <th>M45 45-49</th>
      <th>M50 50-54</th>
      <th>M55 55-59</th>
      <th>M60 60-64</th>
      <th>M65 65-69</th>
      <th>M70 70-74</th>
      <th>M75 75-79</th>
      <th>M80 80+</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>137</td>
      <td>130</td>
      <td>125</td>
      <td>115</td>
      <td>102</td>
      <td>92</td>
      <td>80</td>
      <td>67</td>
      <td>62</td>
      <td>55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>62</td>
      <td>152</td>
      <td>145</td>
      <td>137</td>
      <td>127</td>
      <td>112</td>
      <td>102</td>
      <td>90</td>
      <td>75</td>
      <td>67</td>
      <td>57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69</td>
      <td>167</td>
      <td>160</td>
      <td>150</td>
      <td>140</td>
      <td>125</td>
      <td>112</td>
      <td>97</td>
      <td>82</td>
      <td>75</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>77</td>
      <td>182</td>
      <td>172</td>
      <td>165</td>
      <td>150</td>
      <td>135</td>
      <td>122</td>
      <td>107</td>
      <td>90</td>
      <td>82</td>
      <td>65</td>
    </tr>
    <tr>
      <th>4</th>
      <td>85</td>
      <td>192</td>
      <td>182</td>
      <td>175</td>
      <td>160</td>
      <td>142</td>
      <td>130</td>
      <td>112</td>
      <td>95</td>
      <td>87</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>94</td>
      <td>202</td>
      <td>192</td>
      <td>182</td>
      <td>167</td>
      <td>150</td>
      <td>137</td>
      <td>120</td>
      <td>100</td>
      <td>90</td>
      <td>75</td>
    </tr>
    <tr>
      <th>6</th>
      <td>105</td>
      <td>210</td>
      <td>200</td>
      <td>190</td>
      <td>175</td>
      <td>157</td>
      <td>142</td>
      <td>122</td>
      <td>102</td>
      <td>95</td>
      <td>80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>105+</td>
      <td>217</td>
      <td>207</td>
      <td>197</td>
      <td>182</td>
      <td>165</td>
      <td>150</td>
      <td>127</td>
      <td>107</td>
      <td>100</td>
      <td>85</td>
    </tr>
  </tbody>
</table>
</div>




```python
wl_melt = weightlifting.melt(id_vars='Weight Category', 
                             var_name='sex_age', 
                             value_name='Qual Total')
wl_melt.head()
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
      <th>Weight Category</th>
      <th>sex_age</th>
      <th>Qual Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>M35 35-39</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>62</td>
      <td>M35 35-39</td>
      <td>152</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69</td>
      <td>M35 35-39</td>
      <td>167</td>
    </tr>
    <tr>
      <th>3</th>
      <td>77</td>
      <td>M35 35-39</td>
      <td>182</td>
    </tr>
    <tr>
      <th>4</th>
      <td>85</td>
      <td>M35 35-39</td>
      <td>192</td>
    </tr>
  </tbody>
</table>
</div>




```python
sex_age = wl_melt['sex_age'].str.split(expand=True)
sex_age.head()
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
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
sex_age.columns = ['Sex', 'Age Group']
sex_age.head()
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
      <th>Sex</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M35</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
sex_age['Sex'] = sex_age['Sex'].str[0]
sex_age.head()
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
      <th>Sex</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
wl_cat_total = wl_melt[['Weight Category', 'Qual Total']]
wl_tidy = pd.concat([sex_age, wl_cat_total], axis='columns')
wl_tidy.head()
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
      <th>Sex</th>
      <th>Age Group</th>
      <th>Weight Category</th>
      <th>Qual Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>35-39</td>
      <td>56</td>
      <td>137</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M</td>
      <td>35-39</td>
      <td>62</td>
      <td>152</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>35-39</td>
      <td>69</td>
      <td>167</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M</td>
      <td>35-39</td>
      <td>77</td>
      <td>182</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>35-39</td>
      <td>85</td>
      <td>192</td>
    </tr>
  </tbody>
</table>
</div>




```python
cols = ['Weight Category', 'Qual Total']
sex_age[cols] = wl_melt[cols]
```


```python
age_group = wl_melt.sex_age.str.extract('(\d{2}[-+](?:\d{2})?)', expand=False)
sex = wl_melt.sex_age.str[0]
new_cols = {'Sex':sex, 
            'Age Group': age_group}
```


```python
wl_tidy2 = wl_melt.assign(**new_cols).drop('sex_age', axis='columns')
wl_tidy2.head()
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
      <th>Weight Category</th>
      <th>Qual Total</th>
      <th>Sex</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>56</td>
      <td>137</td>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>62</td>
      <td>152</td>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69</td>
      <td>167</td>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>77</td>
      <td>182</td>
      <td>M</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>85</td>
      <td>192</td>
      <td>M</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
wl_tidy2.sort_index(axis=1).equals(wl_tidy.sort_index(axis=1))
```




    True




```python

```
