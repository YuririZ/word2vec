from gensim.models import fasttext
from gensim.models import word2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
import logging
from util.word_utils import segment_sen


# 文件路径
train_path = "D://PYTHON//word2vec//data//train_data_1.csv"
learn_path = "D://PYTHON//word2vec//data//learn_path.csv"
stop_path = "D://PYTHON//word2vec//data//stopword.txt"

# 读取数据
data = pd.read_csv(learn_path, encoding='gbk', header=None)
# 停用词
stop_words = [line.strip().decode('utf-8') for line in open(stop_path, "rb").readlines()]
# 构造数据
sentance = list(data[1])

# 分词后的结果
sens_list = [segment_sen(i) for i in sentance]
label_list = list(data[0])

documents = [TaggedDocument(doc, [label]) for doc, label in zip(sens_list,label_list)]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
doc_model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
doc_model.save("doc2vec.model")

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# model = word2vec.Word2Vec(sens_list, min_count=1, iter=20)
# model.save("word2vec.model")
