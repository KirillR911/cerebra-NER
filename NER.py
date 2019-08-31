from deeppavlov import configs, build_model
import sys
from pymystem3 import Mystem

import warnings
warnings.filterwarnings("ignore", category= DeprecationWarning)
class NER():

    '''
        NER module for Named Entity Recognition
        Uses deepPavlov ner model 
        extract to extract ne 
        pars to default pars of extraction result 
    '''
    def __init__(self, model_name = 'ner_ontonotes_bert_mult'):
        print('Started loading model')
        if model_name == 'ner_ontonotes_bert_mult':
            self.ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)
        elif model_name == 'ner_rus_bert' :
            print('WARNING!: ner_ontonotes_bert_mult appears to show better result, so we recomend to choose this model\n\
                instead of ner_rus_bert!')
            self.ner_model = build_model(configs.ner.ner_rus_bert, download=True)
        print('Model is ready to go!')
    def extract(self, s):
        '''
            Extract nemed entity from string 
            input: String 
            output: List of (word, tag) pairs
        '''
        extraction = (self.ner_model([s]))
        return list(zip(extraction[0][0], extraction[1][0]))
    def pars(self, result, lemmataize = True):
        '''
            Pars extraction to dict, where keys are tags and they include lists of words for every entity 
            lemmatize -- Flag to lemmatize text with Mystem by Yandex®
            input: extraction result 
            output: dictionary {tag: [[words], [words]]}
        '''

        if lemmataize:
            m = Mystem()
        d = {}
        s = []
        for word, tag in result:
            if  tag == 'O':
                if len(s) != 0:
                    if key_tag in d.keys():
                        d[key_tag].append(s)
                    else:
                        d[key_tag] = [s]
                    s = []
                else:
                    continue
            elif tag[0] == 'B':
                key_tag = tag[2:]
                s = []
                if lemmataize and key_tag != 'ORG':
                    word = m.lemmatize(word)[0]
                s.append(word)
            elif tag[0] == 'I':
                if lemmataize and key_tag != 'ORG':
                    word = m.lemmatize(word)[0]
                s.append(word)
        return d
        
    def to_json(self, d):
        import json
        with open("NER.json", "w") as fp:
            json.dump(d , fp) 


