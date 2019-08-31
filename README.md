# [Cerebra](cerebra.ai)-NER

### NER system based on [deepPavlov](https://github.com/deepmipt/DeepPavlov) openSource library

## Requirements:

1. DeepPavlov [link](https://github.com/deepmipt/DeepPavlov)

2. Mystem [link](https://github.com/nlpub/pymystem3)



## Example of usage:

### initialization

```python
from NER import NER
ner = NER()
```

### Extract named entities

```python
result = ner.extract(input)
```

### Pars extraction result

```python
parsed = ner.pars(result)
```

### Save result to .json file

```python
ner.to_json(parsed)
```
