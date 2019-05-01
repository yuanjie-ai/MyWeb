<h1 align = "center">:rocket: Yuan :facepunch:</h1>

---
> 数据不是创造规律,而是展示那些原本的规律

https://www.kaggle.com/c/elo-merchant-category-recommendation/discussion/82055#479196
[Competitions][1]

---
## Install
```
pip install Yuan
```
## Usage
#### `from yuan.pipe import *`
```python
@X
def xfunc1(x):
    _ = x.split()
    print(_)
    return _
@X
def xfunc2(x):
    _ = '>>'.join(x)
    print(_)
    return _

'I am very like a linux pipe' | xfunc1 | xfunc2
```
- `xtqdm`

    ![tqdm](pic/tqdm.png)

- `xfilter / xmap / xsort / xreduce`
```python
iterable | xfilter(lambda x: len(x) > 1) | xmap(str.upper) | xsort | xreduce(lambda x, y: x + '-' + y)

'AM-LIKE-LINUX-PIPE-VERY'
```

- `xsummary`
```python
iterable | xsummary

counts               7
uniques              7
missing              0
missing_perc        0%
types           unique
Name: iterable, dtype: object
```
- ...

---
[1]: https://iphysresearch.github.io/DataSciComp/?sub=PF,IT,AC,DM,CV,NLP,RL,SP
