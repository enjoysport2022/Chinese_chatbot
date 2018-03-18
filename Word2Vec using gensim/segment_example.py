# -*- coding: utf-8 -*-
import jieba

seg_list = jieba.cut("我来自中山大学")

print("Default Mode:"+"/ ".join(seg_list))