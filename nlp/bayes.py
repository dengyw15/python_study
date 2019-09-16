from numpy import *
import jieba

#构建数据集
def loadDataSet():
    # postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
    #               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid', 'dog'],
    #               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    #               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    #               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
    #               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # classVec = [0, 1, 0, 1, 0, 1]  #1表示负面言论，0表示正常言论
    chnsName = ['A股', '贵金属', '基金', '期货', '外汇']
    classCode = ['0', '1', '2', '3', '4']
    #读入停用词
    with open(file="J:/tmp/data/nlp/stop_words.txt", mode='r') as stopWords:
        lines = stopWords.readlines()
        stop_words = []
        for word in lines:
            stop_words.append(word.strip())

    with open(file="J:/tmp/data/nlp/allNews1.csv", mode='r') as contentFile:
        lines = contentFile.readlines()
        contentList = []
        classVec = []
        for line in lines:
            if len(line.split(',')) > 2:
                continue
            newsContent = line.split(',')[0].strip()
            newsType = line.split(',')[1].strip()

            line_cut = jieba.cut(newsContent)
            #去掉停用词
            newsContent = [word for word in line_cut if word not in stop_words]
            contentList.append(newsContent)
            classVec.append(classCode[chnsName.index(newsType)])

    return contentList, classVec


#构建词汇表生成函数
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document) #取两个集合的并集
    return list(vocabSet)


#词袋模型
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    rest = []
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    # for i in range(0, len(vocabList)):
    #     rest.append(vocabList[i] + ":" + str(returnVec[i]))
    # print(rest)
    return returnVec  #返回非负整数的词向量


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix) #文档数目
    numWord = len(trainMatrix[0]) #词汇表词数目
    p0busive = sum([cate for cate in trainCategory if cate == '0'])/len(trainCategory) #p0, A股文章的概率
    p1busive = sum([cate for cate in trainCategory if cate == '1']) / len(trainCategory)  # p1, 贵金属文章的概率
    p2busive = sum([cate for cate in trainCategory if cate == '2']) / len(trainCategory)  # p2, 基金文章的概率
    p3busive = sum([cate for cate in trainCategory if cate == '3']) / len(trainCategory)  # p3, 期货文章的概率
    p4busive = sum([cate for cate in trainCategory if cate == '4']) / len(trainCategory)  # p4, 外汇文章的概率
    p0Num = zeros(numWord)
    p1Num = zeros(numWord)
    p2Num = zeros(numWord)
    p3Num = zeros(numWord)
    p4Num = zeros(numWord)
    p0Demon = 0
    p1Demon = 0
    p2Demon = 0
    p3Demon = 0
    p4Demon = 0
    for i in range(numTrainDocs):
        if trainCategory[i] == 0:
            p0Num += trainMatrix[i] #向量相加
            p0Demon += sum(trainMatrix[i]) #向量中1累加求和
        elif trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Demon += sum(trainMatrix[i])
        elif trainCategory[i] == 2:
            p2Num += trainMatrix[i]
            p2Demon += sum(trainMatrix[i])
        elif trainCategory[i] == 3:
            p3Num += trainMatrix[i]
            p3Demon += sum(trainMatrix[i])
        elif trainCategory[i] == 4:
            p4Num += trainMatrix[i]
            p4Demon += sum(trainMatrix[i])
    p0Vec = p0Num/p0Demon
    p1Vec = p1Num/p1Demon
    p2Vec = p2Num / p2Demon
    p3Vec = p3Num / p3Demon
    p4Vec = p4Num / p4Demon

    return p0Vec, p1Vec, p2Vec, p3Vec, p4Vec, p0busive, p1busive, p2busive, p3busive, p4busive

if __name__ == "__main__":
    print('开始生成数据集...')
    listPosts, listClasses = loadDataSet()
    print('开始生成词汇表...')
    myVocabList = createVocabList(listPosts)
    print(myVocabList)
    trainMat =[]
    print('生成词袋模型...' + str(len(listPosts)))
    for postinDoc in listPosts:
        trainMat.append(bagOfWords2VecMN(myVocabList, postinDoc))
    print('开始训练模型...')
    p0v, p1v, pAb = trainNB0(trainMat, listClasses)
    print(p0v)
    print(p1v)
    # print(pAb)
    # print(listPosts)
    # print(bagOfWords2VecMN(myVocabList, listPosts[1]))
