from gensim.models import Doc2Vec
from util.word_utils import segment_sen
from util.word_utils import sent2vec
import pandas as pd
import random
from common.constant import Constant


# 载入模型
model = Doc2Vec.load('doc2vec.model')

# 读取数据
data = pd.read_csv(Constant.classification_segment_data_path_csv, encoding='utf-8', header=None)

# 构造数据
sens_list = list(data[1])
labels = list(data[0])
random.seed(123)
random.shuffle(sens_list)
random.seed(123)
random.shuffle(labels)
sens_list = sens_list[int(len(sens_list) * 0.8) + 1: int(len(sens_list))]
labels = labels[int(len(labels) * 0.8) + 1: int(len(labels))]


right = 0
left = len(labels)
for sen, label in zip(sens_list, labels):
    print(left)
    words = segment_sen(sen)
    vec = sent2vec(model, words)
    try:
        sims = model.docvecs.most_similar([vec],topn=1)
    except:
        print(sen)
    if sims[0][0] == label:
        right += 1
    left -= 1
accuracy_rate = right/len(labels)
print(accuracy_rate)

# input = "不会亏，但是二手车同样因为高保值率，会显得不是很有性价比，如果预算不是有限，建议直接买新车。但是依旧有好多车主选择二手，选择开了十年甚至5年依旧售价不低的飞度，这是为什么？先说4－5万这个价位，可供选择的二手车不少，但是综合表现能够媲美飞度的还是少之又少，尤其是结合油耗和稳定可靠性来看，"

# inferred_vector_dm = model.infer_vector(words)
# print(inferred_vector_dm)

# sims = model.docvecs.most_similar([vec])
# print(sims)

# vec = model.wv[input]
# print(vec)


# result = model.wv.similar_by_vector(vec)

# print(result)
