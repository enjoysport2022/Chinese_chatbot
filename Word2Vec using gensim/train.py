# -*- coding: utf-8 -*-

import logging
from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence('wiki_seg.txt')
    model = word2vec.Word2Vec(sentences, size=250)

    # 保存模型
    model.save("word2vec.model")

    # 保留二进制文件
    model.wv.save_word2vec_format('word2vec.bin')

    # 读取模型
    model = word2vec.Word2Vec.load('word2vec.model')

if __name__ == "__main__":
    main()