from cerebraner.NER import NER
import warnings
import os
ext = NER()
s = input()
result = ext.extract(s)
print(ext.pars(result))
ext.to_json(ext.pars(result))