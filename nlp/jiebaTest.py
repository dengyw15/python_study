# -*- coding:utf-8 -*-

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

jieba.suggest_freq('沙瑞金', True)
jieba.suggest_freq('易学习', True)
jieba.suggest_freq('王大路', True)
jieba.suggest_freq('京州', True)
jieba.load_userdict('J:/tmp/data/dict.txt')

with open(file='J:/tmp/data/stop_words.txt', mode='rb') as stop_file:
    stpwrd_content = stop_file.read()
    stpwrdlst = stpwrd_content.splitlines()

with open(file='J:/tmp/data/nlp_test0.txt') as f:
    document = f.read()
    # document_decode = document.decode('GBK')
    document_cut = jieba.cut(document)
    result = ' '.join(document_cut)
    # result = result.encode('utf-8')
    with open(file='J:/tmp/data/nlp_test1.txt', mode='w') as f2:
        f2.write(result)

with open(file='J:/tmp/data/nlp_test1.txt', mode='r') as ff:
     res = ff.read()

corpus = [res]
vector = TfidfVectorizer(stop_words=stpwrdlst)
tfidf = vector.fit_transform(corpus)
wordlist = vector.get_feature_names()
weightlist = tfidf.toarray()
print(wordlist)
print(weightlist)
for i in range(len(weightlist)):
    print("-------第{0}段文本词语权重".format(i))
    for j in range(len(wordlist)):
        print(wordlist[j], weightlist[i][j])

