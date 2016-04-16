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

## Debug

### Tokenized Text

```
python check_tweet.py --help
usage: check_tweet.py [-h] ids [ids ...]

positional arguments:
  ids

optional arguments:
  -h, --help  show this help message and exit
```

e.g.

```
python check_tweet.py 554564419162619904 472138319464108033
```

[![https://gyazo.com/521d906d267d5741249e532ec91c3391](https://i.gyazo.com/521d906d267d5741249e532ec91c3391.png)](https://gyazo.com/521d906d267d5741249e532ec91c3391)

## Analysis

### Put Run File and Result

e.g. make `results` directory and put them there

```
$ cd results
$ ls
LSTC-STC/         accuracy-12-5.txt  evaluation_results/     test-final-labeled.txt.zip
SLSTC-STC.tar.gz   accuracy-2-1.txt   evaluation_results.zip
accuracy-12-1.txt  accuracy-2-5.txt   test-final-labeled.txt
```

### Sum results

Once, dump results

e.g.

```
python dump_result.py --run-file results/SLSTC-STC/SLSTC-J-R2.txt
```

Output results

e.g.

```
python output_result.py --dump-file outputs/SLSTC-J-R2.txt.dump
```

If you modify output formet, see [`output_result.py`](./output_result.py).
