import jieba
import numpy as np

# 文件路径
stop_path = "D://PYTHON//data//stopword.txt"
dict_path = "D://PYTHON//data//dict.txt"
# 停用词
stop_words = [line.strip().decode('utf-8') for line in open(stop_path, "rb").readlines()]
# 分词字典
jieba.load_userdict(dict_path)


def segment_sen(sen):
    '''
    返回去停用词后的分词结果
    :param sen:
    :return:
    '''
    sen_list = []
    sens_list_with_stop_word = []
    try:
        sen_list = jieba.lcut(sen)
        # 去停用词
        for word in sen_list:
            if word in stop_words or word == '\n':
                continue
            else:
                sens_list_with_stop_word.append(word)
    except:
        pass
    return sens_list_with_stop_word


def sent2vec(model, words):
    '''
    文本转换成向量
    :param model:
    :param words:
    :return:
    '''
    vect_list = []
    for w in words:
        try:
            vect_list.append(model.wv[w])
        except:
            continue
    vect_list = np.array(vect_list)
    vect = vect_list.sum(axis=0)
    try:
        return vect / np.sqrt((vect ** 2).sum())
    except:
        pass
    return vect
