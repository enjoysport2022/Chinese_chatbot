# -*- coding: utf-8 -*-

from gensim import models

model = models.Word2Vec.load('word2vec.model')

print("提供 3 种测试模式\n")
print("输入一个词，寻找top10的相似词")
print("输入两个词，计算相似度")
print("输入三个词，进行类比推理")


query = input()
q_list = query.split()

if len(q_list) == 1:
    print("相似词语top10:")
    res = model.most_similar(q_list[0],topn = 10)
    for item in res:
        print(item[0]+","+str(item[1]))

elif len(q_list) == 2:
    print("计算 Cosine 相似度")
    res = model.similarity(q_list[0],q_list[1])
    print(res)
else:
    print("%s之于%s，如%ss之于" % (q_list[0],q_list[2],q_list[1]))
    res = model.most_similar([q_list[0],q_list[1]], [q_list[2]], topn= 10)
    for item in res:
        print(item[0]+","+str(item[1]))