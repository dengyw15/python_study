import codecs
import jieba
import math
def loadData():
    #读入停用词
    with codecs.open(filename='J:/tmp/data/nlp/stop_words.txt', mode='r') as stop_words:
        lines = stop_words.readlines()
        list_stop_words = [line.strip() for line in lines]

    #读入文本集
    with codecs.open(filename='J:/tmp/data/nlp/allNews.csv', mode='r') as content:
        lines = content.readlines()
        list_content = [line.strip() for line in lines]

    # for l in list_content:
    #     line_cut = jieba.cut(l)
    #     newsContent = [word for word in line_cut if word not in list_stop_words]
    #     print(newsContent)
    #     break
    #分词
    list_content_cutted = []
    # for art in [jieba.cut(oneContent) for oneContent in list_content]:
    #     print(art)
    for oneContent in list_content:
        line_cut = jieba.cut(oneContent)
        list_content_cutted.append([word for word in line_cut if word not in list_stop_words])
    return list_content_cutted

def computTf(word, list_content, index):
    no_word = 0
    print(list_content[index])
    for w in list_content[index]:
        if w == word:
            no_word += 1
    return no_word/len(list_content[index])

def computIDF(word, list_content):
    no_art_word = 0
    for con in list_content:
        if word in con:
            no_art_word += 1
    return math.log10(len(list_content) / (1+no_art_word))

def getContentCut(content, list_stop_words):
    content_cut = jieba.cut(content)
    list_content_cut = [word for word in content_cut if word not in list_stop_words]
    return list_content_cut

def computTf1(word, content):
    no_word = 0
    # print(content)
    for w in content:
        if w == word:
            no_word += 1
    # print(no_word)
    # print(len(content))
    return no_word / len(content)

def computIDF1(word, all_content):
    no_art_word = 0
    for content in all_content:
        if word in content:
            no_art_word += 1
    return math.log10(len(all_content) / (1+no_art_word))

if __name__ == '__main__':
    with codecs.open(filename='J:/tmp/data/nlp/stop_words.txt', mode='r') as stop_words:
        lines = stop_words.readlines()
        list_stop_words = [line.strip() for line in lines]
        # 读入文本集
    with codecs.open(filename='J:/tmp/data/nlp/allNews.csv', mode='r') as content:
        lines = content.readlines()
        list_content = [line.strip() for line in lines]
    list_content_cut = getContentCut(list_content[0], list_stop_words)
    for word in list_content_cut:
        tf = computTf1(word, list_content_cut)
        idf = computIDF1(word, list_content)
        print(word, tf*idf)

    # list_content = loadData()
    # tf = computTf('财务', list_content, 0)
    # print(tf)
    # idf = computIDF('财务', list_content)
    # print(idf)
