from scrapy import Selector
from requests import get

doc = '''
    <div>
        <ul>
            <li class="item-0"><a href="like1.html">first item</a></li>
            <li class="item-01"><a href="like11.html">first item</a></li>
            <li class="item-01active"><a href="like11.html">first item</a></li>
        </ul>
    </div>
'''
sel = Selector(text=doc, type="html")
# print(sel.xpath("//li[@class]").extract())
# print(sel.xpath("//li[re:test(@class, 'item-\d+$')]/a/text()").extract())

resp = get("http://wcm.ccb.com/wcmau/ccbcache/zh/ns:LHQ6NixmOjE2ODQsYzoscDosYTosbTo=/channel.vsml")
print(resp.text)

