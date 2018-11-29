
# Chapter 3 - Pandas Foundation pada buku Pandas Cookbook
#### download data yang akan digunakan pada [Pandas-Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)
#### data yang saya dowload saya letakkan pada "/data"
```bash
import pandas as pd
import numpy as np
```

# Developing a data analysis routine


```python
college = pd.read_csv('data/college.csv')
```


```python
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
      <th>INSTNM</th>
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
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama A &amp; M University</td>
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
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
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
      <th>1</th>
      <td>University of Alabama at Birmingham</td>
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
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
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
      <th>2</th>
      <td>Amridge University</td>
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
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
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
      <th>3</th>
      <td>University of Alabama in Huntsville</td>
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
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
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
      <th>4</th>
      <td>Alabama State University</td>
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
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
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
</div>




```python
college.shape
```




    (7535, 27)




```python
with pd.option_context('display.max_rows', 8):
    display(college.describe(include=[np.number]).T)
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <td>7535.0</td>
      <td>0.190975</td>
      <td>0.393096</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>0.923291</td>
      <td>0.266146</td>
      <td>0.0</td>
      <td>1.0000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.3578</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.3329</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.2415</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>22 rows × 8 columns</p>
</div>



```python
college.describe(include=[np.object, pd.Categorical]).T
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
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>INSTNM</th>
      <td>7535</td>
      <td>7535</td>
      <td>San Francisco State University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>CITY</th>
      <td>7535</td>
      <td>2514</td>
      <td>New York</td>
      <td>87</td>
    </tr>
    <tr>
      <th>STABBR</th>
      <td>7535</td>
      <td>59</td>
      <td>CA</td>
      <td>773</td>
    </tr>
    <tr>
      <th>MD_EARN_WNE_P10</th>
      <td>6413</td>
      <td>598</td>
      <td>PrivacySuppressed</td>
      <td>822</td>
    </tr>
    <tr>
      <th>GRAD_DEBT_MDN_SUPP</th>
      <td>7503</td>
      <td>2038</td>
      <td>PrivacySuppressed</td>
      <td>1510</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 7535 entries, 0 to 7534
    Data columns (total 27 columns):
    INSTNM                7535 non-null object
    CITY                  7535 non-null object
    STABBR                7535 non-null object
    HBCU                  7164 non-null float64
    MENONLY               7164 non-null float64
    WOMENONLY             7164 non-null float64
    RELAFFIL              7535 non-null int64
    SATVRMID              1185 non-null float64
    SATMTMID              1196 non-null float64
    DISTANCEONLY          7164 non-null float64
    UGDS                  6874 non-null float64
    UGDS_WHITE            6874 non-null float64
    UGDS_BLACK            6874 non-null float64
    UGDS_HISP             6874 non-null float64
    UGDS_ASIAN            6874 non-null float64
    UGDS_AIAN             6874 non-null float64
    UGDS_NHPI             6874 non-null float64
    UGDS_2MOR             6874 non-null float64
    UGDS_NRA              6874 non-null float64
    UGDS_UNKN             6874 non-null float64
    PPTUG_EF              6853 non-null float64
    CURROPER              7535 non-null int64
    PCTPELL               6849 non-null float64
    PCTFLOAN              6849 non-null float64
    UG25ABV               6718 non-null float64
    MD_EARN_WNE_P10       6413 non-null object
    GRAD_DEBT_MDN_SUPP    7503 non-null object
    dtypes: float64(20), int64(2), object(5)
    memory usage: 1.6+ MB



```python
college.describe(include=[np.number]).T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <td>7535.0</td>
      <td>0.190975</td>
      <td>0.393096</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>SATVRMID</th>
      <td>1185.0</td>
      <td>522.819409</td>
      <td>68.578862</td>
      <td>290.0</td>
      <td>475.000000</td>
      <td>510.00000</td>
      <td>555.000000</td>
      <td>765.0000</td>
    </tr>
    <tr>
      <th>SATMTMID</th>
      <td>1196.0</td>
      <td>530.765050</td>
      <td>73.469767</td>
      <td>310.0</td>
      <td>482.000000</td>
      <td>520.00000</td>
      <td>565.000000</td>
      <td>785.0000</td>
    </tr>
    <tr>
      <th>DISTANCEONLY</th>
      <td>7164.0</td>
      <td>0.005583</td>
      <td>0.074519</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UGDS</th>
      <td>6874.0</td>
      <td>2356.837940</td>
      <td>5474.275871</td>
      <td>0.0</td>
      <td>117.000000</td>
      <td>412.50000</td>
      <td>1929.500000</td>
      <td>151558.0000</td>
    </tr>
    <tr>
      <th>UGDS_WHITE</th>
      <td>6874.0</td>
      <td>0.510207</td>
      <td>0.286958</td>
      <td>0.0</td>
      <td>0.267500</td>
      <td>0.55570</td>
      <td>0.747875</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>6874.0</td>
      <td>0.189997</td>
      <td>0.224587</td>
      <td>0.0</td>
      <td>0.036125</td>
      <td>0.10005</td>
      <td>0.257700</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>6874.0</td>
      <td>0.161635</td>
      <td>0.221854</td>
      <td>0.0</td>
      <td>0.027600</td>
      <td>0.07140</td>
      <td>0.198875</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>6874.0</td>
      <td>0.033544</td>
      <td>0.073777</td>
      <td>0.0</td>
      <td>0.002500</td>
      <td>0.01290</td>
      <td>0.032700</td>
      <td>0.9727</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>6874.0</td>
      <td>0.013813</td>
      <td>0.070196</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00260</td>
      <td>0.007300</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>6874.0</td>
      <td>0.004569</td>
      <td>0.033125</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.002500</td>
      <td>0.9983</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>6874.0</td>
      <td>0.023950</td>
      <td>0.031288</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01750</td>
      <td>0.033900</td>
      <td>0.5333</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>6874.0</td>
      <td>0.016086</td>
      <td>0.050172</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.011700</td>
      <td>0.9286</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>6874.0</td>
      <td>0.045181</td>
      <td>0.093440</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01430</td>
      <td>0.045400</td>
      <td>0.9027</td>
    </tr>
    <tr>
      <th>PPTUG_EF</th>
      <td>6853.0</td>
      <td>0.226639</td>
      <td>0.246470</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.15040</td>
      <td>0.376900</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>0.923291</td>
      <td>0.266146</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.357800</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.332900</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.241500</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.describe(include=[np.object, pd.Categorical]).T
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
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>INSTNM</th>
      <td>7535</td>
      <td>7535</td>
      <td>San Francisco State University</td>
      <td>1</td>
    </tr>
    <tr>
      <th>CITY</th>
      <td>7535</td>
      <td>2514</td>
      <td>New York</td>
      <td>87</td>
    </tr>
    <tr>
      <th>STABBR</th>
      <td>7535</td>
      <td>59</td>
      <td>CA</td>
      <td>773</td>
    </tr>
    <tr>
      <th>MD_EARN_WNE_P10</th>
      <td>6413</td>
      <td>598</td>
      <td>PrivacySuppressed</td>
      <td>822</td>
    </tr>
    <tr>
      <th>GRAD_DEBT_MDN_SUPP</th>
      <td>7503</td>
      <td>2038</td>
      <td>PrivacySuppressed</td>
      <td>1510</td>
    </tr>
  </tbody>
</table>
</div>



## There's more...


```python
with pd.option_context('display.max_rows', 5):
    display(college.describe(include=[np.number], 
                 percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>1%</th>
      <th>5%</th>
      <th>10%</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>90%</th>
      <th>95%</th>
      <th>99%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.3329</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>0.84752</td>
      <td>0.89792</td>
      <td>0.986368</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.0025</td>
      <td>0.0374</td>
      <td>0.0899</td>
      <td>0.2415</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>0.72666</td>
      <td>0.80000</td>
      <td>0.917383</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
<p>22 rows × 14 columns</p>
</div>



```python
college_dd = pd.read_csv('data/college_data_dictionary.csv')
```


```python
with pd.option_context('display.max_rows', 8):
    display(college_dd)
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
      <th>column_name</th>
      <th>description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>INSTNM</td>
      <td>Institution Name</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CITY</td>
      <td>City Location</td>
    </tr>
    <tr>
      <th>2</th>
      <td>STABBR</td>
      <td>State Abbreviation</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HBCU</td>
      <td>Historically Black College or University</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PCTFLOAN</td>
      <td>Percent Students with federal loan</td>
    </tr>
    <tr>
      <th>24</th>
      <td>UG25ABV</td>
      <td>Percent Students Older than 25</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MD_EARN_WNE_P10</td>
      <td>Median Earnings 10 years after enrollment</td>
    </tr>
    <tr>
      <th>26</th>
      <td>GRAD_DEBT_MDN_SUPP</td>
      <td>Median debt of completers</td>
    </tr>
  </tbody>
</table>
<p>27 rows × 2 columns</p>
</div>


# Reducing memory by changing data types


```python
college = pd.read_csv('data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]
col2.head()
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
      <th>RELAFFIL</th>
      <th>SATMTMID</th>
      <th>CURROPER</th>
      <th>INSTNM</th>
      <th>STABBR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>420.0</td>
      <td>1</td>
      <td>Alabama A &amp; M University</td>
      <td>AL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>565.0</td>
      <td>1</td>
      <td>University of Alabama at Birmingham</td>
      <td>AL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>NaN</td>
      <td>1</td>
      <td>Amridge University</td>
      <td>AL</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>590.0</td>
      <td>1</td>
      <td>University of Alabama in Huntsville</td>
      <td>AL</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>430.0</td>
      <td>1</td>
      <td>Alabama State University</td>
      <td>AL</td>
    </tr>
  </tbody>
</table>
</div>




```python
col2.dtypes
```




    RELAFFIL      int64
    SATMTMID    float64
    CURROPER      int64
    INSTNM       object
    STABBR       object
    dtype: object




```python
original_mem = col2.memory_usage(deep=True)
original_mem
```




    Index           80
    RELAFFIL     60280
    SATMTMID     60280
    CURROPER     60280
    INSTNM      660240
    STABBR      444565
    dtype: int64




```python
col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
```


```python
col2.dtypes
```




    RELAFFIL       int8
    SATMTMID    float64
    CURROPER      int64
    INSTNM       object
    STABBR       object
    dtype: object




```python
col2.select_dtypes(include=['object']).nunique()
```




    INSTNM    7535
    STABBR      59
    dtype: int64




```python
col2['STABBR'] = col2['STABBR'].astype('category')
col2.dtypes
```




    RELAFFIL        int8
    SATMTMID     float64
    CURROPER       int64
    INSTNM        object
    STABBR      category
    dtype: object




```python
new_mem = col2.memory_usage(deep=True)
new_mem
```




    Index           80
    RELAFFIL      7535
    SATMTMID     60280
    CURROPER     60280
    INSTNM      660699
    STABBR       13576
    dtype: int64




```python
new_mem / original_mem
```




    Index       1.000000
    RELAFFIL    0.125000
    SATMTMID    1.000000
    CURROPER    1.000000
    INSTNM      1.000695
    STABBR      0.030538
    dtype: float64



## There's more...


```python
college = pd.read_csv('data/college.csv')
```


```python
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)
```




    Index           80
    CURROPER     60280
    INSTNM      660240
    dtype: int64




```python
college.loc[0, 'CURROPER'] = 10000000
college.loc[0, 'INSTNM'] = college.loc[0, 'INSTNM'] + 'a'
# college.loc[1, 'INSTNM'] = college.loc[1, 'INSTNM'] + 'a'
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)
```




    Index           80
    CURROPER     60280
    INSTNM      660345
    dtype: int64




```python
college['MENONLY'].dtype
```




    dtype('float64')




```python
college['MENONLY'].astype('int8') # ValueError: Cannot convert non-finite values (NA or inf) to integer
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-26-98afc27c1701> in <module>()
    ----> 1 college['MENONLY'].astype('int8') # ValueError: Cannot convert non-finite values (NA or inf) to integer
    

    ~/anaconda3/lib/python3.6/site-packages/pandas/util/_decorators.py in wrapper(*args, **kwargs)
        116                 else:
        117                     kwargs[new_arg_name] = new_arg_value
    --> 118             return func(*args, **kwargs)
        119         return wrapper
        120     return _deprecate_kwarg


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py in astype(self, dtype, copy, errors, **kwargs)
       4002         # else, only a single dtype is given
       4003         new_data = self._data.astype(dtype=dtype, copy=copy, errors=errors,
    -> 4004                                      **kwargs)
       4005         return self._constructor(new_data).__finalize__(self)
       4006 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py in astype(self, dtype, **kwargs)
       3455 
       3456     def astype(self, dtype, **kwargs):
    -> 3457         return self.apply('astype', dtype=dtype, **kwargs)
       3458 
       3459     def convert(self, **kwargs):


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py in apply(self, f, axes, filter, do_integrity_check, consolidate, **kwargs)
       3322 
       3323             kwargs['mgr'] = self
    -> 3324             applied = getattr(b, f)(**kwargs)
       3325             result_blocks = _extend_blocks(applied, result_blocks)
       3326 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py in astype(self, dtype, copy, errors, values, **kwargs)
        542     def astype(self, dtype, copy=False, errors='raise', values=None, **kwargs):
        543         return self._astype(dtype, copy=copy, errors=errors, values=values,
    --> 544                             **kwargs)
        545 
        546     def _astype(self, dtype, copy=False, errors='raise', values=None,


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py in _astype(self, dtype, copy, errors, values, klass, mgr, **kwargs)
        623 
        624                 # _astype_nansafe works fine with 1-d only
    --> 625                 values = astype_nansafe(values.ravel(), dtype, copy=True)
        626                 values = values.reshape(self.shape)
        627 


    ~/anaconda3/lib/python3.6/site-packages/pandas/core/dtypes/cast.py in astype_nansafe(arr, dtype, copy)
        685 
        686         if not np.isfinite(arr).all():
    --> 687             raise ValueError('Cannot convert non-finite values (NA or inf) to '
        688                              'integer')
        689 


    ValueError: Cannot convert non-finite values (NA or inf) to integer



```python
college.describe(include=['int64', 'float64']).T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <td>7535.0</td>
      <td>0.190975</td>
      <td>0.393096</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>SATVRMID</th>
      <td>1185.0</td>
      <td>522.819409</td>
      <td>68.578862</td>
      <td>290.0</td>
      <td>475.000000</td>
      <td>510.00000</td>
      <td>555.000000</td>
      <td>7.650000e+02</td>
    </tr>
    <tr>
      <th>SATMTMID</th>
      <td>1196.0</td>
      <td>530.765050</td>
      <td>73.469767</td>
      <td>310.0</td>
      <td>482.000000</td>
      <td>520.00000</td>
      <td>565.000000</td>
      <td>7.850000e+02</td>
    </tr>
    <tr>
      <th>DISTANCEONLY</th>
      <td>7164.0</td>
      <td>0.005583</td>
      <td>0.074519</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS</th>
      <td>6874.0</td>
      <td>2356.837940</td>
      <td>5474.275871</td>
      <td>0.0</td>
      <td>117.000000</td>
      <td>412.50000</td>
      <td>1929.500000</td>
      <td>1.515580e+05</td>
    </tr>
    <tr>
      <th>UGDS_WHITE</th>
      <td>6874.0</td>
      <td>0.510207</td>
      <td>0.286958</td>
      <td>0.0</td>
      <td>0.267500</td>
      <td>0.55570</td>
      <td>0.747875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>6874.0</td>
      <td>0.189997</td>
      <td>0.224587</td>
      <td>0.0</td>
      <td>0.036125</td>
      <td>0.10005</td>
      <td>0.257700</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>6874.0</td>
      <td>0.161635</td>
      <td>0.221854</td>
      <td>0.0</td>
      <td>0.027600</td>
      <td>0.07140</td>
      <td>0.198875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>6874.0</td>
      <td>0.033544</td>
      <td>0.073777</td>
      <td>0.0</td>
      <td>0.002500</td>
      <td>0.01290</td>
      <td>0.032700</td>
      <td>9.727000e-01</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>6874.0</td>
      <td>0.013813</td>
      <td>0.070196</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00260</td>
      <td>0.007300</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>6874.0</td>
      <td>0.004569</td>
      <td>0.033125</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.002500</td>
      <td>9.983000e-01</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>6874.0</td>
      <td>0.023950</td>
      <td>0.031288</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01750</td>
      <td>0.033900</td>
      <td>5.333000e-01</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>6874.0</td>
      <td>0.016086</td>
      <td>0.050172</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.011700</td>
      <td>9.286000e-01</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>6874.0</td>
      <td>0.045181</td>
      <td>0.093440</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01430</td>
      <td>0.045400</td>
      <td>9.027000e-01</td>
    </tr>
    <tr>
      <th>PPTUG_EF</th>
      <td>6853.0</td>
      <td>0.226639</td>
      <td>0.246470</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.15040</td>
      <td>0.376900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>1328.063172</td>
      <td>115201.552429</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.000000e+07</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.357800</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.332900</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.241500</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.000000e+00</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.describe(include=[np.int64, np.float64]).T
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <td>7535.0</td>
      <td>0.190975</td>
      <td>0.393096</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>SATVRMID</th>
      <td>1185.0</td>
      <td>522.819409</td>
      <td>68.578862</td>
      <td>290.0</td>
      <td>475.000000</td>
      <td>510.00000</td>
      <td>555.000000</td>
      <td>7.650000e+02</td>
    </tr>
    <tr>
      <th>SATMTMID</th>
      <td>1196.0</td>
      <td>530.765050</td>
      <td>73.469767</td>
      <td>310.0</td>
      <td>482.000000</td>
      <td>520.00000</td>
      <td>565.000000</td>
      <td>7.850000e+02</td>
    </tr>
    <tr>
      <th>DISTANCEONLY</th>
      <td>7164.0</td>
      <td>0.005583</td>
      <td>0.074519</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS</th>
      <td>6874.0</td>
      <td>2356.837940</td>
      <td>5474.275871</td>
      <td>0.0</td>
      <td>117.000000</td>
      <td>412.50000</td>
      <td>1929.500000</td>
      <td>1.515580e+05</td>
    </tr>
    <tr>
      <th>UGDS_WHITE</th>
      <td>6874.0</td>
      <td>0.510207</td>
      <td>0.286958</td>
      <td>0.0</td>
      <td>0.267500</td>
      <td>0.55570</td>
      <td>0.747875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>6874.0</td>
      <td>0.189997</td>
      <td>0.224587</td>
      <td>0.0</td>
      <td>0.036125</td>
      <td>0.10005</td>
      <td>0.257700</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>6874.0</td>
      <td>0.161635</td>
      <td>0.221854</td>
      <td>0.0</td>
      <td>0.027600</td>
      <td>0.07140</td>
      <td>0.198875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>6874.0</td>
      <td>0.033544</td>
      <td>0.073777</td>
      <td>0.0</td>
      <td>0.002500</td>
      <td>0.01290</td>
      <td>0.032700</td>
      <td>9.727000e-01</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>6874.0</td>
      <td>0.013813</td>
      <td>0.070196</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00260</td>
      <td>0.007300</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>6874.0</td>
      <td>0.004569</td>
      <td>0.033125</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.002500</td>
      <td>9.983000e-01</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>6874.0</td>
      <td>0.023950</td>
      <td>0.031288</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01750</td>
      <td>0.033900</td>
      <td>5.333000e-01</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>6874.0</td>
      <td>0.016086</td>
      <td>0.050172</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.011700</td>
      <td>9.286000e-01</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>6874.0</td>
      <td>0.045181</td>
      <td>0.093440</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01430</td>
      <td>0.045400</td>
      <td>9.027000e-01</td>
    </tr>
    <tr>
      <th>PPTUG_EF</th>
      <td>6853.0</td>
      <td>0.226639</td>
      <td>0.246470</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.15040</td>
      <td>0.376900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>1328.063172</td>
      <td>115201.552429</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.000000e+07</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.357800</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.332900</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.241500</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.000000e+00</td>
    </tr>
  </tbody>
</table>
</div>




```python
college['RELAFFIL'] = college['RELAFFIL'].astype(np.int8)
```


```python
college.describe(include=['int', 'float']).T  # defaults to 64 bit int/floats
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>SATVRMID</th>
      <td>1185.0</td>
      <td>522.819409</td>
      <td>68.578862</td>
      <td>290.0</td>
      <td>475.000000</td>
      <td>510.00000</td>
      <td>555.000000</td>
      <td>7.650000e+02</td>
    </tr>
    <tr>
      <th>SATMTMID</th>
      <td>1196.0</td>
      <td>530.765050</td>
      <td>73.469767</td>
      <td>310.0</td>
      <td>482.000000</td>
      <td>520.00000</td>
      <td>565.000000</td>
      <td>7.850000e+02</td>
    </tr>
    <tr>
      <th>DISTANCEONLY</th>
      <td>7164.0</td>
      <td>0.005583</td>
      <td>0.074519</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS</th>
      <td>6874.0</td>
      <td>2356.837940</td>
      <td>5474.275871</td>
      <td>0.0</td>
      <td>117.000000</td>
      <td>412.50000</td>
      <td>1929.500000</td>
      <td>1.515580e+05</td>
    </tr>
    <tr>
      <th>UGDS_WHITE</th>
      <td>6874.0</td>
      <td>0.510207</td>
      <td>0.286958</td>
      <td>0.0</td>
      <td>0.267500</td>
      <td>0.55570</td>
      <td>0.747875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>6874.0</td>
      <td>0.189997</td>
      <td>0.224587</td>
      <td>0.0</td>
      <td>0.036125</td>
      <td>0.10005</td>
      <td>0.257700</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>6874.0</td>
      <td>0.161635</td>
      <td>0.221854</td>
      <td>0.0</td>
      <td>0.027600</td>
      <td>0.07140</td>
      <td>0.198875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>6874.0</td>
      <td>0.033544</td>
      <td>0.073777</td>
      <td>0.0</td>
      <td>0.002500</td>
      <td>0.01290</td>
      <td>0.032700</td>
      <td>9.727000e-01</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>6874.0</td>
      <td>0.013813</td>
      <td>0.070196</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00260</td>
      <td>0.007300</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>6874.0</td>
      <td>0.004569</td>
      <td>0.033125</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.002500</td>
      <td>9.983000e-01</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>6874.0</td>
      <td>0.023950</td>
      <td>0.031288</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01750</td>
      <td>0.033900</td>
      <td>5.333000e-01</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>6874.0</td>
      <td>0.016086</td>
      <td>0.050172</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.011700</td>
      <td>9.286000e-01</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>6874.0</td>
      <td>0.045181</td>
      <td>0.093440</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01430</td>
      <td>0.045400</td>
      <td>9.027000e-01</td>
    </tr>
    <tr>
      <th>PPTUG_EF</th>
      <td>6853.0</td>
      <td>0.226639</td>
      <td>0.246470</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.15040</td>
      <td>0.376900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>1328.063172</td>
      <td>115201.552429</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.000000e+07</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.357800</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.332900</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.241500</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.000000e+00</td>
    </tr>
  </tbody>
</table>
</div>




```python
college.describe(include=['number']).T  # also works as the default int/float are 64 bits
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>HBCU</th>
      <td>7164.0</td>
      <td>0.014238</td>
      <td>0.118478</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>MENONLY</th>
      <td>7164.0</td>
      <td>0.009213</td>
      <td>0.095546</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>WOMENONLY</th>
      <td>7164.0</td>
      <td>0.005304</td>
      <td>0.072642</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>RELAFFIL</th>
      <td>7535.0</td>
      <td>0.190975</td>
      <td>0.393096</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>SATVRMID</th>
      <td>1185.0</td>
      <td>522.819409</td>
      <td>68.578862</td>
      <td>290.0</td>
      <td>475.000000</td>
      <td>510.00000</td>
      <td>555.000000</td>
      <td>7.650000e+02</td>
    </tr>
    <tr>
      <th>SATMTMID</th>
      <td>1196.0</td>
      <td>530.765050</td>
      <td>73.469767</td>
      <td>310.0</td>
      <td>482.000000</td>
      <td>520.00000</td>
      <td>565.000000</td>
      <td>7.850000e+02</td>
    </tr>
    <tr>
      <th>DISTANCEONLY</th>
      <td>7164.0</td>
      <td>0.005583</td>
      <td>0.074519</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS</th>
      <td>6874.0</td>
      <td>2356.837940</td>
      <td>5474.275871</td>
      <td>0.0</td>
      <td>117.000000</td>
      <td>412.50000</td>
      <td>1929.500000</td>
      <td>1.515580e+05</td>
    </tr>
    <tr>
      <th>UGDS_WHITE</th>
      <td>6874.0</td>
      <td>0.510207</td>
      <td>0.286958</td>
      <td>0.0</td>
      <td>0.267500</td>
      <td>0.55570</td>
      <td>0.747875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_BLACK</th>
      <td>6874.0</td>
      <td>0.189997</td>
      <td>0.224587</td>
      <td>0.0</td>
      <td>0.036125</td>
      <td>0.10005</td>
      <td>0.257700</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_HISP</th>
      <td>6874.0</td>
      <td>0.161635</td>
      <td>0.221854</td>
      <td>0.0</td>
      <td>0.027600</td>
      <td>0.07140</td>
      <td>0.198875</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_ASIAN</th>
      <td>6874.0</td>
      <td>0.033544</td>
      <td>0.073777</td>
      <td>0.0</td>
      <td>0.002500</td>
      <td>0.01290</td>
      <td>0.032700</td>
      <td>9.727000e-01</td>
    </tr>
    <tr>
      <th>UGDS_AIAN</th>
      <td>6874.0</td>
      <td>0.013813</td>
      <td>0.070196</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00260</td>
      <td>0.007300</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UGDS_NHPI</th>
      <td>6874.0</td>
      <td>0.004569</td>
      <td>0.033125</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.002500</td>
      <td>9.983000e-01</td>
    </tr>
    <tr>
      <th>UGDS_2MOR</th>
      <td>6874.0</td>
      <td>0.023950</td>
      <td>0.031288</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01750</td>
      <td>0.033900</td>
      <td>5.333000e-01</td>
    </tr>
    <tr>
      <th>UGDS_NRA</th>
      <td>6874.0</td>
      <td>0.016086</td>
      <td>0.050172</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.011700</td>
      <td>9.286000e-01</td>
    </tr>
    <tr>
      <th>UGDS_UNKN</th>
      <td>6874.0</td>
      <td>0.045181</td>
      <td>0.093440</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.01430</td>
      <td>0.045400</td>
      <td>9.027000e-01</td>
    </tr>
    <tr>
      <th>PPTUG_EF</th>
      <td>6853.0</td>
      <td>0.226639</td>
      <td>0.246470</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.15040</td>
      <td>0.376900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>CURROPER</th>
      <td>7535.0</td>
      <td>1328.063172</td>
      <td>115201.552429</td>
      <td>0.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.000000</td>
      <td>1.000000e+07</td>
    </tr>
    <tr>
      <th>PCTPELL</th>
      <td>6849.0</td>
      <td>0.530643</td>
      <td>0.225544</td>
      <td>0.0</td>
      <td>0.357800</td>
      <td>0.52150</td>
      <td>0.712900</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>PCTFLOAN</th>
      <td>6849.0</td>
      <td>0.522211</td>
      <td>0.283616</td>
      <td>0.0</td>
      <td>0.332900</td>
      <td>0.58330</td>
      <td>0.745000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>UG25ABV</th>
      <td>6718.0</td>
      <td>0.410021</td>
      <td>0.228939</td>
      <td>0.0</td>
      <td>0.241500</td>
      <td>0.40075</td>
      <td>0.572275</td>
      <td>1.000000e+00</td>
    </tr>
  </tbody>
</table>
</div>




```python
college['MENONLY'] = college['MENONLY'].astype('float16')
college['RELAFFIL'] = college['RELAFFIL'].astype('int8')
```


```python
college.index = pd.Int64Index(college.index)
college.index.memory_usage()
```




    60280



# Selecting the smallest of the largest


```python
movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie2.head()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>7.9</td>
      <td>237000000.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>7.1</td>
      <td>300000000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>6.8</td>
      <td>245000000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>8.5</td>
      <td>250000000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>7.1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.nlargest(100, 'imdb_score').head()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2725</th>
      <td>Towering Inferno</td>
      <td>9.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1920</th>
      <td>The Shawshank Redemption</td>
      <td>9.3</td>
      <td>25000000.0</td>
    </tr>
    <tr>
      <th>3402</th>
      <td>The Godfather</td>
      <td>9.2</td>
      <td>6000000.0</td>
    </tr>
    <tr>
      <th>2779</th>
      <td>Dekalog</td>
      <td>9.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4312</th>
      <td>Kickboxer: Vengeance</td>
      <td>9.1</td>
      <td>17000000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4804</th>
      <td>Butterfly Girl</td>
      <td>8.7</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4801</th>
      <td>Children of Heaven</td>
      <td>8.5</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4706</th>
      <td>12 Angry Men</td>
      <td>8.9</td>
      <td>350000.0</td>
    </tr>
    <tr>
      <th>4550</th>
      <td>A Separation</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>The Other Dream Team</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
  </tbody>
</table>
</div>



# Selecting the largest of each group by sorting


```python
movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]
```


```python
movie2.sort_values('title_year', ascending=False).head()
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
      <th>title_year</th>
      <th>imdb_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3884</th>
      <td>The Veil</td>
      <td>2016.0</td>
      <td>4.7</td>
    </tr>
    <tr>
      <th>2375</th>
      <td>My Big Fat Greek Wedding 2</td>
      <td>2016.0</td>
      <td>6.1</td>
    </tr>
    <tr>
      <th>2794</th>
      <td>Miracles from Heaven</td>
      <td>2016.0</td>
      <td>6.8</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Independence Day: Resurgence</td>
      <td>2016.0</td>
      <td>5.5</td>
    </tr>
    <tr>
      <th>153</th>
      <td>Kung Fu Panda 3</td>
      <td>2016.0</td>
      <td>7.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie3 = movie2.sort_values(['title_year','imdb_score'], ascending=False)
movie3.head()
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
      <th>title_year</th>
      <th>imdb_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4312</th>
      <td>Kickboxer: Vengeance</td>
      <td>2016.0</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>4277</th>
      <td>A Beginner's Guide to Snuff</td>
      <td>2016.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>3798</th>
      <td>Airlift</td>
      <td>2016.0</td>
      <td>8.5</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Captain America: Civil War</td>
      <td>2016.0</td>
      <td>8.2</td>
    </tr>
    <tr>
      <th>98</th>
      <td>Godzilla Resurgence</td>
      <td>2016.0</td>
      <td>8.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie_top_year = movie3.drop_duplicates(subset='title_year')
movie_top_year.head()
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
      <th>title_year</th>
      <th>imdb_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4312</th>
      <td>Kickboxer: Vengeance</td>
      <td>2016.0</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>3745</th>
      <td>Running Forever</td>
      <td>2015.0</td>
      <td>8.6</td>
    </tr>
    <tr>
      <th>4369</th>
      <td>Queen of the Mountains</td>
      <td>2014.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>3935</th>
      <td>Batman: The Dark Knight Returns, Part 2</td>
      <td>2013.0</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>2012.0</td>
      <td>8.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie4 = movie[['movie_title', 'title_year', 'content_rating', 'budget']]
movie4_sorted = movie4.sort_values(['title_year', 'content_rating', 'budget'], 
                                   ascending=[False, False, True])
movie4_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10)
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
      <th>title_year</th>
      <th>content_rating</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4026</th>
      <td>Compadres</td>
      <td>2016.0</td>
      <td>R</td>
      <td>3000000.0</td>
    </tr>
    <tr>
      <th>4658</th>
      <td>Fight to the Finish</td>
      <td>2016.0</td>
      <td>PG-13</td>
      <td>150000.0</td>
    </tr>
    <tr>
      <th>4661</th>
      <td>Rodeo Girl</td>
      <td>2016.0</td>
      <td>PG</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>3252</th>
      <td>The Wailing</td>
      <td>2016.0</td>
      <td>Not Rated</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4659</th>
      <td>Alleluia! The Devil's Carnival</td>
      <td>2016.0</td>
      <td>NaN</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>4731</th>
      <td>Bizarre</td>
      <td>2015.0</td>
      <td>Unrated</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>812</th>
      <td>The Ridiculous 6</td>
      <td>2015.0</td>
      <td>TV-14</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4831</th>
      <td>The Gallows</td>
      <td>2015.0</td>
      <td>R</td>
      <td>100000.0</td>
    </tr>
    <tr>
      <th>4825</th>
      <td>Romantic Schemer</td>
      <td>2015.0</td>
      <td>PG-13</td>
      <td>125000.0</td>
    </tr>
    <tr>
      <th>3796</th>
      <td>R.L. Stine's Monsterville: The Cabinet of Souls</td>
      <td>2015.0</td>
      <td>PG</td>
      <td>4400000.0</td>
    </tr>
  </tbody>
</table>
</div>



# Replicating nlargest with sort_values


```python
movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
movie_smallest_largest
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4804</th>
      <td>Butterfly Girl</td>
      <td>8.7</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4801</th>
      <td>Children of Heaven</td>
      <td>8.5</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4706</th>
      <td>12 Angry Men</td>
      <td>8.9</td>
      <td>350000.0</td>
    </tr>
    <tr>
      <th>4550</th>
      <td>A Separation</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>The Other Dream Team</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.sort_values('imdb_score', ascending=False).head(100).head()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2725</th>
      <td>Towering Inferno</td>
      <td>9.5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1920</th>
      <td>The Shawshank Redemption</td>
      <td>9.3</td>
      <td>25000000.0</td>
    </tr>
    <tr>
      <th>3402</th>
      <td>The Godfather</td>
      <td>9.2</td>
      <td>6000000.0</td>
    </tr>
    <tr>
      <th>2779</th>
      <td>Dekalog</td>
      <td>9.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4312</th>
      <td>Kickboxer: Vengeance</td>
      <td>9.1</td>
      <td>17000000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4815</th>
      <td>A Charlie Brown Christmas</td>
      <td>8.4</td>
      <td>150000.0</td>
    </tr>
    <tr>
      <th>4801</th>
      <td>Children of Heaven</td>
      <td>8.5</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4804</th>
      <td>Butterfly Girl</td>
      <td>8.7</td>
      <td>180000.0</td>
    </tr>
    <tr>
      <th>4706</th>
      <td>12 Angry Men</td>
      <td>8.9</td>
      <td>350000.0</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>The Other Dream Team</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.nlargest(100, 'imdb_score').tail()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4023</th>
      <td>Oldboy</td>
      <td>8.4</td>
      <td>3000000.0</td>
    </tr>
    <tr>
      <th>4163</th>
      <td>To Kill a Mockingbird</td>
      <td>8.4</td>
      <td>2000000.0</td>
    </tr>
    <tr>
      <th>4395</th>
      <td>Reservoir Dogs</td>
      <td>8.4</td>
      <td>1200000.0</td>
    </tr>
    <tr>
      <th>4550</th>
      <td>A Separation</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>The Other Dream Team</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie2.sort_values('imdb_score', ascending=False).head(100).tail()
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
      <th>imdb_score</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3799</th>
      <td>Anne of Green Gables</td>
      <td>8.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3777</th>
      <td>Requiem for a Dream</td>
      <td>8.4</td>
      <td>4500000.0</td>
    </tr>
    <tr>
      <th>3935</th>
      <td>Batman: The Dark Knight Returns, Part 2</td>
      <td>8.4</td>
      <td>3500000.0</td>
    </tr>
    <tr>
      <th>4636</th>
      <td>The Other Dream Team</td>
      <td>8.4</td>
      <td>500000.0</td>
    </tr>
    <tr>
      <th>2455</th>
      <td>Aliens</td>
      <td>8.4</td>
      <td>18500000.0</td>
    </tr>
  </tbody>
</table>
</div>



# Calculating a trailing stop order price


```python
import pandas_datareader as pdr
```

### Note: pandas_datareader issues
pandas_datareader can have issues when the source is 'google'. It can also read from Yahoo! finance. Try switching it to 'yahoo'


```python
tsla = pdr.DataReader('tsla', data_source='yahoo',start='2017-1-1')
tsla.head(8)
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
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
    <tr>
      <th>Date</th>
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
      <th>2017-01-03</th>
      <td>214.860001</td>
      <td>220.330002</td>
      <td>210.960007</td>
      <td>216.990005</td>
      <td>216.990005</td>
      <td>5923300</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>214.750000</td>
      <td>228.000000</td>
      <td>214.309998</td>
      <td>226.990005</td>
      <td>226.990005</td>
      <td>11213500</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>226.419998</td>
      <td>227.479996</td>
      <td>221.949997</td>
      <td>226.750000</td>
      <td>226.750000</td>
      <td>5911700</td>
    </tr>
    <tr>
      <th>2017-01-06</th>
      <td>226.929993</td>
      <td>230.309998</td>
      <td>225.449997</td>
      <td>229.009995</td>
      <td>229.009995</td>
      <td>5527900</td>
    </tr>
    <tr>
      <th>2017-01-09</th>
      <td>228.970001</td>
      <td>231.919998</td>
      <td>228.000000</td>
      <td>231.279999</td>
      <td>231.279999</td>
      <td>3957000</td>
    </tr>
    <tr>
      <th>2017-01-10</th>
      <td>232.000000</td>
      <td>232.000000</td>
      <td>226.889999</td>
      <td>229.869995</td>
      <td>229.869995</td>
      <td>3660000</td>
    </tr>
    <tr>
      <th>2017-01-11</th>
      <td>229.070007</td>
      <td>229.979996</td>
      <td>226.679993</td>
      <td>229.729996</td>
      <td>229.729996</td>
      <td>3650800</td>
    </tr>
    <tr>
      <th>2017-01-12</th>
      <td>229.059998</td>
      <td>230.699997</td>
      <td>225.580002</td>
      <td>229.589996</td>
      <td>229.589996</td>
      <td>3790200</td>
    </tr>
  </tbody>
</table>
</div>




```python
tsla_close = tsla['Close']
```


```python
tsla_cummax = tsla_close.cummax()
tsla_cummax.head(8)
```




    Date
    2017-01-03    216.990005
    2017-01-04    226.990005
    2017-01-05    226.990005
    2017-01-06    229.009995
    2017-01-09    231.279999
    2017-01-10    231.279999
    2017-01-11    231.279999
    2017-01-12    231.279999
    Name: Close, dtype: float64




```python
tsla_trailing_stop = tsla_cummax * .9
tsla_trailing_stop.head(8)
```




    Date
    2017-01-03    195.291004
    2017-01-04    204.291004
    2017-01-05    204.291004
    2017-01-06    206.108996
    2017-01-09    208.151999
    2017-01-10    208.151999
    2017-01-11    208.151999
    2017-01-12    208.151999
    Name: Close, dtype: float64



## There's more...


```python
def set_trailing_loss(symbol, purchase_date, perc):
    close = pdr.DataReader(symbol, 'yahoo', start=purchase_date)['Close']
    return close.cummax() * perc
```


```python
msft_trailing_stop = set_trailing_loss('msft', '2017-6-1', .85)
msft_trailing_stop.head()
```




    Date
    2017-06-01    59.584998
    2017-06-02    60.996002
    2017-06-05    61.437999
    2017-06-06    61.641997
    2017-06-07    61.641997
    Name: Close, dtype: float64




```python

```
