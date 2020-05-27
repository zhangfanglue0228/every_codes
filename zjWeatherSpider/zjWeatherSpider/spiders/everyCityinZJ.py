from re import findall
from urllib.request import urlopen
from zjWeatherSpider.items import ZjweatherspiderItem

import scrapy


class EverycityinzjSpider(scrapy.Spider):
    name = "everyCityinZJ"
    allowed_domains = ["www.weather.com.cn"]
    start_urls = []
    # 遍历各城市， 获取要爬取的页面 URL
    url = r"http://www.weather.com.cn/zhejiang/index.shtml"
    with urlopen(url) as fp:
        contents = fp.read().decode()
    pattern = '<a title=".*?" href="(.+?)" target="_blank">(.+?)</a>'
    for url in findall(pattern, contents):
        start_urls.append(url[0])

    def parse(self, response):
        # 处理每个城市的天气预报页面数据
        item = ZjweatherspiderItem()
        city = response.xpath(
            '//div[@class="crumbs fl"]//a[3]//text()'
            ).extract()[0]
        item["city"] = city
        # 每个页面只有一个城市的天气数据， 直接取[0]
        selector = response.xpath('//ul[@class="t clearfix"]')[0]
        # 存放天气数据
        weather = ""
        for li in selector.xpath("./li"):
            date = li.xpath("./h1//text()").extract()[0]
            cloud = li.xpath("./p[@title]//text()").extract()[0]
            high = li.xpath('./p[@class="tem"]//span//text()').extract()[0]
            low = li.xpath('./p[@class="tem"]//i//text()').extract()[0]
            wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0]
            wind = wind + li.xpath('./p[@class="win"]//i//text()').extract()[0]
            weather = weather + date + ":" + cloud + "," + high + r"/" + low + "," + wind + "\n"
        item["weather"] = weather
        return [item]
