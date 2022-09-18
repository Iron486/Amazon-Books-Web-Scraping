import scrapy
from scrapy.crawler import CrawlerProcess

class FirstWebsiteSpider(scrapy.Spider):
    name = 'first_website'
    allowed_domains = [r"www.amazon.com"]
    start_urls = [r"http://www.amazon.com/s?k=data+science&i=stripbooks-intl-ship&crid=1YWU6OJK4L3BA&sprefix=data+science%2Cstripbooks-intl-ship%2C247&ref=nb_sb_ss_ts-doa-p_4_12"]

    def parse(self, response):
        title=response.xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/span/text()").getall()
        authors=[]
        box=response.xpath("//div[@class='a-row']")
        for i in box:
            author=i.xpath("//div[@class='a-row']/a[@class='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-     style']/text() | ( //div[@class='a-row']/span[@class='a-size-base']/text()").getall()
            authors.append(author)    
        yield {'titles':title,'authors':author}
#//div[@class='a-row']/a[@class='a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style']/text() | ( //div[@class='a-#row']/span[@class='a-size-base']/text()
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start()