from gensim.models import word2vec
from util.word_utils import segment_sen
from util.word_utils import sent2vec
import numpy

# 载入模型
model = word2vec.Word2Vec.load('word2vec.model')

message = ''
while message != 'quit':
    message = input("问题：")
    if message != 'quit':
        sen = segment_sen(message)
        vec = sent2vec(model, sen)
        if isinstance(vec, numpy.ndarray):
            words = model.wv.similar_by_vector(vec, topn=3000)
            for word in words:
                if word[0] in ["外观", "内饰", "空间", "动力", "操控", "油耗", "舒适性", "性价比", "售前售后"]:
                    print(word)
                    break
    print("-------------------------------------")
