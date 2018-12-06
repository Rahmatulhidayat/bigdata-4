# Chapter 4 - Pandas Foundation pada buku Pandas Cookbook
#### download data yang akan digunakan pada [Pandas-Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)
#### data yang saya dowload saya letakkan pada "/data"

# Pembahasan Praktik :
## Chapter 4
### Selecting Series data


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
city.head()
```




    INSTNM
    Alabama A & M University                   Normal
    University of Alabama at Birmingham    Birmingham
    Amridge University                     Montgomery
    University of Alabama in Huntsville    Huntsville
    Alabama State University               Montgomery
    Name: CITY, dtype: object




```python
city.iloc[3]
```




    'Huntsville'




```python
city.iloc[[10,20,30]]
```




    INSTNM
    Birmingham Southern College                            Birmingham
    George C Wallace State Community College-Hanceville    Hanceville
    Judson College                                             Marion
    Name: CITY, dtype: object




```python
city.iloc[4:50:10]
```




    INSTNM
    Alabama State University              Montgomery
    Enterprise State Community College    Enterprise
    Heritage Christian University           Florence
    Marion Military Institute                 Marion
    Reid State Technical College           Evergreen
    Name: CITY, dtype: object




```python
city.loc['Heritage Christian University']
```




    'Florence'




```python
np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
labels
```




    ['Northwest HVAC/R Training Center',
     'California State University-Dominguez Hills',
     'Lower Columbia College',
     'Southwest Acupuncture College-Boulder']




```python
city.loc[labels]
```




    INSTNM
    Northwest HVAC/R Training Center                Spokane
    California State University-Dominguez Hills      Carson
    Lower Columbia College                         Longview
    Southwest Acupuncture College-Boulder           Boulder
    Name: CITY, dtype: object




```python
city.loc['Alabama State University':'Reid State Technical College':10]
```




    INSTNM
    Alabama State University              Montgomery
    Enterprise State Community College    Enterprise
    Heritage Christian University           Florence
    Marion Military Institute                 Marion
    Reid State Technical College           Evergreen
    Name: CITY, dtype: object




```python
city['Alabama State University':'Reid State Technical College':10]
```




    INSTNM
    Alabama State University              Montgomery
    Enterprise State Community College    Enterprise
    Heritage Christian University           Florence
    Marion Military Institute                 Marion
    Reid State Technical College           Evergreen
    Name: CITY, dtype: object




```python
city.iloc[[3]]
```




    INSTNM
    University of Alabama in Huntsville    Huntsville
    Name: CITY, dtype: object




```python
city.loc['Reid State Technical College':'Alabama State University':10]
```




    Series([], Name: CITY, dtype: object)




```python
city.loc['Reid State Technical College':'Alabama State University':-10]
```




    INSTNM
    Reid State Technical College           Evergreen
    Marion Military Institute                 Marion
    Heritage Christian University           Florence
    Enterprise State Community College    Enterprise
    Alabama State University              Montgomery
    Name: CITY, dtype: object




```python

```

### Selecting DataFrame rows


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
      <th>WOMENONLY</th>
      <th>RELAFFIL</th>
      <th>SATVRMID</th>
      <th>SATMTMID</th>
      <th>DISTANCEONLY</th>
      <th>UGDS</th>
      <th>...</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>PPTUG_EF</th>
      <th>CURROPER</th>
      <th>PCTPELL</th>
      <th>PCTFLOAN</th>
      <th>UG25ABV</th>
      <th>MD_EARN_WNE_P10</th>
      <th>GRAD_DEBT_MDN_SUPP</th>
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
      <th>Alabama A &amp; M University</th>
      <td>Normal</td>
      <td>AL</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>424.0</td>
      <td>420.0</td>
      <td>0.0</td>
      <td>4206.0</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
      <td>0.0656</td>
      <td>1</td>
      <td>0.7356</td>
      <td>0.8284</td>
      <td>0.1049</td>
      <td>30300</td>
      <td>33888</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>Birmingham</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>570.0</td>
      <td>565.0</td>
      <td>0.0</td>
      <td>11383.0</td>
      <td>...</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
      <td>0.2607</td>
      <td>1</td>
      <td>0.3460</td>
      <td>0.5214</td>
      <td>0.2422</td>
      <td>39700</td>
      <td>21941.5</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>Montgomery</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>291.0</td>
      <td>...</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
      <td>0.4536</td>
      <td>1</td>
      <td>0.6801</td>
      <td>0.7795</td>
      <td>0.8540</td>
      <td>40100</td>
      <td>23370</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>Huntsville</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>595.0</td>
      <td>590.0</td>
      <td>0.0</td>
      <td>5451.0</td>
      <td>...</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
      <td>0.2146</td>
      <td>1</td>
      <td>0.3072</td>
      <td>0.4596</td>
      <td>0.2640</td>
      <td>45500</td>
      <td>24097</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>Montgomery</td>
      <td>AL</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>425.0</td>
      <td>430.0</td>
      <td>0.0</td>
      <td>4811.0</td>
      <td>...</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
      <td>0.0892</td>
      <td>1</td>
      <td>0.7347</td>
      <td>0.7554</td>
      <td>0.1270</td>
      <td>26600</td>
      <td>33118.5</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 26 columns</p>
</div>




```python
pd.options.display.max_rows = 6
```


```python
college.iloc[60]
```




    CITY                  Anchorage
    STABBR                       AK
    HBCU                          0
                            ...    
    UG25ABV                  0.4386
    MD_EARN_WNE_P10           42500
    GRAD_DEBT_MDN_SUPP      19449.5
    Name: University of Alaska Anchorage, Length: 26, dtype: object




```python
college.loc['University of Alaska Anchorage']
```




    CITY                  Anchorage
    STABBR                       AK
    HBCU                          0
                            ...    
    UG25ABV                  0.4386
    MD_EARN_WNE_P10           42500
    GRAD_DEBT_MDN_SUPP      19449.5
    Name: University of Alaska Anchorage, Length: 26, dtype: object




```python
college.iloc[[60, 99, 3]]
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
      <th>WOMENONLY</th>
      <th>RELAFFIL</th>
      <th>SATVRMID</th>
      <th>SATMTMID</th>
      <th>DISTANCEONLY</th>
      <th>UGDS</th>
      <th>...</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>PPTUG_EF</th>
      <th>CURROPER</th>
      <th>PCTPELL</th>
      <th>PCTFLOAN</th>
      <th>UG25ABV</th>
      <th>MD_EARN_WNE_P10</th>
      <th>GRAD_DEBT_MDN_SUPP</th>
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
      <th>University of Alaska Anchorage</th>
      <td>Anchorage</td>
      <td>AK</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>12865.0</td>
      <td>...</td>
      <td>0.0980</td>
      <td>0.0181</td>
      <td>0.0457</td>
      <td>0.4539</td>
      <td>1</td>
      <td>0.2385</td>
      <td>0.2647</td>
      <td>0.4386</td>
      <td>42500</td>
      <td>19449.5</td>
    </tr>
    <tr>
      <th>International Academy of Hair Design</th>
      <td>Tempe</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>188.0</td>
      <td>...</td>
      <td>0.0160</td>
      <td>0.0000</td>
      <td>0.0638</td>
      <td>0.0000</td>
      <td>0</td>
      <td>0.7185</td>
      <td>0.7346</td>
      <td>0.3905</td>
      <td>22200</td>
      <td>10556</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>Huntsville</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>595.0</td>
      <td>590.0</td>
      <td>0.0</td>
      <td>5451.0</td>
      <td>...</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
      <td>0.2146</td>
      <td>1</td>
      <td>0.3072</td>
      <td>0.4596</td>
      <td>0.2640</td>
      <td>45500</td>
      <td>24097</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 26 columns</p>
</div>




```python
labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
college.loc[labels]
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
      <th>WOMENONLY</th>
      <th>RELAFFIL</th>
      <th>SATVRMID</th>
      <th>SATMTMID</th>
      <th>DISTANCEONLY</th>
      <th>UGDS</th>
      <th>...</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>PPTUG_EF</th>
      <th>CURROPER</th>
      <th>PCTPELL</th>
      <th>PCTFLOAN</th>
      <th>UG25ABV</th>
      <th>MD_EARN_WNE_P10</th>
      <th>GRAD_DEBT_MDN_SUPP</th>
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
      <th>University of Alaska Anchorage</th>
      <td>Anchorage</td>
      <td>AK</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>12865.0</td>
      <td>...</td>
      <td>0.0980</td>
      <td>0.0181</td>
      <td>0.0457</td>
      <td>0.4539</td>
      <td>1</td>
      <td>0.2385</td>
      <td>0.2647</td>
      <td>0.4386</td>
      <td>42500</td>
      <td>19449.5</td>
    </tr>
    <tr>
      <th>International Academy of Hair Design</th>
      <td>Tempe</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>188.0</td>
      <td>...</td>
      <td>0.0160</td>
      <td>0.0000</td>
      <td>0.0638</td>
      <td>0.0000</td>
      <td>0</td>
      <td>0.7185</td>
      <td>0.7346</td>
      <td>0.3905</td>
      <td>22200</td>
      <td>10556</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>Huntsville</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>595.0</td>
      <td>590.0</td>
      <td>0.0</td>
      <td>5451.0</td>
      <td>...</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
      <td>0.2146</td>
      <td>1</td>
      <td>0.3072</td>
      <td>0.4596</td>
      <td>0.2640</td>
      <td>45500</td>
      <td>24097</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 26 columns</p>
</div>




```python
college.iloc[99:102]
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
      <th>WOMENONLY</th>
      <th>RELAFFIL</th>
      <th>SATVRMID</th>
      <th>SATMTMID</th>
      <th>DISTANCEONLY</th>
      <th>UGDS</th>
      <th>...</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>PPTUG_EF</th>
      <th>CURROPER</th>
      <th>PCTPELL</th>
      <th>PCTFLOAN</th>
      <th>UG25ABV</th>
      <th>MD_EARN_WNE_P10</th>
      <th>GRAD_DEBT_MDN_SUPP</th>
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
      <th>International Academy of Hair Design</th>
      <td>Tempe</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>188.0</td>
      <td>...</td>
      <td>0.0160</td>
      <td>0.0000</td>
      <td>0.0638</td>
      <td>0.0000</td>
      <td>0</td>
      <td>0.7185</td>
      <td>0.7346</td>
      <td>0.3905</td>
      <td>22200</td>
      <td>10556</td>
    </tr>
    <tr>
      <th>GateWay Community College</th>
      <td>Phoenix</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>5211.0</td>
      <td>...</td>
      <td>0.0127</td>
      <td>0.0161</td>
      <td>0.0702</td>
      <td>0.7465</td>
      <td>1</td>
      <td>0.3270</td>
      <td>0.2189</td>
      <td>0.5832</td>
      <td>29800</td>
      <td>7283</td>
    </tr>
    <tr>
      <th>Mesa Community College</th>
      <td>Mesa</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>19055.0</td>
      <td>...</td>
      <td>0.0205</td>
      <td>0.0257</td>
      <td>0.0682</td>
      <td>0.6457</td>
      <td>1</td>
      <td>0.3423</td>
      <td>0.2207</td>
      <td>0.4010</td>
      <td>35200</td>
      <td>8000</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 26 columns</p>
</div>




```python
start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
college.loc[start:stop]
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
      <th>WOMENONLY</th>
      <th>RELAFFIL</th>
      <th>SATVRMID</th>
      <th>SATMTMID</th>
      <th>DISTANCEONLY</th>
      <th>UGDS</th>
      <th>...</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
      <th>PPTUG_EF</th>
      <th>CURROPER</th>
      <th>PCTPELL</th>
      <th>PCTFLOAN</th>
      <th>UG25ABV</th>
      <th>MD_EARN_WNE_P10</th>
      <th>GRAD_DEBT_MDN_SUPP</th>
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
      <th>International Academy of Hair Design</th>
      <td>Tempe</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>188.0</td>
      <td>...</td>
      <td>0.0160</td>
      <td>0.0000</td>
      <td>0.0638</td>
      <td>0.0000</td>
      <td>0</td>
      <td>0.7185</td>
      <td>0.7346</td>
      <td>0.3905</td>
      <td>22200</td>
      <td>10556</td>
    </tr>
    <tr>
      <th>GateWay Community College</th>
      <td>Phoenix</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>5211.0</td>
      <td>...</td>
      <td>0.0127</td>
      <td>0.0161</td>
      <td>0.0702</td>
      <td>0.7465</td>
      <td>1</td>
      <td>0.3270</td>
      <td>0.2189</td>
      <td>0.5832</td>
      <td>29800</td>
      <td>7283</td>
    </tr>
    <tr>
      <th>Mesa Community College</th>
      <td>Mesa</td>
      <td>AZ</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>19055.0</td>
      <td>...</td>
      <td>0.0205</td>
      <td>0.0257</td>
      <td>0.0682</td>
      <td>0.6457</td>
      <td>1</td>
      <td>0.3423</td>
      <td>0.2207</td>
      <td>0.4010</td>
      <td>35200</td>
      <td>8000</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 26 columns</p>
</div>




```python
college.iloc[[60, 99, 3]].index.tolist()
```




    ['University of Alaska Anchorage',
     'International Academy of Hair Design',
     'University of Alabama in Huntsville']




```python

```

### Selecting DataFrame rows and columns simultaneously


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college.iloc[:3, :4]
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>Normal</td>
      <td>AL</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>Birmingham</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>Montgomery</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.loc[:'Amridge University', :'MENONLY']
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
      <th>CITY</th>
      <th>STABBR</th>
      <th>HBCU</th>
      <th>MENONLY</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>Normal</td>
      <td>AL</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>Birmingham</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>Montgomery</td>
      <td>AL</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.iloc[:, [4,6]].head()
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
      <th>WOMENONLY</th>
      <th>SATVRMID</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0</td>
      <td>424.0</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.0</td>
      <td>570.0</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.0</td>
      <td>595.0</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0</td>
      <td>425.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.loc[:, ['WOMENONLY', 'SATVRMID']]
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
      <th>WOMENONLY</th>
      <th>SATVRMID</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0</td>
      <td>424.0</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.0</td>
      <td>570.0</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.0</td>
      <td>595.0</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0</td>
      <td>425.0</td>
    </tr>
    <tr>
      <th>The University of Alabama</th>
      <td>0.0</td>
      <td>555.0</td>
    </tr>
    <tr>
      <th>Central Alabama Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Athens State University</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Auburn University at Montgomery</th>
      <td>0.0</td>
      <td>486.0</td>
    </tr>
    <tr>
      <th>Auburn University</th>
      <td>0.0</td>
      <td>575.0</td>
    </tr>
    <tr>
      <th>Birmingham Southern College</th>
      <td>0.0</td>
      <td>560.0</td>
    </tr>
    <tr>
      <th>Chattahoochee Valley Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Concordia College Alabama</th>
      <td>0.0</td>
      <td>420.0</td>
    </tr>
    <tr>
      <th>South University-Montgomery</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Enterprise State Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>James H Faulkner State Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Faulkner University</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Gadsden State Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>New Beginning College of Cosmetology</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>George C Wallace State Community College-Dothan</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>George C Wallace State Community College-Hanceville</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>George C Wallace State Community College-Selma</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Herzing University-Birmingham</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Huntingdon College</th>
      <td>0.0</td>
      <td>510.0</td>
    </tr>
    <tr>
      <th>Heritage Christian University</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>J F Drake State Community and Technical College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Jacksonville State University</th>
      <td>0.0</td>
      <td>495.0</td>
    </tr>
    <tr>
      <th>Jefferson Davis Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Jefferson State Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>John C Calhoun State Community College</th>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Strayer University-Lawrenceville</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Piscataway</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Utah County Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>L'esprit Academy - Royal Oak</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>National Career Institute - Jersey City Branch</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Cobb Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Morrow Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Roswell Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Douglasville Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Lithonia Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Savannah Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Augusta Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Columbus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Columbia Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Charleston Campus</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Irving</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Katy</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Northwest Houston</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Plano</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Cedar Hill</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-North Dallas</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-San Antonio</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Strayer University-Stafford</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>WestMed College - Merced</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Vantage College</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>SAE Institute of Technology  San Francisco</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Rasmussen College - Overland Park</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>National Personal Training Institute of Cleveland</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Bay Area Medical Academy - San Jose Satellite Location</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Excel Learning Center-San Antonio South</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>7535 rows × 2 columns</p>
</div>




```python
college.iloc[[100, 200], [7, 15]]
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
      <th>SATMTMID</th>
      <th>UGDS_NHPI</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GateWay Community College</th>
      <td>NaN</td>
      <td>0.0029</td>
    </tr>
    <tr>
      <th>American Baptist Seminary of the West</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
rows = ['GateWay Community College', 'American Baptist Seminary of the West']
columns = ['SATMTMID', 'UGDS_NHPI']
college.loc[rows, columns]
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
      <th>SATMTMID</th>
      <th>UGDS_NHPI</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GateWay Community College</th>
      <td>NaN</td>
      <td>0.0029</td>
    </tr>
    <tr>
      <th>American Baptist Seminary of the West</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.iloc[5, -4]
```




    0.401




```python
college.loc['The University of Alabama', 'PCTFLOAN']
```




    0.401




```python
college.iloc[90:80:-2, 5]
```




    INSTNM
    Empire Beauty School-Flagstaff     0
    Charles of Italy Beauty College    0
    Central Arizona College            0
    University of Arizona              0
    Arizona State University-Tempe     0
    Name: RELAFFIL, dtype: int64




```python
start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
college.loc[start:stop:-2, 'RELAFFIL']
```




    INSTNM
    Empire Beauty School-Flagstaff     0
    Charles of Italy Beauty College    0
    Central Arizona College            0
    University of Arizona              0
    Arizona State University-Tempe     0
    Name: RELAFFIL, dtype: int64




```python

```

### Selecting data with both integers and labels


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
```


```python
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
col_start, col_end
```




    (10, 19)




```python
college.iloc[:5, col_start:col_end]
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
row_start = college.index[10]
row_end = college.index[15]
college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN']
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
      <th>Birmingham Southern College</th>
      <td>0.7983</td>
      <td>0.1102</td>
      <td>0.0195</td>
      <td>0.0517</td>
      <td>0.0102</td>
      <td>0.0000</td>
      <td>0.0051</td>
      <td>0.0000</td>
      <td>0.0051</td>
    </tr>
    <tr>
      <th>Chattahoochee Valley Community College</th>
      <td>0.4661</td>
      <td>0.4372</td>
      <td>0.0492</td>
      <td>0.0127</td>
      <td>0.0023</td>
      <td>0.0035</td>
      <td>0.0151</td>
      <td>0.0000</td>
      <td>0.0139</td>
    </tr>
    <tr>
      <th>Concordia College Alabama</th>
      <td>0.0280</td>
      <td>0.8758</td>
      <td>0.0373</td>
      <td>0.0093</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0031</td>
      <td>0.0466</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>South University-Montgomery</th>
      <td>0.3046</td>
      <td>0.6054</td>
      <td>0.0153</td>
      <td>0.0153</td>
      <td>0.0153</td>
      <td>0.0096</td>
      <td>0.0000</td>
      <td>0.0019</td>
      <td>0.0326</td>
    </tr>
    <tr>
      <th>Enterprise State Community College</th>
      <td>0.6408</td>
      <td>0.2435</td>
      <td>0.0509</td>
      <td>0.0202</td>
      <td>0.0081</td>
      <td>0.0029</td>
      <td>0.0254</td>
      <td>0.0012</td>
      <td>0.0069</td>
    </tr>
    <tr>
      <th>James H Faulkner State Community College</th>
      <td>0.6979</td>
      <td>0.2259</td>
      <td>0.0320</td>
      <td>0.0084</td>
      <td>0.0177</td>
      <td>0.0014</td>
      <td>0.0152</td>
      <td>0.0007</td>
      <td>0.0009</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

### Speeding up scalar selection


```python
import pandas as pd
import numpy as np
```


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
college.loc[cn, 'UGDS_WHITE']
```




    0.6609999999999999




```python
college.at[cn, 'UGDS_WHITE']
```




    0.6609999999999999




```python
%timeit college.loc[cn, 'UGDS_WHITE']
```

    5.82 µs ± 263 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
%timeit college.at[cn, 'UGDS_WHITE']
```

    3.45 µs ± 24 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
```


```python
row_num, col_num
```




    (3765, 10)




```python
%timeit college.iloc[row_num, col_num]
```

    6.46 µs ± 222 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
%timeit college.iat[row_num, col_num]
```

    3.98 µs ± 179 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
%timeit college.iloc[5, col_num]
```

    6.09 µs ± 22.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
%timeit college.iat[5, col_num]
```

    4.02 µs ± 247 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



```python
state = college['STABBR']
```


```python
state.iat[1000]
```




    'IL'




```python
state.at['Stanford University']
```




    'CA'




```python

```
