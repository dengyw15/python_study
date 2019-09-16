from bs4 import BeautifulSoup as bs
from urllib import request

# response = request.urlopen("http://icsp.jh:1340/ICSPWeb/jsp/rics/realIndex.jsp?viewtype=index&LinkFlag=dgmh");
# fi = open("H:/test.txt", "w+");
# fi.write(str(response.read(),"UTF-8"));
soup = bs(open("H:/test.txt"), "html.parser");
imgContent = soup.find("img", src="/ICSPWeb/rics_img/news_title_a.gif");
# print(imgContent)
for c in imgContent:
    print(str(c) + "=========================")
# imgSoup = bs(imgContent, "html.parser")
# print(imgSoup.prettify())