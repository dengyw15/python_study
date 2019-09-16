import csv
import codecs


def readNewsContent(newspath):
    with codecs.open(newspath, encoding='gbk', mode='r') as file:
        print(file.encoding)
        lines = file.readlines()
        content = ''
        for line in lines:
            line = line.strip()
            if line != '':
                content = content + line
        return content

def readIndexFile(indexFile):
    with codecs.open(indexFile, 'r', 'utf-8') as indexFile:
        i = 0
        # while True:
        #     line = indexFile.readline()
        #     if line:
        #         print(line)
        #         i = i+1
        #     else:
        #         break
        datas = []
        j = 0
        for line in indexFile:
            j = j+1
            oneline = line.strip().split('|@|')
            onedata = []
            for i in range(0, len(oneline) - 1):
                content = oneline[i]
                if i == 2:
                    print(content)
                    content = readNewsContent('H:/news/allNews/' + oneline[i])
                onedata.append(content)
            datas.append(onedata)
            if j == 10000:
                writeCvsFile(datas)
                datas=[]
                j=0



def writeCvsFile(datas):
    with open(file='H:/news/allNews.csv', mode='a', encoding='gbk', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(datas)


readIndexFile('H:/news/allNews/indexFiles/FinanceNews_All_20180131151307.dat')

# with open('h:/names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'B,eans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
#
# with open('h:/names.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['first_name'])
