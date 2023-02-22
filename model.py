import numpy as np
import pandas as pd
import MeCab
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
from gensim.utils import simple_preprocess as preprocess
  
def wakati_by_mecab(style):
    tagger = MeCab.Tagger('')
    tagger.parse('') 
    node = tagger.parseToNode(style)
    word_list = []
    while node:
        pos = node.feature.split(",")[0]
        if pos in ["名詞", "動詞", "形容詞","形容動詞"]:   # 対象とする品詞
            word = node.surface
            word_list.append(word)
        node = node.next
    return word_list



def model(text):
    model = Doc2Vec.load('model original/smashbros3.model')
    #model.dv = model.__dict__['docvecs']
    #model.dv.norms = None
    fighter_list=model.docvecs.most_similar([model.infer_vector((text))])
    #fighter_list=model.dv.most_similar([style])
    return fighter_list[0][0],fighter_list[1][0],fighter_list[2][0],fighter_list[3][0],fighter_list[4][0]









#def model(style):
    #model = Doc2Vec.load('model original/smashbros3.model') 
    #model.dv = model.__dict__['docvecs']
    #model.dv.norms = None
    #fighter_list=model.dv.most_similar([style])
    #return fighter_list[0][0],fighter_list[1][0],fighter_list[2][0],fighter_list[3][0],fighter_list[4][0]
