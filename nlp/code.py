import codecs
from numpy import *
import csv

# with codecs.open(filename='J:/tmp/data/code.txt', mode='r', encoding='utf-8') as file:
#     lines = file.readlines()
#     codes = []
#     print("开始读取新闻codes...")
#     for line in lines:
#         # print(line.strip().split('|'))
#         for code in line.strip().split('|')[0].split(' '):
#             if code.strip() != '' and code not in codes:
#                 codes.append(code)
#     print(codes)
#     print(len(codes))


def writeCsvFile(filename, csvdatas) :
    with open(file='J:/tmp/data/' + filename, mode='a', encoding='gbk', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvdatas)

with codecs.open(filename='J:/tmp/data/all_distinct_codes.txt', mode='r', encoding='utf-8') as codesFile:
    line = codesFile.readline()

    stkCodes =[]  #股票代码
    idxCodes = []  #指数代码
    fncPrdCodes = [] #金融产品代码
    otherCodes = [] #其他代码
    newsCode = [] #新闻代码
    futureCode = [] #期货代码

    for code in line.split(','):
        # print(code)
        if len(code) > 20:
            continue
        # elif '.HK' in code or '.SS' in code or '.SZ' in code or '.KS' in code:
        elif code.count('.') > 0 and code.index('.') != 0 and code.index('.') != (len(code) - 1):
            stkCodes.append(code)
        elif code.count('.') > 0 and code.index('.') == 0:
            idxCodes.append(code)
        elif code.count('=') > 0 and code.index('=') >= 0:
            fncPrdCodes.append(code)
        elif code.count('/') > 0 and code.index('/') >= 0:
            newsCode.append(code)
        elif code.count('0#') > 0 and code.index('0#') == 0 and code.count(':') > 0 and code.index(':') == (len(code) - 1):
            futureCode.append(code)
        else:
            otherCodes.append(code)

with codecs.open(filename='J:/tmp/data/reuters_code.txt', mode='r', encoding='utf-8') as allNewsCodeFile:
    lines = allNewsCodeFile.readlines()

    newsCodeNum = zeros(len(newsCode))
    otherCodeNum = zeros(len(otherCodes))

    for line in lines:
        for code in line.strip().split('|')[0].split(' '):
            if code.strip() != '' and len(code) < 20:
                if code.strip() in newsCode:
                    newsCodeNum[newsCode.index(code.strip())] += 1
                elif code.strip() in otherCodes:
                    otherCodeNum[otherCodes.index(code.strip())] += 1

    print(len(newsCodeNum))
    print(len(newsCode))
    print(len(otherCodeNum))
    print(len(otherCodes))
    csvdatas = []
    for i in range(len(newsCodeNum)):
        onecsvdata = [newsCode[i], newsCodeNum[i]]
        csvdatas.append(onecsvdata)

    csvdatas1 = []
    for j in range(len(otherCodeNum)):
        onecsvdata1 = [otherCodes[j], otherCodeNum[j]]
        csvdatas1.append(onecsvdata1)

    writeCsvFile('news_cod_num.csv', csvdatas)
    writeCsvFile('oth_cod_num.csv', csvdatas1)




    # print('股票相关代码,共计{0}个===================='.format(len(stkCodes)))
    # print(stkCodes)
    # print('指数相关代码,共计{0}个===================='.format(len(idxCodes)))
    # print(idxCodes)
    # print('路透金融产品相关代码,共计{0}个===================='.format(len(fncPrdCodes)))
    # print(fncPrdCodes)
    # print('新闻代码,共计{0}个===================='.format(len(newsCode)))
    # print(newsCode)
    # print('期货产品代码,共计{0}个===================='.format(len(futureCode)))
    # print(futureCode)
    # print('其他代码,共计{0}个===================='.format(len(otherCodes)))
    # print(otherCodes)