# stc

## Preliminary

### Install Dependencies

* MeCab
* https://github.com/mysql/mysql-connector-python
* [progressbar2 3.6.0 : Python Package Index](https://pypi.python.org/pypi/progressbar2)


### Make Dictionary

```
python make_dic.py --help
usage: make_dic.py [-h] [--file-path FILE_PATH] [--overwrite OVERWRITE]

optional arguments:
  -h, --help            show this help message and exit
  --file-path FILE_PATH
  --overwrite OVERWRITE
```

e.g.

```
python make_dic.py --file-path ./data/tweet_dic.pkl --overwrite True
```

[![https://gyazo.com/52fb076f8c095c064fbcf02d03c710c6](https://i.gyazo.com/52fb076f8c095c064fbcf02d03c710c6.png)](https://gyazo.com/52fb076f8c095c064fbcf02d03c710c6)


### Indexing

```
python make_index.py --help
usage: make_index.py [-h] [--file-path FILE_PATH] [--overwrite OVERWRITE]

optional arguments:
  -h, --help            show this help message and exit
  --file-path FILE_PATH
  --overwrite OVERWRITE
```

e.g.

```
python make_index.py --file-path ./data/index.pkl --overwrite True
```

[![https://gyazo.com/a651af765751687771e08cf4c7677a25](https://i.gyazo.com/a651af765751687771e08cf4c7677a25.png)](https://gyazo.com/a651af765751687771e08cf4c7677a25)
