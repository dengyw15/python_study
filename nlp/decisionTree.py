from math import log
from operator import *


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')  # pickle默认方式是二进制，需要制定'wb'
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')  # 需要制定'rb'，以byte形式读取
    return pickle.load(fr)


def createDataSet():
    '''
    dataSet=[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    '''
    dataSet = [['sunny', 'hot', 'high', 'weak', 'no'],
               ['sunny', 'hot', 'high', 'strong', 'no'],
               ['overcast', 'hot', 'high', 'weak', 'yes'],
               ['rain', 'mild', 'high', 'weak', 'yes'],
               ['rain', 'cool', 'normal', 'weak', 'yes'],
               ['rain', 'cool', 'normal', 'strong', 'no'],
               ['overcast', 'cool', 'normal', 'strong', 'yes'],
               ['sunny', 'mild', 'high', 'weak', 'no'],
               ['sunny', 'cool', 'normal', 'weak', 'yes'],
               ['rain', 'mild', 'normal', 'weak', 'yes'],
               ['sunny', 'mild', 'normal', 'strong', 'yes'],
               ['overcast', 'mild', 'high', 'strong', 'yes'],
               ['overcast', 'hot', 'normal', 'weak', 'yes'],
               ['rain', 'mild', 'high', 'strong', 'no']]
    labels = ['outlook', 'temperature', 'humidity', 'wind']
    return dataSet, labels


def calcShannonEnt(dataSet):  # 计算香农熵
    numEntries = len(dataSet)

    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 取得最后一列数据，该属性取值情况有多少个
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    # 计算熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)

    return shannonEnt


# 定义按照某个特征进行划分的函数splitDataSet
# 输入三个变量（待划分的数据集，特征，分类值）
# axis特征值中0代表no surfacing，1代表flippers
# value分类值中0代表否，1代表是
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:  # 取大列表中的每个小列表
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)

    return retDataSet  # 返回不含划分特征的子集


def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInforGain = 0
    bestFeature = -1

    for i in range(numFeature):
        featList = [number[i] for number in dataSet]  # 得到某个特征下所有值（某列）
        uniquelVals = set(featList)  # set无重复的属性特征值，得到所有无重复的属性取值

        # 计算每个属性i的概论熵
        newEntropy = 0
        for value in uniquelVals:
            subDataSet = splitDataSet(dataSet, i, value)  # 得到i属性下取i属性为value时的集合
            prob = len(subDataSet) / float(len(dataSet))  # 每个属性取值为value时所占比重
            newEntropy += prob * calcShannonEnt(subDataSet)
        inforGain = baseEntropy - newEntropy  # 当前属性i的信息增益

        if inforGain > bestInforGain:
            bestInforGain = inforGain
            bestFeature = i

    return bestFeature  # 返回最大信息增益属性下标


# 递归创建树,用于找出出现次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:  # 统计当前划分下每中情况的个数
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items, key=operator.itemgetter(1), reversed=True)  # reversed=True表示由大到小排序
    # 对字典里的元素按照value值由大到小排序

    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 创建数组存放所有标签值,取dataSet里最后一列（结果）
    # 类别相同，停止划分
    if classList.count(classList[-1]) == len(classList):  # 判断classList里是否全是一类，count() 方法用于统计某个元素在列表中出现的次数
        return classList[-1]  # 当全是一类时停止分割
    # 长度为1，返回出现次数最多的类别
    if len(classList[0]) == 1:  # 当没有更多特征时停止分割，即分到最后一个特征也没有把数据完全分开，就返回多数的那个结果
        return majorityCnt(classList)
    # 按照信息增益最高选取分类特征属性
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 返回分类的特征序号,按照最大熵原则进行分类
    bestFeatLable = labels[bestFeat]  # 该特征的label, #存储分类特征的标签

    myTree = {bestFeatLable: {}}  # 构建树的字典
    del (labels[bestFeat])  # 从labels的list中删除该label

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLables = labels[:]  # 子集合 ,将labels赋给sublabels，此时的labels已经删掉了用于分类的特征的标签
        # 构建数据的子集合，并进行递归
        myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLables)
    return myTree


if __name__ == "__main__":
    my_Data, labels = createDataSet()

    # print(calcShannonEnt(my_Data))
    Mytree = createTree(my_Data, labels)
    print(Mytree)