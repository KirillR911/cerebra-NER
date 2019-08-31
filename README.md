# [Cerebra](cerebra.ai)-NER

### NER system based on [deepPavlov]([https://github.com/deepmipt/DeepPavlov](https://github.com/deepmipt/DeepPavlov) openSource library

Example of usage: 

### Inicialization

```python
from NER import NER
ner = NER()
```

### Extract named entities

```python
result = NER.extract(input)
```

### Pars extraction result

```python
parsed = NER.pars(result)
```

### Save result to .json file

```python
ext.to_json(parsed)
```
