## Tests

### Preliminary

```
pip install nose
```

### Testing

```
# root of this repository
nosetests -sv
```

Note: This repository is not package, so we added root to path forcibly.

```
sys.path.append(os.getcwd())
```

Please run testing command at root.
