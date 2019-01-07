# Chapter 4 - Pandas Foundation pada buku Pandas Cookbook
#### download data yang akan digunakan pada [Pandas-Cookbook](https://github.com/PacktPublishing/Pandas-Cookbook)
#### data yang saya dowload saya letakkan pada "/data"

# Pembahasan Praktik :
## Chapter 4
### Selecting Series Data
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']
print(city.head())
print(city.iloc[3])
print(city.iloc[[10,20,30]])
print(city.iloc[4:50:10])
print(city.loc['Heritage Christian University'])

np.random.seed(1)
labels = list(np.random.choice(city.index, 4))
print(labels)
print(city.loc[labels])
print(city.loc['Alabama State University':'Reid State Technical College':10])
print(city['Alabama State University':'Reid State Technical College':10])
print(city.iloc[[3]])
print(city.loc['Reid State Technical College':'Alabama State University':10])
print(city.loc['Reid State Technical College':'Alabama State University':-10])
```
#### Output
```
INSTNM
Alabama A & M University                   Normal
University of Alabama at Birmingham    Birmingham
Amridge University                     Montgomery
University of Alabama in Huntsville    Huntsville
Alabama State University               Montgomery
Name: CITY, dtype: object

Huntsville
INSTNM
Birmingham Southern College                            Birmingham
George C Wallace State Community College-Hanceville    Hanceville
Judson College                                             Marion
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

Florence
['Northwest HVAC/R Training Center', 'California State University-Dominguez Hills', 'Lower Columbia College', 'Southwest Acupuncture College-Boulder']
INSTNM
Northwest HVAC/R Training Center                Spokane
California State University-Dominguez Hills      Carson
Lower Columbia College                         Longview
Southwest Acupuncture College-Boulder           Boulder
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

INSTNM
Alabama State University              Montgomery
Enterprise State Community College    Enterprise
Heritage Christian University           Florence
Marion Military Institute                 Marion
Reid State Technical College           Evergreen
Name: CITY, dtype: object

INSTNM
University of Alabama in Huntsville    Huntsville
Name: CITY, dtype: object

Series([], Name: CITY, dtype: object)
INSTNM
Reid State Technical College           Evergreen
Marion Military Institute                 Marion
Heritage Christian University           Florence
Enterprise State Community College    Enterprise
Alabama State University              Montgomery
Name: CITY, dtype: object
```

### Selecting DataFrame Rows
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.head())

pd.options.display.max_rows = 6
print(college.iloc[60])
print(college.loc['University of Alaska Anchorage'])
print(college.iloc[[60, 99, 3]])

labels = ['University of Alaska Anchorage',
          'International Academy of Hair Design',
          'University of Alabama in Huntsville']
print(college.loc[labels])
print(college.iloc[99:102])

start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
print(college.loc[start:stop])
print(college.iloc[[60, 99, 3]].index.tolist())
```

#### Output
```
                                           CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                        ...
Alabama A & M University                 Normal     AL   1.0      0.0         ...            0.8284   0.1049            30300               33888
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0         ...            0.5214   0.2422            39700             21941.5
Amridge University                   Montgomery     AL   0.0      0.0         ...            0.7795   0.8540            40100               23370
University of Alabama in Huntsville  Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
Alabama State University             Montgomery     AL   1.0      0.0         ...            0.7554   0.1270            26600             33118.5
[5 rows x 26 columns]

CITY                  Anchorage
STABBR                       AK
HBCU                          0
                        ...
UG25ABV                  0.4386
MD_EARN_WNE_P10           42500
GRAD_DEBT_MDN_SUPP      19449.5
Name: University of Alaska Anchorage, Length: 26, dtype: object

CITY                  Anchorage
STABBR                       AK
HBCU                          0
                        ...
UG25ABV                  0.4386
MD_EARN_WNE_P10           42500
GRAD_DEBT_MDN_SUPP      19449.5
Name: University of Alaska Anchorage, Length: 26, dtype: object

                                            CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                         ...
University of Alaska Anchorage         Anchorage     AK   0.0      0.0         ...            0.2647   0.4386            42500             19449.5
International Academy of Hair Design       Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
University of Alabama in Huntsville   Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
[3 rows x 26 columns]

                                            CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                         ...
University of Alaska Anchorage         Anchorage     AK   0.0      0.0         ...            0.2647   0.4386            42500             19449.5
International Academy of Hair Design       Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
University of Alabama in Huntsville   Huntsville     AL   0.0      0.0         ...            0.4596   0.2640            45500               24097
[3 rows x 26 columns]

                                         CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                      ...
International Academy of Hair Design    Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
GateWay Community College             Phoenix     AZ   0.0      0.0         ...            0.2189   0.5832            29800                7283
Mesa Community College                   Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
[3 rows x 26 columns]

                                         CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                      ...
International Academy of Hair Design    Tempe     AZ   0.0      0.0         ...            0.7346   0.3905            22200               10556
GateWay Community College             Phoenix     AZ   0.0      0.0         ...            0.2189   0.5832            29800                7283
Mesa Community College                   Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
[3 rows x 26 columns]

['University of Alaska Anchorage', 'International Academy of Hair Design', 'University of Alabama in Huntsville']
```

### Selecting DataFrame rows and columns simultaneously
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
print(college.iloc[:3, :4])
print(college.loc[:'Amridge University', :'MENONLY'])
print(college.iloc[:, [4,6]].head())
print(college.loc[:, ['WOMENONLY', 'SATVRMID']])
print(college.iloc[[100, 200], [7, 15]])

rows = ['GateWay Community College', 'American Baptist Seminary of the West']
columns = ['SATMTMID', 'UGDS_NHPI']
print(college.loc[rows, columns])
print(college.iloc[5, -4])
print(college.loc['The University of Alabama', 'PCTFLOAN'])
print(college.iloc[90:80:-2, 5])

start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
print(college.loc[start:stop:-2, 'RELAFFIL'])

```

#### Output
```
                                           CITY STABBR  HBCU  MENONLY
INSTNM
Alabama A & M University                 Normal     AL   1.0      0.0
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0
Amridge University                   Montgomery     AL   0.0      0.0
                                           CITY STABBR  HBCU  MENONLY

INSTNM
Alabama A & M University                 Normal     AL   1.0      0.0
University of Alabama at Birmingham  Birmingham     AL   0.0      0.0
Amridge University                   Montgomery     AL   0.0      0.0
                                     WOMENONLY  SATVRMID

INSTNM
Alabama A & M University                   0.0     424.0
University of Alabama at Birmingham        0.0     570.0
Amridge University                         0.0       NaN
University of Alabama in Huntsville        0.0     595.0
Alabama State University                   0.0     425.0

                                                    WOMENONLY  SATVRMID
INSTNM
Alabama A & M University                                  0.0     424.0
University of Alabama at Birmingham                       0.0     570.0
Amridge University                                        0.0       NaN
University of Alabama in Huntsville                       0.0     595.0
Alabama State University                                  0.0     425.0
The University of Alabama                                 0.0     555.0
Central Alabama Community College                         0.0       NaN
Athens State University                                   0.0       NaN
Auburn University at Montgomery                           0.0     486.0
Auburn University                                         0.0     575.0
Birmingham Southern College                               0.0     560.0
Chattahoochee Valley Community College                    0.0       NaN
Concordia College Alabama                                 0.0     420.0
South University-Montgomery                               0.0       NaN
Enterprise State Community College                        0.0       NaN
James H Faulkner State Community College                  0.0       NaN
Faulkner University                                       0.0       NaN
Gadsden State Community College                           0.0       NaN
New Beginning College of Cosmetology                      0.0       NaN
George C Wallace State Community College-Dothan           0.0       NaN
George C Wallace State Community College-Hancev...        0.0       NaN
George C Wallace State Community College-Selma            0.0       NaN
Herzing University-Birmingham                             0.0       NaN
Huntingdon College                                        0.0     510.0
Heritage Christian University                             0.0       NaN
J F Drake State Community and Technical College           0.0       NaN
Jacksonville State University                             0.0     495.0
Jefferson Davis Community College                         0.0       NaN
Jefferson State Community College                         0.0       NaN
John C Calhoun State Community College                    0.0       NaN
...                                                       ...       ...
Strayer University-Lawrenceville                          NaN       NaN
Strayer University-Piscataway                             NaN       NaN
Utah County Campus                                        NaN       NaN
L'esprit Academy - Royal Oak                              NaN       NaN
National Career Institute - Jersey City Branch            NaN       NaN
Strayer University-Cobb Campus                            NaN       NaN
Strayer University-Morrow Campus                          NaN       NaN
Strayer University-Roswell Campus                         NaN       NaN
Strayer University-Douglasville Campus                    NaN       NaN
Strayer University-Lithonia Campus                        NaN       NaN
Strayer University-Savannah Campus                        NaN       NaN
Strayer University-Augusta Campus                         NaN       NaN
Strayer University-Columbus                               NaN       NaN
Strayer University-Columbia Campus                        NaN       NaN
Strayer University-Charleston Campus                      NaN       NaN
Strayer University-Irving                                 NaN       NaN
Strayer University-Katy                                   NaN       NaN
Strayer University-Northwest Houston                      NaN       NaN
Strayer University-Plano                                  NaN       NaN
Strayer University-Cedar Hill                             NaN       NaN
Strayer University-North Dallas                           NaN       NaN
Strayer University-San Antonio                            NaN       NaN
Strayer University-Stafford                               NaN       NaN
WestMed College - Merced                                  NaN       NaN
Vantage College                                           NaN       NaN
SAE Institute of Technology  San Francisco                NaN       NaN
Rasmussen College - Overland Park                         NaN       NaN
National Personal Training Institute of Cleveland         NaN       NaN
Bay Area Medical Academy - San Jose Satellite L...        NaN       NaN
Excel Learning Center-San Antonio South                   NaN       NaN
[7535 rows x 2 columns]

                                       SATMTMID  UGDS_NHPI
INSTNM
GateWay Community College                   NaN     0.0029
American Baptist Seminary of the West       NaN        NaN

                                       SATMTMID  UGDS_NHPI
INSTNM
GateWay Community College                   NaN     0.0029
American Baptist Seminary of the West       NaN        NaN
0.401
0.401

INSTNM
Empire Beauty School-Flagstaff     0
Charles of Italy Beauty College    0
Central Arizona College            0
University of Arizona              0
Arizona State University-Tempe     0
Name: RELAFFIL, dtype: int64

INSTNM
Empire Beauty School-Flagstaff     0
Charles of Italy Beauty College    0
Central Arizona College            0
University of Arizona              0
Arizona State University-Tempe     0
Name: RELAFFIL, dtype: int64
```

### Selecting data with both integers and labels
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
print(col_start, col_end)
print(college.iloc[:5, col_start:col_end])

row_start = college.index[10]
row_end = college.index[15]
print(college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN'])
```

#### Output
```
(10, 19)

                                     UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN
INSTNM
Alabama A & M University                 0.0333      0.9353     0.0055      0.0019     0.0024     0.0019     0.0000    0.0059     0.0138
University of Alabama at Birmingham      0.5922      0.2600     0.0283      0.0518     0.0022     0.0007     0.0368    0.0179     0.0100
Amridge University                       0.2990      0.4192     0.0069      0.0034     0.0000     0.0000     0.0000    0.0000     0.2715
University of Alabama in Huntsville      0.6988      0.1255     0.0382      0.0376     0.0143     0.0002     0.0172    0.0332     0.0350
Alabama State University                 0.0158      0.9208     0.0121      0.0019     0.0010     0.0006     0.0098    0.0243     0.0137

                                          UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN
INSTNM
Birmingham Southern College                   0.7983      0.1102     0.0195      0.0517     0.0102     0.0000     0.0051    0.0000     0.0051
Chattahoochee Valley Community College        0.4661      0.4372     0.0492      0.0127     0.0023     0.0035     0.0151    0.0000     0.0139
Concordia College Alabama                     0.0280      0.8758     0.0373      0.0093     0.0000     0.0000     0.0031    0.0466     0.0000
South University-Montgomery                   0.3046      0.6054     0.0153      0.0153     0.0153     0.0096     0.0000    0.0019     0.0326
Enterprise State Community College            0.6408      0.2435     0.0509      0.0202     0.0081     0.0029     0.0254    0.0012     0.0069
James H Faulkner State Community College      0.6979      0.2259     0.0320      0.0084     0.0177     0.0014     0.0152    0.0007     0.0009
```

### Speeding up scalar selection
```python
import pandas as pd
import numpy as np
from IPython import InteractiveShell

inter = InteractiveShell()

college = pd.read_csv('data/college.csv', index_col='INSTNM')
cn = 'Texas A & M University-College Station'
print(college.loc[cn, 'UGDS_WHITE'])
print(college.at[cn, 'UGDS_WHITE'])
print(inter.get_ipython().run_line_magic('timeit', "college.loc[cn, 'UGDS_WHITE']"))
print(inter.get_ipython().run_line_magic('timeit', "college.at[cn, 'UGDS_WHITE']"))

row_num = college.index.get_loc(cn)
col_num = college.columns.get_loc('UGDS_WHITE')
print(row_num, col_num)

print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[row_num, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iloc[5, col_num]'))
print(inter.get_ipython().run_line_magic('timeit', 'college.iat[5, col_num]'))

state = college['STABBR']
print(state.iat[1000])
print(state.at['Stanford University'])
```

#### Output
```
0.6609999999999999
0.6609999999999999
42.9 µs ± 9.91 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
21.1 µs ± 1.61 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
3765 10
45.4 µs ± 8.26 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
22.2 µs ± 1.06 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
46.9 µs ± 10 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
31.6 µs ± 6.83 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
None
IL
CA
```

### Slicing rows lazily
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
city = college['CITY']

print(college[10:20:2])
print(city[10:20:2])
print(college.index[4001])

start = 'Mesa Community College'
stop = 'Spokane Community College'
print(college[start:stop:1500])
print(city[start:stop:1500])
# print(college[:10, ['CITY', 'STABBR']])

first_ten_instnm = college.index[:10]
print(college.loc[first_ten_instnm, ['CITY', 'STABBR']])
```

#### Output
```
                                             CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                          ...
Birmingham Southern College            Birmingham     AL   0.0      0.0         ...            0.4809   0.0152            44200               27000
Concordia College Alabama                   Selma     AL   1.0      0.0         ...            0.9333   0.2367            19900   PrivacySuppressed
Enterprise State Community College     Enterprise     AL   0.0      0.0         ...            0.2263   0.3399            24600                8273
Faulkner University                    Montgomery     AL   0.0      0.0         ...            0.7253   0.4589            37200               22000
New Beginning College of Cosmetology  Albertville     AL   0.0      0.0         ...            0.8553   0.3933              NaN                5500
[5 rows x 26 columns]

INSTNM
Birmingham Southern College              Birmingham
Concordia College Alabama                     Selma
Enterprise State Community College       Enterprise
Faulkner University                      Montgomery
New Beginning College of Cosmetology    Albertville
Name: CITY, dtype: object

Spokane Community College

                                                CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV  MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                             ...
Mesa Community College                          Mesa     AZ   0.0      0.0         ...            0.2207   0.4010            35200                8000
Hair Academy Inc-New Carrollton       New Carrollton     MD   0.0      0.0         ...            1.0000   0.5882            15200                9666
National College of Natural Medicine        Portland     OR   0.0      0.0         ...               NaN      NaN              NaN   PrivacySuppressed
[3 rows x 26 columns]

INSTNM
Mesa Community College                            Mesa
Hair Academy Inc-New Carrollton         New Carrollton
National College of Natural Medicine          Portland
Name: CITY, dtype: object

                                               CITY STABBR
INSTNM
Alabama A & M University                     Normal     AL
University of Alabama at Birmingham      Birmingham     AL
Amridge University                       Montgomery     AL
University of Alabama in Huntsville      Huntsville     AL
Alabama State University                 Montgomery     AL
The University of Alabama                Tuscaloosa     AL
Central Alabama Community College    Alexander City     AL
Athens State University                      Athens     AL
Auburn University at Montgomery          Montgomery     AL
Auburn University                            Auburn     AL
```

### Slicing lexicographically
```python
import pandas as pd
import numpy as np


college = pd.read_csv('data/college.csv', index_col='INSTNM')
# print(college.loc['Sp':'Su'])
college = college.sort_index()
print(college.head())

pd.options.display.max_rows = 6
print(college.loc['Sp':'Su'])

college = college.sort_index(ascending=False)
print(college.index.is_monotonic_decreasing)
print(college.loc['E':'B'])
print(college.loc['E':'B'])
```

#### Output
```
                                                           CITY STABBR  HBCU         ...          UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
A & W Healthcare Educators                          New Orleans     LA   0.0         ...           0.6667                NaN             19022.5
A T Still University of Health Sciences              Kirksville     MO   0.0         ...              NaN             219800   PrivacySuppressed
ABC Beauty Academy                                      Garland     TX   0.0         ...           0.8286                NaN   PrivacySuppressed
ABC Beauty College Inc                              Arkadelphia     AR   0.0         ...           0.4688  PrivacySuppressed               16500
AI Miami International University of Art and De...        Miami     FL   0.0         ...           0.3262              29900               31000
[5 rows x 26 columns]

                                                 CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                              ...
Spa Tech Institute-Ipswich                    Ipswich     MA   0.0      0.0         ...            0.3906   0.7907              21500                6333
Spa Tech Institute-Plymouth                  Plymouth     MA   0.0      0.0         ...            0.4266   0.6250              21500                6333
Spa Tech Institute-Westboro                  Westboro     MA   0.0      0.0         ...            0.4545   0.6882              21500                6333
...                                               ...    ...   ...      ...         ...               ...      ...                ...                 ...
Stylemaster College of Hair Design           Longview     WA   0.0      0.0         ...            0.7024   0.4510              17000               13320
Styles and Profiles Beauty College             Selmer     TN   0.0      0.0         ...            0.7955   0.2400  PrivacySuppressed   PrivacySuppressed
Styletrends Barber and Hairstyling Academy  Rock Hill     SC   0.0      0.0         ...            1.0000   0.3529  PrivacySuppressed              9495.5
[201 rows x 26 columns]

True

                                                  CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
Dyersburg State Community College            Dyersburg     TN   0.0      0.0         ...            0.2493   0.3097              26800                7475
Dutchess Community College                Poughkeepsie     NY   0.0      0.0         ...            0.1936   0.1806              32500               10250
Dutchess BOCES-Practical Nursing Program  Poughkeepsie     NY   0.0      0.0         ...            0.6275   0.5430              36500                9500
...                                                ...    ...   ...      ...         ...               ...      ...                ...                 ...
BJ's Beauty & Barber College                    Auburn     WA   0.0      0.0         ...            0.6154   0.2917                NaN   PrivacySuppressed
BIR Training Center                            Chicago     IL   0.0      0.0         ...            0.6998   0.6741  PrivacySuppressed               15394
B M Spurr School of Practical Nursing        Glen Dale     WV   0.0      0.0         ...            0.0000   0.4444  PrivacySuppressed   PrivacySuppressed
[1411 rows x 26 columns]

                                                  CITY STABBR  HBCU  MENONLY         ...          PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  GRAD_DEBT_MDN_SUPP
INSTNM                                                                               ...
Dyersburg State Community College            Dyersburg     TN   0.0      0.0         ...            0.2493   0.3097              26800                7475
Dutchess Community College                Poughkeepsie     NY   0.0      0.0         ...            0.1936   0.1806              32500               10250
Dutchess BOCES-Practical Nursing Program  Poughkeepsie     NY   0.0      0.0         ...            0.6275   0.5430              36500                9500
...                                                ...    ...   ...      ...         ...               ...      ...                ...                 ...
BJ's Beauty & Barber College                    Auburn     WA   0.0      0.0         ...            0.6154   0.2917                NaN   PrivacySuppressed
BIR Training Center                            Chicago     IL   0.0      0.0         ...            0.6998   0.6741  PrivacySuppressed               15394
B M Spurr School of Practical Nursing        Glen Dale     WV   0.0      0.0         ...            0.0000   0.4444  PrivacySuppressed   PrivacySuppressed
[1411 rows x 26 columns]
```

## Bab 5 - Boolean Indexing
### Calculating boolean statistics
```python
import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print(movie.head())

movie_2_hours = movie['duration'] > 120
print(movie_2_hours.head(10))
print(movie_2_hours.sum())
print(movie_2_hours.mean())
print(movie_2_hours.describe())
print(movie['duration'].dropna().gt(120).mean())
print(movie_2_hours.value_counts(normalize=True))

actors = movie[['actor_1_facebook_likes', 'actor_2_facebook_likes']].dropna()
print((actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']).mean())
```

#### Output
```
                                            color      director_name  \
movie_title
Avatar                                      Color      James Cameron
Pirates of the Caribbean: At World's End    Color     Gore Verbinski
Spectre                                     Color         Sam Mendes
The Dark Knight Rises                       Color  Christopher Nolan
Star Wars: Episode VII - The Force Awakens    NaN        Doug Walker

                                            num_critic_for_reviews  duration  \
movie_title
Avatar                                                       723.0     178.0
Pirates of the Caribbean: At World's End                     302.0     169.0
Spectre                                                      602.0     148.0
The Dark Knight Rises                                        813.0     164.0
Star Wars: Episode VII - The Force Awakens                     NaN       NaN

                                            director_facebook_likes  \
movie_title
Avatar                                                          0.0
Pirates of the Caribbean: At World's End                      563.0
Spectre                                                         0.0
The Dark Knight Rises                                       22000.0
Star Wars: Episode VII - The Force Awakens                    131.0

                                            actor_3_facebook_likes  \
movie_title
Avatar                                                       855.0
Pirates of the Caribbean: At World's End                    1000.0
Spectre                                                      161.0
The Dark Knight Rises                                      23000.0
Star Wars: Episode VII - The Force Awakens                     NaN

                                                actor_2_name  \
movie_title
Avatar                                      Joel David Moore
Pirates of the Caribbean: At World's End       Orlando Bloom
Spectre                                         Rory Kinnear
The Dark Knight Rises                         Christian Bale
Star Wars: Episode VII - The Force Awakens        Rob Walker

                                            actor_1_facebook_likes  \
movie_title
Avatar                                                      1000.0
Pirates of the Caribbean: At World's End                   40000.0
Spectre                                                    11000.0
The Dark Knight Rises                                      27000.0
Star Wars: Episode VII - The Force Awakens                   131.0

                                                  gross  \
movie_title
Avatar                                      760505847.0
Pirates of the Caribbean: At World's End    309404152.0
Spectre                                     200074175.0
The Dark Knight Rises                       448130642.0
Star Wars: Episode VII - The Force Awakens          NaN

                                                                     genres  \
movie_title
Avatar                                      Action|Adventure|Fantasy|Sci-Fi
Pirates of the Caribbean: At World's End           Action|Adventure|Fantasy
Spectre                                           Action|Adventure|Thriller
The Dark Knight Rises                                       Action|Thriller
Star Wars: Episode VII - The Force Awakens                      Documentary

                                               actor_1_name  num_voted_users  \
movie_title
Avatar                                          CCH Pounder           886204
Pirates of the Caribbean: At World's End        Johnny Depp           471220
Spectre                                     Christoph Waltz           275868
The Dark Knight Rises                             Tom Hardy          1144337
Star Wars: Episode VII - The Force Awakens      Doug Walker                8

                                            cast_total_facebook_likes  \
movie_title
Avatar                                                           4834
Pirates of the Caribbean: At World's End                        48350
Spectre                                                         11700
The Dark Knight Rises                                          106759
Star Wars: Episode VII - The Force Awakens                        143

                                                    actor_3_name  \
movie_title
Avatar                                                 Wes Studi
Pirates of the Caribbean: At World's End          Jack Davenport
Spectre                                         Stephanie Sigman
The Dark Knight Rises                       Joseph Gordon-Levitt
Star Wars: Episode VII - The Force Awakens                   NaN

                                            facenumber_in_poster  \
movie_title
Avatar                                                       0.0
Pirates of the Caribbean: At World's End                     0.0
Spectre                                                      1.0
The Dark Knight Rises                                        0.0
Star Wars: Episode VII - The Force Awakens                   0.0

movie_title
Avatar                                                 avatar|future|marine|native|paraplegic
Pirates of the Caribbean: At World's End    goddess|marriage ceremony|marriage proposal|pi...
Spectre                                                   bomb|espionage|sequel|spy|terrorist
The Dark Knight Rises                       deception|imprisonment|lawlessness|police offi...
Star Wars: Episode VII - The Force Awakens                                                NaN

movie_title
Avatar                                      http://www.imdb.com/title/tt0499549/?ref_=fn_t...
Pirates of the Caribbean: At World's End    http://www.imdb.com/title/tt0449088/?ref_=fn_t...
Spectre                                     http://www.imdb.com/title/tt2379713/?ref_=fn_t...
The Dark Knight Rises                       http://www.imdb.com/title/tt1345836/?ref_=fn_t...
Star Wars: Episode VII - The Force Awakens  http://www.imdb.com/title/tt5289954/?ref_=fn_t...

                                            num_user_for_reviews language  \
movie_title
Avatar                                                    3054.0  English
Pirates of the Caribbean: At World's End                  1238.0  English
Spectre                                                    994.0  English
The Dark Knight Rises                                     2701.0  English
Star Wars: Episode VII - The Force Awakens                   NaN      NaN

                                           country content_rating  \
movie_title
Avatar                                         USA          PG-13
Pirates of the Caribbean: At World's End       USA          PG-13
Spectre                                         UK          PG-13
The Dark Knight Rises                          USA          PG-13
Star Wars: Episode VII - The Force Awakens     NaN            NaN

                                                 budget  title_year  \
movie_title
Avatar                                      237000000.0      2009.0
Pirates of the Caribbean: At World's End    300000000.0      2007.0
Spectre                                     245000000.0      2015.0
The Dark Knight Rises                       250000000.0      2012.0
Star Wars: Episode VII - The Force Awakens          NaN         NaN

                                            actor_2_facebook_likes  \
movie_title
Avatar                                                       936.0
Pirates of the Caribbean: At World's End                    5000.0
Spectre                                                      393.0
The Dark Knight Rises                                      23000.0
Star Wars: Episode VII - The Force Awakens                    12.0

                                            imdb_score  aspect_ratio  \
movie_title
Avatar                                             7.9          1.78
Pirates of the Caribbean: At World's End           7.1          2.35
Spectre                                            6.8          2.35
The Dark Knight Rises                              8.5          2.35
Star Wars: Episode VII - The Force Awakens         7.1           NaN

                                            movie_facebook_likes
movie_title
Avatar                                                     33000
Pirates of the Caribbean: At World's End                       0
Spectre                                                    85000
The Dark Knight Rises                                     164000
Star Wars: Episode VII - The Force Awakens                     0
movie_title
Avatar                                         True
Pirates of the Caribbean: At World's End       True
Spectre                                        True
The Dark Knight Rises                          True
Star Wars: Episode VII - The Force Awakens    False
John Carter                                    True
Spider-Man 3                                   True
Tangled                                       False
Avengers: Age of Ultron                        True
Harry Potter and the Half-Blood Prince         True
Name: duration, dtype: bool
1039
0.2113506916192026
count      4916
unique        2
top       False
freq       3877
Name: duration, dtype: object
0.21199755152009794
False    0.788649
True     0.211351
Name: duration, dtype: float64
0.9777687130328371
```

### Constructing multiple boolean conditions
```python
import pandas as pd
import numpy as np


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')
print(movie.head())

criteria1 = movie.imdb_score > 8
criteria2 = movie.content_rating == 'PG-13'
criteria3 = (movie.title_year < 2000) | (movie.title_year >= 2010)
print(criteria2.head())

criteria_final = criteria1 & criteria2 & criteria3
print(criteria_final.head())
```

#### Output
```
                                            color      director_name  \
movie_title
Avatar                                      Color      James Cameron
Pirates of the Caribbean: At World's End    Color     Gore Verbinski
Spectre                                     Color         Sam Mendes
The Dark Knight Rises                       Color  Christopher Nolan
Star Wars: Episode VII - The Force Awakens    NaN        Doug Walker

                                            num_critic_for_reviews  duration  \
movie_title
Avatar                                                       723.0     178.0
Pirates of the Caribbean: At World's End                     302.0     169.0
Spectre                                                      602.0     148.0
The Dark Knight Rises                                        813.0     164.0
Star Wars: Episode VII - The Force Awakens                     NaN       NaN

                                            director_facebook_likes  \
movie_title
Avatar                                                          0.0
Pirates of the Caribbean: At World's End                      563.0
Spectre                                                         0.0
The Dark Knight Rises                                       22000.0
Star Wars: Episode VII - The Force Awakens                    131.0

                                            actor_3_facebook_likes  \
movie_title
Avatar                                                       855.0
Pirates of the Caribbean: At World's End                    1000.0
Spectre                                                      161.0
The Dark Knight Rises                                      23000.0
Star Wars: Episode VII - The Force Awakens                     NaN

                                                actor_2_name  \
movie_title
Avatar                                      Joel David Moore
Pirates of the Caribbean: At World's End       Orlando Bloom
Spectre                                         Rory Kinnear
The Dark Knight Rises                         Christian Bale
Star Wars: Episode VII - The Force Awakens        Rob Walker

                                            actor_1_facebook_likes  \
movie_title
Avatar                                                      1000.0
Pirates of the Caribbean: At World's End                   40000.0
Spectre                                                    11000.0
The Dark Knight Rises                                      27000.0
Star Wars: Episode VII - The Force Awakens                   131.0

                                                  gross  \
movie_title
Avatar                                      760505847.0
Pirates of the Caribbean: At World's End    309404152.0
Spectre                                     200074175.0
The Dark Knight Rises                       448130642.0
Star Wars: Episode VII - The Force Awakens          NaN

                                                                     genres  \
movie_title
Avatar                                      Action|Adventure|Fantasy|Sci-Fi
Pirates of the Caribbean: At World's End           Action|Adventure|Fantasy
Spectre                                           Action|Adventure|Thriller
The Dark Knight Rises                                       Action|Thriller
Star Wars: Episode VII - The Force Awakens                      Documentary

                                               actor_1_name  num_voted_users  \
movie_title
Avatar                                          CCH Pounder           886204
Pirates of the Caribbean: At World's End        Johnny Depp           471220
Spectre                                     Christoph Waltz           275868
The Dark Knight Rises                             Tom Hardy          1144337
Star Wars: Episode VII - The Force Awakens      Doug Walker                8

                                            cast_total_facebook_likes  \
movie_title
Avatar                                                           4834
Pirates of the Caribbean: At World's End                        48350
Spectre                                                         11700
The Dark Knight Rises                                          106759
Star Wars: Episode VII - The Force Awakens                        143

                                                    actor_3_name  \
movie_title
Avatar                                                 Wes Studi
Pirates of the Caribbean: At World's End          Jack Davenport
Spectre                                         Stephanie Sigman
The Dark Knight Rises                       Joseph Gordon-Levitt
Star Wars: Episode VII - The Force Awakens                   NaN

                                            facenumber_in_poster  \
movie_title
Avatar                                                       0.0
Pirates of the Caribbean: At World's End                     0.0
Spectre                                                      1.0
The Dark Knight Rises                                        0.0
Star Wars: Episode VII - The Force Awakens                   0.0

movie_title
Avatar                                                 avatar|future|marine|native|paraplegic
Pirates of the Caribbean: At World's End    goddess|marriage ceremony|marriage proposal|pi...
Spectre                                                   bomb|espionage|sequel|spy|terrorist
The Dark Knight Rises                       deception|imprisonment|lawlessness|police offi...
Star Wars: Episode VII - The Force Awakens                                                NaN
movie_title
Avatar                                      http://www.imdb.com/title/tt0499549/?ref_=fn_t...
Pirates of the Caribbean: At World's End    http://www.imdb.com/title/tt0449088/?ref_=fn_t...
Spectre                                     http://www.imdb.com/title/tt2379713/?ref_=fn_t...
The Dark Knight Rises                       http://www.imdb.com/title/tt1345836/?ref_=fn_t...
Star Wars: Episode VII - The Force Awakens  http://www.imdb.com/title/tt5289954/?ref_=fn_t...

                                            num_user_for_reviews language  \
movie_title
Avatar                                                    3054.0  English
Pirates of the Caribbean: At World's End                  1238.0  English
Spectre                                                    994.0  English
The Dark Knight Rises                                     2701.0  English
Star Wars: Episode VII - The Force Awakens                   NaN      NaN

                                           country content_rating  \
movie_title
Avatar                                         USA          PG-13
Pirates of the Caribbean: At World's End       USA          PG-13
Spectre                                         UK          PG-13
The Dark Knight Rises                          USA          PG-13
Star Wars: Episode VII - The Force Awakens     NaN            NaN

                                                 budget  title_year  \
movie_title
Avatar                                      237000000.0      2009.0
Pirates of the Caribbean: At World's End    300000000.0      2007.0
Spectre                                     245000000.0      2015.0
The Dark Knight Rises                       250000000.0      2012.0
Star Wars: Episode VII - The Force Awakens          NaN         NaN

                                            actor_2_facebook_likes  \
movie_title
Avatar                                                       936.0
Pirates of the Caribbean: At World's End                    5000.0
Spectre                                                      393.0
The Dark Knight Rises                                      23000.0
Star Wars: Episode VII - The Force Awakens                    12.0

                                            imdb_score  aspect_ratio  \
movie_title
Avatar                                             7.9          1.78
Pirates of the Caribbean: At World's End           7.1          2.35
Spectre                                            6.8          2.35
The Dark Knight Rises                              8.5          2.35
Star Wars: Episode VII - The Force Awakens         7.1           NaN

                                            movie_facebook_likes
movie_title
Avatar                                                     33000
Pirates of the Caribbean: At World's End                       0
Spectre                                                    85000
The Dark Knight Rises                                     164000
Star Wars: Episode VII - The Force Awakens                     0
movie_title
Avatar                                         True
Pirates of the Caribbean: At World's End       True
Spectre                                        True
The Dark Knight Rises                          True
Star Wars: Episode VII - The Force Awakens    False
Name: content_rating, dtype: bool
movie_title
Avatar                                        False
Pirates of the Caribbean: At World's End      False
Spectre                                       False
The Dark Knight Rises                          True
Star Wars: Episode VII - The Force Awakens    False
dtype: bool
```

### Filtering with boolean indexing
```python
import pandas as pd
import numpy as numpy


pd.options.display.max_columns = 50

movie = pd.read_csv('data/movie.csv', index_col='movie_title')

crit_a1 = movie.imdb_score > 8
crit_a2 = movie.content_rating == 'PG-13'
crit_a3 = (movie.title_year < 2000) | (movie.title_year > 2009)
final_crit_a = crit_a1 & crit_a2 & crit_a3

crit_b1 = movie.imdb_score < 5
crit_b2 = movie.content_rating == 'R'
crit_b3 = (movie.title_year >= 2000) & (movie.title_year <= 2010)
final_crit_b = crit_b1 & crit_b2 & crit_b3
final_crit_all = final_crit_a | final_crit_b
print(final_crit_all.head())
print(movie[final_crit_all].head())

cols = ['imdb_score', 'content_rating', 'title_year']
movie_filtered = movie.loc[final_crit_all, cols]
print(movie_filtered.head(10))

final_crit_a2 = (movie.imdb_score > 8) & \
                (movie.content_rating == 'PG-13') & \
                ((movie.title_year < 2000) | (movie.title_year > 2009))
print(final_crit_a2.equals(final_crit_a))
```

#### Output
```
movie_title
Avatar                                        False
Pirates of the Caribbean: At World's End      False
Spectre                                       False
The Dark Knight Rises                          True
Star Wars: Episode VII - The Force Awakens    False
dtype: bool
                            color      director_name  num_critic_for_reviews  \
movie_title
The Dark Knight Rises       Color  Christopher Nolan                   813.0
The Avengers                Color        Joss Whedon                   703.0
Captain America: Civil War  Color      Anthony Russo                   516.0
Guardians of the Galaxy     Color         James Gunn                   653.0
Interstellar                Color  Christopher Nolan                   712.0

                            duration  director_facebook_likes  \
movie_title
The Dark Knight Rises          164.0                  22000.0
The Avengers                   173.0                      0.0
Captain America: Civil War     147.0                     94.0
Guardians of the Galaxy        121.0                    571.0
Interstellar                   169.0                  22000.0

                            actor_3_facebook_likes        actor_2_name  \
movie_title
The Dark Knight Rises                      23000.0      Christian Bale
The Avengers                               19000.0   Robert Downey Jr.
Captain America: Civil War                 11000.0  Scarlett Johansson
Guardians of the Galaxy                     3000.0          Vin Diesel
Interstellar                                6000.0       Anne Hathaway

                            actor_1_facebook_likes        gross  \
movie_title
The Dark Knight Rises                      27000.0  448130642.0
The Avengers                               26000.0  623279547.0
Captain America: Civil War                 21000.0  407197282.0
Guardians of the Galaxy                    14000.0  333130696.0
Interstellar                               11000.0  187991439.0

                                             genres         actor_1_name  \
movie_title
The Dark Knight Rises               Action|Thriller            Tom Hardy
The Avengers                Action|Adventure|Sci-Fi      Chris Hemsworth
Captain America: Civil War  Action|Adventure|Sci-Fi    Robert Downey Jr.
Guardians of the Galaxy     Action|Adventure|Sci-Fi       Bradley Cooper
Interstellar                 Adventure|Drama|Sci-Fi  Matthew McConaughey

                            num_voted_users  cast_total_facebook_likes  \
movie_title
The Dark Knight Rises               1144337                     106759
The Avengers                         995415                      87697
Captain America: Civil War           272670                      64798
Guardians of the Galaxy              682155                      32438
Interstellar                         928227                      31488

                                    actor_3_name  facenumber_in_poster  \
movie_title
The Dark Knight Rises       Joseph Gordon-Levitt                   0.0
The Avengers                  Scarlett Johansson                   3.0
Captain America: Civil War           Chris Evans                   0.0
Guardians of the Galaxy           Djimon Hounsou                   3.0
Interstellar                       Mackenzie Foy                   1.0

                                                                plot_keywords  \
movie_title
The Dark Knight Rises       deception|imprisonment|lawlessness|police offi...
The Avengers                  alien invasion|assassin|battle|iron man|soldier
Captain America: Civil War  based on comic book|knife|marvel cinematic uni...
Guardians of the Galaxy     bounty hunter|outer space|raccoon|talking anim...
Interstellar                black hole|father daughter relationship|saving...

                                                              movie_imdb_link  \
movie_title
The Dark Knight Rises       http://www.imdb.com/title/tt1345836/?ref_=fn_t...
The Avengers                http://www.imdb.com/title/tt0848228/?ref_=fn_t...
Captain America: Civil War  http://www.imdb.com/title/tt3498820/?ref_=fn_t...
Guardians of the Galaxy     http://www.imdb.com/title/tt2015381/?ref_=fn_t...
Interstellar                http://www.imdb.com/title/tt0816692/?ref_=fn_t...

                            num_user_for_reviews language country  \
movie_title
The Dark Knight Rises                     2701.0  English     USA
The Avengers                              1722.0  English     USA
Captain America: Civil War                1022.0  English     USA
Guardians of the Galaxy                   1097.0  English     USA
Interstellar                              2725.0  English     USA

                           content_rating       budget  title_year  \
movie_title
The Dark Knight Rises               PG-13  250000000.0      2012.0
The Avengers                        PG-13  220000000.0      2012.0
Captain America: Civil War          PG-13  250000000.0      2016.0
Guardians of the Galaxy             PG-13  170000000.0      2014.0
Interstellar                        PG-13  165000000.0      2014.0

                            actor_2_facebook_likes  imdb_score  aspect_ratio  \
movie_title
The Dark Knight Rises                      23000.0         8.5          2.35
The Avengers                               21000.0         8.1          1.85
Captain America: Civil War                 19000.0         8.2          2.35
Guardians of the Galaxy                    14000.0         8.1          2.35
Interstellar                               11000.0         8.6          2.35

                            movie_facebook_likes
movie_title
The Dark Knight Rises                     164000
The Avengers                              123000
Captain America: Civil War                 72000
Guardians of the Galaxy                    96000
Interstellar                              349000
                            imdb_score content_rating  title_year
movie_title
The Dark Knight Rises              8.5          PG-13      2012.0
The Avengers                       8.1          PG-13      2012.0
Captain America: Civil War         8.2          PG-13      2016.0
Guardians of the Galaxy            8.1          PG-13      2014.0
Interstellar                       8.6          PG-13      2014.0
Inception                          8.8          PG-13      2010.0
The Martian                        8.1          PG-13      2015.0
Town & Country                     4.4              R      2001.0
Sex and the City 2                 4.3              R      2010.0
Rollerball                         3.0              R      2002.0
True
```

### Replicating boolean indexing with index selection
```python
import pandas as pd
import numpy as np
from IPython import InteractiveShell


inter = InteractiveShell()
pd.options.display.max_columns = 50


college = pd.read_csv('data/college.csv')
print(college[college['STABBR'] == 'TX'].head())

college2 = college.set_index('STABBR')
print(college2.loc['TX'].head())

print(inter.get_ipython().run_line_magic('timeit', "college[college['STABBR'] == 'TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2.loc['TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2 = college.set_index('STABBR')"))

states =['TX', 'CA', 'NY']
print(college[college['STABBR'].isin(states)])
print(college2.loc[states].head())
```

#### Output
```
                            INSTNM        CITY STABBR  HBCU  MENONLY  \
3610  Abilene Christian University     Abilene     TX   0.0      0.0
3611       Alvin Community College       Alvin     TX   0.0      0.0
3612              Amarillo College    Amarillo     TX   0.0      0.0
3613              Angelina College      Lufkin     TX   0.0      0.0
3614       Angelo State University  San Angelo     TX   0.0      0.0

      WOMENONLY  RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY    UGDS  \
3610        0.0         1     530.0     545.0           0.0  3572.0
3611        0.0         0       NaN       NaN           0.0  4682.0
3612        0.0         0       NaN       NaN           0.0  9346.0
3613        0.0         0       NaN       NaN           0.0  3825.0
3614        0.0         0     475.0     490.0           0.0  5290.0

      UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  \
3610      0.6739      0.0798     0.1414      0.0090     0.0039     0.0000
3611      0.5126      0.1034     0.3093      0.0500     0.0064     0.0038
3612      0.5104      0.0507     0.3888      0.0293     0.0122     0.0000
3613      0.5854      0.1508     0.2207      0.0076     0.0073     0.0013
3614      0.5225      0.0841     0.3166      0.0087     0.0036     0.0017

      UGDS_2MOR  UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  PCTPELL  PCTFLOAN  \
3610     0.0454    0.0423     0.0045    0.0468         1   0.2595    0.5527
3611     0.0002    0.0000     0.0143    0.7123         1   0.1549    0.0625
3612     0.0000    0.0001     0.0085    0.6922         1   0.3786    0.1573
3613     0.0264    0.0005     0.0000    0.5600         1   0.5308    0.0000
3614     0.0285    0.0331     0.0011    0.1289         1   0.4068    0.5279

      UG25ABV MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
3610   0.0381           40200              25985
3611   0.2841           34500               6750
3612   0.3431           31700              10950
3613   0.2603           26900  PrivacySuppressed
3614   0.1407           37700            21319.5
                              INSTNM        CITY  HBCU  MENONLY  WOMENONLY  \
STABBR
TX      Abilene Christian University     Abilene   0.0      0.0        0.0
TX           Alvin Community College       Alvin   0.0      0.0        0.0
TX                  Amarillo College    Amarillo   0.0      0.0        0.0
TX                  Angelina College      Lufkin   0.0      0.0        0.0
TX           Angelo State University  San Angelo   0.0      0.0        0.0

        RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY    UGDS  UGDS_WHITE  \
STABBR
TX             1     530.0     545.0           0.0  3572.0      0.6739
TX             0       NaN       NaN           0.0  4682.0      0.5126
TX             0       NaN       NaN           0.0  9346.0      0.5104
TX             0       NaN       NaN           0.0  3825.0      0.5854
TX             0     475.0     490.0           0.0  5290.0      0.5225

        UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  \
STABBR
TX          0.0798     0.1414      0.0090     0.0039     0.0000     0.0454
TX          0.1034     0.3093      0.0500     0.0064     0.0038     0.0002
TX          0.0507     0.3888      0.0293     0.0122     0.0000     0.0000
TX          0.1508     0.2207      0.0076     0.0073     0.0013     0.0264
TX          0.0841     0.3166      0.0087     0.0036     0.0017     0.0285

        UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  PCTPELL  PCTFLOAN  UG25ABV  \
STABBR
TX        0.0423     0.0045    0.0468         1   0.2595    0.5527   0.0381
TX        0.0000     0.0143    0.7123         1   0.1549    0.0625   0.2841
TX        0.0001     0.0085    0.6922         1   0.3786    0.1573   0.3431
TX        0.0005     0.0000    0.5600         1   0.5308    0.0000   0.2603
TX        0.0331     0.0011    0.1289         1   0.4068    0.5279   0.1407

       MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
STABBR
TX               40200              25985
TX               34500               6750
TX               31700              10950
TX               26900  PrivacySuppressed
TX               37700            21319.5
3.15 ms ± 50.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
None
1.6 ms ± 42.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
None
3.54 ms ± 12.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
None
                                                 INSTNM              CITY  \
192                           Academy of Art University     San Francisco
193              ITT Technical Institute-Rancho Cordova    Rancho Cordova
194      Academy of Chinese Culture and Health Sciences           Oakland
195            The Academy of Radio and TV Broadcasting  Huntington Beach
196                Avalon School of Cosmetology-Alameda           Alameda
197                                  College of Alameda           Alameda
198                               Allan Hancock College       Santa Maria
199       American Academy of Dramatic Arts-Los Angeles       Los Angeles
200               American Baptist Seminary of the West          Berkeley
201                American Film Institute Conservatory       Los Angeles
202                             American Beauty College       West Covina
203                 American Career College-Los Angeles       Los Angeles
204                       American Conservatory Theater     San Francisco
205                              American River College        Sacramento
206                             Antelope Valley College         Lancaster
207                        Art Center College of Design          Pasadena
208            Associated Technical College-Los Angeles       Los Angeles
209              Associated Technical College-San Diego         San Diego
210                            Azusa Pacific University             Azusa
211                                 Bakersfield College       Bakersfield
212                           Barstow Community College           Barstow
213                        Bellus Academy-National City     National City
214                                 Bethesda University           Anaheim
215                                    Biola University         La Mirada
216                                    Brooks Institute           Ventura
217                           Brownson Technical School           Anaheim
218                                    Bryan University       Los Angeles
219                                       Butte College          Oroville
220                         Phillips Graduate Institute        Chatsworth
221            California Institute of Integral Studies     San Francisco
...                                                 ...               ...
7423                    Vista College - College Station   College Station
7425                 CC's Cosmetology College-Texarkana         Texarkana
7427          SW School of Business & Technical Careers            Uvalde
7428  SW School of Business and Technical Careers-De...           Del Rio
7429  SW School of Business and Technical Careers-No...            Austin
7430  SW School of Business and Technical Careers-So...            Austin
7433                            UEI College-Bakersfield       Bakersfield
7440                 Marinello School of Beauty-Concord           Concord
7441                Marinello School of Beauty-Stockton          Stockton
7452        Franklin Career Institute - Brooklyn Campus          Brooklyn
7457  Texas Barber Colleges and Hairstyling Schools ...            Dallas
7458  Texas Barber Colleges and Hairstyling Schools ...            Dallas
7459  Texas Barber Colleges and Hairstyling Schools ...           Houston
7460  Texas Barber Colleges and Hairstyling Schools ...           Houston
7461  Texas Barber Colleges and Hairstyling Schools ...            Conroe
7475                Blake Austin College Beauty Academy         Vacaville
7494                                CCI Training Center            Dallas
7520                          Strayer University-Irving            Irving
7521                            Strayer University-Katy           Houston
7522               Strayer University-Northwest Houston           Houston
7523                           Strayer University-Plano             Plano
7524                      Strayer University-Cedar Hill        Cedar Hill
7525                    Strayer University-North Dallas            Dallas
7526                     Strayer University-San Antonio       San Antonio
7527                        Strayer University-Stafford          Stafford
7528                           WestMed College - Merced            Merced
7529                                    Vantage College           El Paso
7530         SAE Institute of Technology  San Francisco        Emeryville
7533  Bay Area Medical Academy - San Jose Satellite ...          San Jose
7534            Excel Learning Center-San Antonio South       San Antonio

     STABBR  HBCU  MENONLY  WOMENONLY  RELAFFIL  SATVRMID  SATMTMID  \
192      CA   0.0      0.0        0.0         0       NaN       NaN
193      CA   0.0      0.0        0.0         0       NaN       NaN
194      CA   0.0      0.0        0.0         0       NaN       NaN
195      CA   0.0      0.0        0.0         0       NaN       NaN
196      CA   0.0      0.0        0.0         0       NaN       NaN
197      CA   0.0      0.0        0.0         0       NaN       NaN
198      CA   0.0      0.0        0.0         0       NaN       NaN
199      CA   0.0      0.0        0.0         0       NaN       NaN
200      CA   0.0      0.0        0.0         1       NaN       NaN
201      CA   0.0      0.0        0.0         0       NaN       NaN
202      CA   0.0      0.0        0.0         0       NaN       NaN
203      CA   0.0      0.0        0.0         0       NaN       NaN
204      CA   0.0      0.0        0.0         0       NaN       NaN
205      CA   0.0      0.0        0.0         0       NaN       NaN
206      CA   0.0      0.0        0.0         0       NaN       NaN
207      CA   0.0      0.0        0.0         0       NaN       NaN
208      CA   0.0      0.0        0.0         0       NaN       NaN
209      CA   0.0      0.0        0.0         0       NaN       NaN
210      CA   0.0      0.0        0.0         1     515.0     515.0
211      CA   0.0      0.0        0.0         0       NaN       NaN
212      CA   0.0      0.0        0.0         0       NaN       NaN
213      CA   0.0      0.0        0.0         0       NaN       NaN
214      CA   0.0      0.0        0.0         1       NaN       NaN
215      CA   0.0      0.0        0.0         1     555.0     555.0
216      CA   0.0      0.0        0.0         0       NaN       NaN
217      CA   0.0      0.0        0.0         0       NaN       NaN
218      CA   0.0      0.0        0.0         0       NaN       NaN
219      CA   0.0      0.0        0.0         0       NaN       NaN
220      CA   0.0      0.0        0.0         0       NaN       NaN
221      CA   0.0      0.0        0.0         0       NaN       NaN
...     ...   ...      ...        ...       ...       ...       ...
7423     TX   NaN      NaN        NaN         1       NaN       NaN
7425     TX   NaN      NaN        NaN         1       NaN       NaN
7427     TX   NaN      NaN        NaN         1       NaN       NaN
7428     TX   NaN      NaN        NaN         1       NaN       NaN
7429     TX   NaN      NaN        NaN         1       NaN       NaN
7430     TX   NaN      NaN        NaN         1       NaN       NaN
7433     CA   NaN      NaN        NaN         1       NaN       NaN
7440     CA   NaN      NaN        NaN         1       NaN       NaN
7441     CA   NaN      NaN        NaN         1       NaN       NaN
7452     NY   NaN      NaN        NaN         1       NaN       NaN
7457     TX   NaN      NaN        NaN         1       NaN       NaN
7458     TX   NaN      NaN        NaN         1       NaN       NaN
7459     TX   NaN      NaN        NaN         1       NaN       NaN
7460     TX   NaN      NaN        NaN         1       NaN       NaN
7461     TX   NaN      NaN        NaN         1       NaN       NaN
7475     CA   NaN      NaN        NaN         1       NaN       NaN
7494     TX   NaN      NaN        NaN         1       NaN       NaN
7520     TX   NaN      NaN        NaN         1       NaN       NaN
7521     TX   NaN      NaN        NaN         1       NaN       NaN
7522     TX   NaN      NaN        NaN         1       NaN       NaN
7523     TX   NaN      NaN        NaN         1       NaN       NaN
7524     TX   NaN      NaN        NaN         1       NaN       NaN
7525     TX   NaN      NaN        NaN         1       NaN       NaN
7526     TX   NaN      NaN        NaN         1       NaN       NaN
7527     TX   NaN      NaN        NaN         1       NaN       NaN
7528     CA   NaN      NaN        NaN         1       NaN       NaN
7529     TX   NaN      NaN        NaN         1       NaN       NaN
7530     CA   NaN      NaN        NaN         1       NaN       NaN
7533     CA   NaN      NaN        NaN         1       NaN       NaN
7534     TX   NaN      NaN        NaN         1       NaN       NaN

      DISTANCEONLY     UGDS  UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  \
192            0.0   9885.0      0.2392      0.0685     0.1141      0.0804
193            0.0    500.0      0.4720      0.1140     0.1100      0.0760
194            0.0      NaN         NaN         NaN        NaN         NaN
195            0.0     14.0      0.2143      0.4286     0.3571      0.0000
196            0.0    253.0      0.1265      0.4743     0.2253      0.0672
197            0.0   5141.0      0.1529      0.2128     0.2196      0.3021
198            0.0   9738.0      0.3565      0.0279     0.5287      0.0418
199            0.0    280.0      0.4143      0.0821     0.0964      0.0107
200            0.0      NaN         NaN         NaN        NaN         NaN
201            0.0      NaN         NaN         NaN        NaN         NaN
202            0.0     97.0      0.1031      0.0619     0.7835      0.0412
203            0.0   1613.0      0.0484      0.1494     0.6454      0.0694
204            0.0      0.0      0.0000      0.0000     0.0000      0.0000
205            0.0  26803.0      0.4695      0.0989     0.2063      0.1063
206            0.0  12367.0      0.2401      0.2008     0.4601      0.0323
207            0.0   1814.0      0.2001      0.0116     0.1097      0.3484
208            0.0    361.0      0.0970      0.4377     0.3850      0.0166
209            0.0    119.0      0.2353      0.3193     0.4454      0.0000
210            0.0   5918.0      0.4714      0.0448     0.2614      0.0912
211            0.0  16982.0      0.2298      0.0400     0.6473      0.0377
212            0.0   1588.0      0.3004      0.1398     0.4509      0.0258
213            0.0    177.0      0.1073      0.1299     0.6045      0.0678
214            0.0    261.0      0.1111      0.1456     0.2261      0.4751
215            0.0   4364.0      0.5165      0.0209     0.1829      0.1613
216            0.0    415.0      0.2602      0.0313     0.0675      0.0241
217            0.0     46.0      0.1739      0.0652     0.5435      0.1957
218            0.0   1324.0      0.5355      0.2100     0.1337      0.0181
219            0.0  11164.0      0.6006      0.0257     0.1916      0.0547
220            0.0      NaN         NaN         NaN        NaN         NaN
221            0.0    104.0      0.4423      0.1442     0.2212      0.0385
...            ...      ...         ...         ...        ...         ...
7423           NaN      NaN         NaN         NaN        NaN         NaN
7425           NaN      NaN         NaN         NaN        NaN         NaN
7427           NaN      NaN         NaN         NaN        NaN         NaN
7428           NaN      NaN         NaN         NaN        NaN         NaN
7429           NaN      NaN         NaN         NaN        NaN         NaN
7430           NaN      NaN         NaN         NaN        NaN         NaN
7433           NaN      NaN         NaN         NaN        NaN         NaN
7440           NaN      NaN         NaN         NaN        NaN         NaN
7441           NaN      NaN         NaN         NaN        NaN         NaN
7452           NaN      NaN         NaN         NaN        NaN         NaN
7457           NaN      NaN         NaN         NaN        NaN         NaN
7458           NaN      NaN         NaN         NaN        NaN         NaN
7459           NaN      NaN         NaN         NaN        NaN         NaN
7460           NaN      NaN         NaN         NaN        NaN         NaN
7461           NaN      NaN         NaN         NaN        NaN         NaN
7475           NaN      NaN         NaN         NaN        NaN         NaN
7494           NaN      NaN         NaN         NaN        NaN         NaN
7520           NaN      NaN         NaN         NaN        NaN         NaN
7521           NaN      NaN         NaN         NaN        NaN         NaN
7522           NaN      NaN         NaN         NaN        NaN         NaN
7523           NaN      NaN         NaN         NaN        NaN         NaN
7524           NaN      NaN         NaN         NaN        NaN         NaN
7525           NaN      NaN         NaN         NaN        NaN         NaN
7526           NaN      NaN         NaN         NaN        NaN         NaN
7527           NaN      NaN         NaN         NaN        NaN         NaN
7528           NaN      NaN         NaN         NaN        NaN         NaN
7529           NaN      NaN         NaN         NaN        NaN         NaN
7530           NaN      NaN         NaN         NaN        NaN         NaN
7533           NaN      NaN         NaN         NaN        NaN         NaN
7534           NaN      NaN         NaN         NaN        NaN         NaN

      UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN  PPTUG_EF  \
192      0.0051     0.0058     0.0249    0.2523     0.2098    0.4334
193      0.0080     0.0020     0.0400    0.0000     0.1780    0.2540
194         NaN        NaN        NaN       NaN        NaN       NaN
195      0.0000     0.0000     0.0000    0.0000     0.0000    0.0000
196      0.0079     0.0000     0.0553    0.0000     0.0435    0.5099
197      0.0037     0.0041     0.0473    0.0076     0.0500    0.8440
198      0.0070     0.0043     0.0312    0.0021     0.0005    0.6630
199      0.0107     0.0036     0.1321    0.2429     0.0071    0.0000
200         NaN        NaN        NaN       NaN        NaN       NaN
201         NaN        NaN        NaN       NaN        NaN       NaN
202      0.0000     0.0000     0.0103    0.0000     0.0000    0.5670
203      0.0043     0.0081     0.0632    0.0000     0.0118    0.0000
204      0.0000     0.0000     0.0000    0.0000     0.0000       NaN
205      0.0076     0.0085     0.0587    0.0057     0.0385    0.7447
206      0.0041     0.0014     0.0475    0.0013     0.0125    0.6531
207      0.0022     0.0033     0.0436    0.2696     0.0116    0.1340
208      0.0111     0.0055     0.0360    0.0000     0.0111    0.0000
209      0.0000     0.0000     0.0000    0.0000     0.0000    0.0000
210      0.0019     0.0095     0.0738    0.0191     0.0269    0.0875
211      0.0042     0.0011     0.0320    0.0026     0.0052    0.6585
212      0.0120     0.0069     0.0560    0.0019     0.0063    0.7513
213      0.0169     0.0113     0.0621    0.0000     0.0000    0.0000
214      0.0000     0.0000     0.0000    0.0115     0.0307    0.1609
215      0.0014     0.0030     0.0648    0.0270     0.0222    0.0229
216      0.0024     0.0024     0.0048    0.0000     0.6072    0.2169
217      0.0000     0.0000     0.0000    0.0000     0.0217    0.0000
218      0.0083     0.0076     0.0823    0.0000     0.0045    0.0000
219      0.0170     0.0046     0.0210    0.0157     0.0691    0.4941
220         NaN        NaN        NaN       NaN        NaN       NaN
221      0.0096     0.0000     0.0769    0.0096     0.0577    0.0769
...         ...        ...        ...       ...        ...       ...
7423        NaN        NaN        NaN       NaN        NaN       NaN
7425        NaN        NaN        NaN       NaN        NaN       NaN
7427        NaN        NaN        NaN       NaN        NaN       NaN
7428        NaN        NaN        NaN       NaN        NaN       NaN
7429        NaN        NaN        NaN       NaN        NaN       NaN
7430        NaN        NaN        NaN       NaN        NaN       NaN
7433        NaN        NaN        NaN       NaN        NaN       NaN
7440        NaN        NaN        NaN       NaN        NaN       NaN
7441        NaN        NaN        NaN       NaN        NaN       NaN
7452        NaN        NaN        NaN       NaN        NaN       NaN
7457        NaN        NaN        NaN       NaN        NaN       NaN
7458        NaN        NaN        NaN       NaN        NaN       NaN
7459        NaN        NaN        NaN       NaN        NaN       NaN
7460        NaN        NaN        NaN       NaN        NaN       NaN
7461        NaN        NaN        NaN       NaN        NaN       NaN
7475        NaN        NaN        NaN       NaN        NaN       NaN
7494        NaN        NaN        NaN       NaN        NaN       NaN
7520        NaN        NaN        NaN       NaN        NaN       NaN
7521        NaN        NaN        NaN       NaN        NaN       NaN
7522        NaN        NaN        NaN       NaN        NaN       NaN
7523        NaN        NaN        NaN       NaN        NaN       NaN
7524        NaN        NaN        NaN       NaN        NaN       NaN
7525        NaN        NaN        NaN       NaN        NaN       NaN
7526        NaN        NaN        NaN       NaN        NaN       NaN
7527        NaN        NaN        NaN       NaN        NaN       NaN
7528        NaN        NaN        NaN       NaN        NaN       NaN
7529        NaN        NaN        NaN       NaN        NaN       NaN
7530        NaN        NaN        NaN       NaN        NaN       NaN
7533        NaN        NaN        NaN       NaN        NaN       NaN
7534        NaN        NaN        NaN       NaN        NaN       NaN

      CURROPER  PCTPELL  PCTFLOAN  UG25ABV    MD_EARN_WNE_P10  \
192          1   0.4008    0.5524   0.4043              36000
193          0   0.7137    0.7667   0.7235              38800
194          1      NaN       NaN      NaN                NaN
195          1   0.9579    1.0000   0.4545              28400
196          1   0.7407    0.6768   0.3387              21600
197          1   0.2273    0.0117   0.3940              31900
198          1   0.2531    0.0231   0.3713              29800
199          1   0.5039    0.6008   0.1589              27800
200          1      NaN       NaN      NaN                NaN
201          1      NaN       NaN      NaN                NaN
202          1   0.8200    0.5400   0.1333  PrivacySuppressed
203          1   0.7371    0.6497   0.4017              29500
204          1      NaN       NaN      NaN  PrivacySuppressed
205          1   0.2843    0.0560   0.5035              28400
206          1   0.5291    0.1510   0.3889              27000
207          1   0.3599    0.4929   0.3039              56100
208          1   0.8116    0.3682   0.5916              23500
209          1   0.9442    0.8579   0.5455              18000
210          1   0.2898    0.5172   0.1467              50000
211          1   0.3976    0.0328   0.3337              29300
212          1   0.4902    0.0000   0.5086              31700
213          1   0.7057    0.6755   0.3459              16500
214          1   0.3686    0.2078   0.4672  PrivacySuppressed
215          1   0.3110    0.6176   0.0395              40500
216          1   0.3780    0.6321   0.2907              28800
217          1   0.8077    0.8013   0.6222              39500
218          1   0.5675    0.7468   0.7509              43700
219          1   0.4845    0.1223   0.3289              29400
220          1      NaN       NaN      NaN                NaN
221          1   0.5067    0.7600   0.7067  PrivacySuppressed
...        ...      ...       ...      ...                ...
7423         1      NaN       NaN      NaN                NaN
7425         1      NaN       NaN      NaN              14800
7427         1      NaN       NaN      NaN  PrivacySuppressed
7428         1      NaN       NaN      NaN              14600
7429         0      NaN       NaN      NaN              14600
7430         1      NaN       NaN      NaN              14600
7433         1      NaN       NaN      NaN                NaN
7440         0      NaN       NaN      NaN              18600
7441         0      NaN       NaN      NaN              18600
7452         0      NaN       NaN      NaN              20000
7457         1      NaN       NaN      NaN              16800
7458         1      NaN       NaN      NaN              16800
7459         1      NaN       NaN      NaN              16800
7460         0      NaN       NaN      NaN              16800
7461         0      NaN       NaN      NaN              16800
7475         1      NaN       NaN      NaN  PrivacySuppressed
7494         1      NaN       NaN      NaN                NaN
7520         1      NaN       NaN      NaN              49200
7521         1      NaN       NaN      NaN              49200
7522         1      NaN       NaN      NaN              49200
7523         1      NaN       NaN      NaN              49200
7524         1      NaN       NaN      NaN                NaN
7525         1      NaN       NaN      NaN                NaN
7526         1      NaN       NaN      NaN                NaN
7527         1      NaN       NaN      NaN                NaN
7528         1      NaN       NaN      NaN                NaN
7529         1      NaN       NaN      NaN                NaN
7530         1      NaN       NaN      NaN                NaN
7533         1      NaN       NaN      NaN                NaN
7534         1      NaN       NaN      NaN                NaN

     GRAD_DEBT_MDN_SUPP
192               35093
193             25827.5
194   PrivacySuppressed
195                9500
196                9860
197   PrivacySuppressed
198               10500
199               12000
200   PrivacySuppressed
201   PrivacySuppressed
202                4749
203                9500
204   PrivacySuppressed
205               11410
206               16476
207               33721
208                8963
209                9500
210               22500
211               11398
212   PrivacySuppressed
213               15378
214   PrivacySuppressed
215               24375
216               31000
217                9394
218               20000
219               12898
220   PrivacySuppressed
221               18750
...                 ...
7423              14250
7425  PrivacySuppressed
7427  PrivacySuppressed
7428  PrivacySuppressed
7429  PrivacySuppressed
7430  PrivacySuppressed
7433               9500
7440              10352
7441              10352
7452  PrivacySuppressed
7457               9500
7458               9500
7459               9500
7460               9500
7461               9500
7475               9500
7494               8313
7520            36173.5
7521            36173.5
7522            36173.5
7523            36173.5
7524            36173.5
7525            36173.5
7526            36173.5
7527            36173.5
7528            15623.5
7529               9500
7530               9500
7533  PrivacySuppressed
7534              12125

[1704 rows x 27 columns]
                              INSTNM        CITY  HBCU  MENONLY  WOMENONLY  \
STABBR
TX      Abilene Christian University     Abilene   0.0      0.0        0.0
TX           Alvin Community College       Alvin   0.0      0.0        0.0
TX                  Amarillo College    Amarillo   0.0      0.0        0.0
TX                  Angelina College      Lufkin   0.0      0.0        0.0
TX           Angelo State University  San Angelo   0.0      0.0        0.0

        RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY    UGDS  UGDS_WHITE  \
STABBR
TX             1     530.0     545.0           0.0  3572.0      0.6739
TX             0       NaN       NaN           0.0  4682.0      0.5126
TX             0       NaN       NaN           0.0  9346.0      0.5104
TX             0       NaN       NaN           0.0  3825.0      0.5854
TX             0     475.0     490.0           0.0  5290.0      0.5225

        UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  \
STABBR
TX          0.0798     0.1414      0.0090     0.0039     0.0000     0.0454
TX          0.1034     0.3093      0.0500     0.0064     0.0038     0.0002
TX          0.0507     0.3888      0.0293     0.0122     0.0000     0.0000
TX          0.1508     0.2207      0.0076     0.0073     0.0013     0.0264
TX          0.0841     0.3166      0.0087     0.0036     0.0017     0.0285

        UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  PCTPELL  PCTFLOAN  UG25ABV  \
STABBR
TX        0.0423     0.0045    0.0468         1   0.2595    0.5527   0.0381
TX        0.0000     0.0143    0.7123         1   0.1549    0.0625   0.2841
TX        0.0001     0.0085    0.6922         1   0.3786    0.1573   0.3431
TX        0.0005     0.0000    0.5600         1   0.5308    0.0000   0.2603
TX        0.0331     0.0011    0.1289         1   0.4068    0.5279   0.1407

       MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
STABBR
TX               40200              25985
TX               34500               6750
TX               31700              10950
TX               26900  PrivacySuppressed
TX               37700            21319.5
```

### Selecting with unique and sorted indexes
```python
import pandas as pd
import numpy as np
from IPython import InteractiveShell

inter = InteractiveShell()
pd.options.display.max_columns = 50

college = pd.read_csv('data/college.csv')
college2 = college.set_index('STABBR')
print(college2.index.is_monotonic)

college3 = college2.sort_index()
print(college3.index.is_monotonic)
print(inter.get_ipython().run_line_magic('timeit', "college[college['STABBR'] == 'TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college2.loc['TX']"))
print(inter.get_ipython().run_line_magic('timeit', "college3.loc['TX']"))

college_unique = college.set_index('INSTNM')
print(college_unique.index.is_unique)

college[college['INSTNM'] == 'Stanford University']
print(college_unique.loc['Stanford University'])
print(inter.get_ipython().run_line_magic('timeit', "college[college['INSTNM'] == 'Stanford University']"))
print(inter.get_ipython().run_line_magic('timeit', "college_unique.loc['Stanford University']"))

college.index = college['CITY'] + ', ' + college['STABBR']
college = college.sort_index()
print(college.head())
print(college.loc['Miami, FL'].head())
print(inter.get_ipython().run_cell_magic('timeit', '', "crit1 = college['CITY'] == 'Miami' \ncrit2 = college['STABBR'] == 'FL'\ncollege[crit1 & crit2]"))
print(inter.get_ipython().run_line_magic('timeit', "college.loc['Miami, FL']"))
print(college[(college['CITY'] == 'Miami') & (college['STABBR'] == 'FL')].equals(college.loc['Miami, FL']))
```

#### Output
```
False
True
3.13 ms ± 27.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
None
1.66 ms ± 35.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
None
559 µs ± 20.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
None
True
CITY                  Stanford
STABBR                      CA
HBCU                         0
MENONLY                      0
WOMENONLY                    0
RELAFFIL                     0
SATVRMID                   730
SATMTMID                   745
DISTANCEONLY                 0
UGDS                      7018
UGDS_WHITE              0.3752
UGDS_BLACK              0.0591
UGDS_HISP               0.1607
UGDS_ASIAN              0.1979
UGDS_AIAN               0.0114
UGDS_NHPI               0.0038
UGDS_2MOR               0.1067
UGDS_NRA                0.0819
UGDS_UNKN               0.0031
PPTUG_EF                     0
CURROPER                     1
PCTPELL                 0.1556
PCTFLOAN                0.1256
UG25ABV                 0.0401
MD_EARN_WNE_P10          86000
GRAD_DEBT_MDN_SUPP       12782
Name: Stanford University, dtype: object
2.93 ms ± 34 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
None
512 µs ± 1.71 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
None
                                 INSTNM      CITY STABBR  HBCU  MENONLY  \
ARTESIA, CA           Angeles Institute   ARTESIA     CA   0.0      0.0
Aberdeen, SD       Presentation College  Aberdeen     SD   0.0      0.0
Aberdeen, SD  Northern State University  Aberdeen     SD   0.0      0.0
Aberdeen, WA       Grays Harbor College  Aberdeen     WA   0.0      0.0
Abilene, TX   Hardin-Simmons University   Abilene     TX   0.0      0.0

              WOMENONLY  RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY    UGDS  \
ARTESIA, CA         0.0         0       NaN       NaN           0.0   114.0
Aberdeen, SD        0.0         1     440.0     480.0           0.0   705.0
Aberdeen, SD        0.0         0     480.0     475.0           0.0  1693.0
Aberdeen, WA        0.0         0       NaN       NaN           0.0  1121.0
Abilene, TX         0.0         1     508.0     515.0           0.0  1576.0

              UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  \
ARTESIA, CA       0.0175      0.2193     0.3860      0.3158     0.0000
Aberdeen, SD      0.6525      0.1163     0.0780      0.0128     0.0156
Aberdeen, SD      0.8435      0.0230     0.0319      0.0112     0.0207
Aberdeen, WA      0.7110      0.0169     0.0946      0.0214     0.0312
Abilene, TX       0.7126      0.0742     0.1472      0.0076     0.0019

              UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  \
ARTESIA, CA      0.0263     0.0175    0.0088     0.0088    0.0000         1
Aberdeen, SD     0.0000     0.0284    0.0142     0.0823    0.2865         1
Aberdeen, SD     0.0030     0.0219    0.0425     0.0024    0.1872         1
Aberdeen, WA     0.0054     0.0937    0.0009     0.0250    0.1820         1
Abilene, TX      0.0006     0.0298    0.0159     0.0102    0.0685         1

              PCTPELL  PCTFLOAN  UG25ABV MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
ARTESIA, CA    0.6275    0.8138   0.5429             NaN              16850
Aberdeen, SD   0.4829    0.7560   0.3097           35900              25000
Aberdeen, SD   0.2272    0.4303   0.1766           33600              24847
Aberdeen, WA   0.4530    0.1502   0.5087           27000              11490
Abilene, TX    0.3256    0.5547   0.0982           38700              25864
                                              INSTNM   CITY STABBR  HBCU  \
Miami, FL        New Professions Technical Institute  Miami     FL   0.0
Miami, FL               Management Resources College  Miami     FL   0.0
Miami, FL                   Strayer University-Doral  Miami     FL   NaN
Miami, FL                   Keiser University- Miami  Miami     FL   NaN
Miami, FL  George T Baker Aviation Technical College  Miami     FL   0.0

           MENONLY  WOMENONLY  RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY  \
Miami, FL      0.0        0.0         0       NaN       NaN           0.0
Miami, FL      0.0        0.0         0       NaN       NaN           0.0
Miami, FL      NaN        NaN         1       NaN       NaN           NaN
Miami, FL      NaN        NaN         1       NaN       NaN           NaN
Miami, FL      0.0        0.0         0       NaN       NaN           0.0

            UGDS  UGDS_WHITE  UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  \
Miami, FL   56.0      0.0179      0.0714     0.9107      0.0000        0.0
Miami, FL  708.0      0.0071      0.0523     0.9407      0.0000        0.0
Miami, FL    NaN         NaN         NaN        NaN         NaN        NaN
Miami, FL    NaN         NaN         NaN        NaN         NaN        NaN
Miami, FL  649.0      0.0894      0.1263     0.7735      0.0046        0.0

           UGDS_NHPI  UGDS_2MOR  UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  \
Miami, FL     0.0000     0.0000       0.0        0.0    0.4464         1
Miami, FL     0.0000     0.0000       0.0        0.0    0.0000         1
Miami, FL        NaN        NaN       NaN        NaN       NaN         1
Miami, FL        NaN        NaN       NaN        NaN       NaN         1
Miami, FL     0.0015     0.0046       0.0        0.0    0.5686         1

           PCTPELL  PCTFLOAN  UG25ABV    MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
Miami, FL   0.8701    0.6780   0.8358              18700               8682
Miami, FL   0.4239    0.5458   0.8698  PrivacySuppressed              12182
Miami, FL      NaN       NaN      NaN              49200            36173.5
Miami, FL      NaN       NaN      NaN              29700              26063
Miami, FL   0.2567    0.0000   0.4366              38600  PrivacySuppressed
5.57 ms ± 96.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
None
547 µs ± 3.79 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
None
True
```

### Gaining perspective on stock prices
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import InteractiveShell


inter = InteractiveShell()
inter.get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_columns = 50

slb = pd.read_csv('data/slb_stock.csv', index_col='Date', parse_dates=['Date'])
print(slb.head())

slb_close = slb['Close']
slb_summary = slb_close.describe(percentiles=[.1, .9])
print(slb_summary)

upper_10 = slb_summary.loc['90%']
lower_10 = slb_summary.loc['10%']
criteria = (slb_close < lower_10) | (slb_close > upper_10)
slb_top_bottom_10 = slb_close[criteria]

slb_close.plot(color='black', figsize=(12,6))
slb_top_bottom_10.plot(marker='o', style=' ', ms=4, color='lightgray')

xmin = criteria.index[0]
xmax = criteria.index[-1]
print(plt.hlines(y=[lower_10, upper_10], xmin=xmin, xmax=xmax,color='black'))

slb_close.plot(color='black', figsize=(12,6))
plt.hlines(y=[lower_10, upper_10],
           xmin=xmin, xmax=xmax,color='lightgray')
plt.fill_between(x=criteria.index, y1=lower_10,
                 y2=slb_close.values, color='black')
plt.fill_between(x=criteria.index,y1=lower_10,
                 y2=slb_close.values, where=slb_close < lower_10,
                 color='lightgray')
plt.fill_between(x=criteria.index, y1=upper_10,
                 y2=slb_close.values, where=slb_close > upper_10,
                 color='lightgray')
```
