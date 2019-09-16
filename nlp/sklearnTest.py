#加载数据
from sklearn.datasets import fetch_20newsgroups
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
n_samples = 2000
data_samples = dataset.data[:n_samples] #截取需要的量

#文本预处理，可选项
def textPrecessing(text):
    #小写化
    text = text.lower()
    #去掉特殊标点
    for c in string.punctuation:
        text = text.replace(c, '')
    #分词
    wordLst = nltk.word_tokenize(text)
    #去掉停用词
    filtered = [w for w in wordLst if w not in stopwords.words('english')]
    # 仅保留名词或特定POS
    refiltered = nltk.pos_tag(filtered)
    filtered = [w for w, pos in refiltered if pos.startswith('NN')]
    #词干化
    ps = PorterStemmer()
    filtered = [ps.stem(w) for w in filtered]
    return " ".join(filtered)

#该区域仅首次运行，进行文本预处理，第二次运行起注释掉
docLst = []
for desc in data_samples :
    docLst.append(textPrecessing(desc).encode('utf-8'))
with open("J:/tmp/data/preRst.txt", 'w') as f:
    for line in docLst:
        f.write(line+'\n')

#==============================================================================
#从第二次运行起，直接获取预处理过的docLst，前面load数据、预处理均注释掉
#docLst = []
#with open(textPre_FilePath, 'r') as f:
#    for line in f.readlines():
#        if line != '':
#            docLst.append(line.strip())
#==============================================================================