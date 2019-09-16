from gensim import corpora, models
import jieba
with open(file='J:/tmp/data/LDA_test.txt', mode='r') as f:
    content = f.readlines()
    #去掉停用词
    stop_list = set("for a of the and to in".split())
    texts = [[word for word in line.strip().lower().split() if word not in stop_list] for line in content]
    print('=============分词后============')
    print(texts)

#构建字典
dictionary = corpora.Dictionary(texts)
#过滤掉出现频率最高的N个单词
# dictionary.filter_n_most_frequent(remove_n=10)

#去掉出现次数低于no_blow的词
#去掉出现次数高于no_above的词。（小数是指百分数）
#在上面基础上，保留出现频率前keep_n的词
# dictionary.filter_extremes(no_below=2, no_above=1, keep_n=1000)

#有两种用法，一种是去掉bad_id对应的词，另一种是保留good_id对应的词而去掉其他词。注意这里bad_ids和good_ids都是列表形式
# dictionary.filter_tokens(bad_ids=['human', 'abc'])

# 在执行完前面的过滤操作以后，可能会造成单词的序号之间有空隙，这时就可以使用该函数来对词典来进行重新排序，去掉这些空隙。
# dictionary.compactify()
dic_len = len(dictionary)
print('==============生成词典=====================')
for item in dictionary.items():
    print(item)
# print(dic_len)
#根据字典，将每行文档都转换为索引形式
corpus = [dictionary.doc2bow(text) for text in texts]
print('====每行文档都转换为索引形式==========')
for line in corpus:
    print(line)
#对每篇文档中的每个词计算tf-idf值
corpus_tfidf = models.TfidfModel(corpus)[corpus]
#打印
print('=======每个词的tf-idf值==========')
for c in corpus_tfidf:
    print(c)
#############以上是特征数据的准备，开始应用LDA模型################
#设置主题的数目
num_topics = 2
#训练模型
lda = models.LdaModel(corpus=corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                      alpha='auto', eta='auto', minimum_probability=0.001)
#打印一下每篇文档被分布在各个主题下的概率
doc_topic = [a for a in lda[corpus_tfidf]]
print('Document Topic')
print(doc_topic)

for topic_id in range(num_topics):
    print("Topic: {0}\n{1}".format(topic_id, lda.show_topic(topic_id)))