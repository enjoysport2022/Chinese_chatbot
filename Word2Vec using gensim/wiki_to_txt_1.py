# -*- coding: utf-8 -*-

import logging
import sys
from gensim.corpora import WikiCorpus

def main():
    if len(sys.argv) != 2:
        print("Usage: python2" + sys.argv[0] + "wiki_data_path")
        exit()

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(massage)s',level=logging.INFO)
    wiki_corpus = WikiCorpus(sys.argv[1],dictionary={})
    texts_num = 0

    with open('wiki_texts.txt','w',encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num +=1
            if texts_num %10000 ==0:
                logging.info("已处理 %d篇文章" %texts_num)

if __name__ == "__main__":
    main()

# python3 wiki_to_txt_1.py zhwiki-20160820-pages-articles.xml.bz2