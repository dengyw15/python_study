import re
import random


def get_useragent():
    user_agents = ['Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                   , 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
                   ,  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)'
                   , 'Opera/9.27 (Windows NT 5.2; U; zh-cn)'
                   , ' Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
                   ]
    return user_agents[random.randint(0, len(user_agents) - 1)]

print(get_useragent())

