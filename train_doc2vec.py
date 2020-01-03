from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import logging

from common.constant import Constant
from util.word_utils import segment_sen

# 读取数据
data = pd.read_csv(Constant.classification_data_path_csv, encoding='utf-8', header=None)

# 构造数据
labels = data[0]
sentences = data[1]

# 分词后的结果
sens_list = []
for sen in sentences:
    if isinstance(sen, str):
        sens_list.append(sen.split(","))
    else:
        sens_list.append([str(sen)])

# sens_list = list(data[1])
label_list = list(data[0])
documents = [TaggedDocument(doc, [label]) for doc, label in zip(sens_list, label_list)]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
doc_model = Doc2Vec(documents, size=100, window=10, min_count=5, workers=11, alpha=0.025, min_alpha=0.025)
doc_model.save("doc2vec.model")
