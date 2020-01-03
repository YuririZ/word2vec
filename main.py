import pandas as pd
from common.constant import Constant
from service.py_service import segment_sen
from util.data_utils import list2csv

# 读取数据
row_data = pd.read_csv(Constant.classification_segment_data_path_csv, encoding='utf-8', header=None)

labels = row_data[0]
sentences = row_data[1]

for sen in sentences:
    print(sen)

print(sentences)

# out_list = []
# for label, sentence in zip(labels, sentences):
#     seg_list = segment_sen(sentence)
#     seg_str = ",".join(seg_list)
#     temp_list = [label, seg_str]
#     print(temp_list)
#     out_list.append(temp_list)
#
# # 写入数据
# list2csv(out_list, Constant.classification_segment_data_path_csv)
