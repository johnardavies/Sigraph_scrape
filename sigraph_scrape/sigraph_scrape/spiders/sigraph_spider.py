import scrapy
import time
import re
#from scrapy.spider import Spider
from scrapy.selector import Selector
from sigraph_scrape.items import  SigraphScrapeItem

class SiggraphSpider(scrapy.Spider):
    name = "siggraph"
    def __init__(self):
        self.page_number=1 #initialises the class with a page number of 1
        
    def start_requests(self):
        print ('hello')
        number_of_pages=2 #6 #This sets the number of pages that are looped through
        for i in range(self.page_number, number_of_pages, 1):  #Loops through the pages between page_number and number_of_pages
         time.sleep(20) #Adds in a 5 second time delay 
         URL='https://digitalartarchive.siggraph.org/writings/papers/?pg='+str(i)+''
         print (URL)
         yield scrapy.Request(url=URL , callback= self.parse)
    

    def parse(self, response):
        hxs = Selector(response)
        print (hxs)
        items=[]
        followers=hxs.xpath('//p').extract()
        for elem in followers: #loops through the returned titles
           print(elem)
           item=SigraphScrapeItem()
           #This extracts the userid from the hyperlink, probably better with a regex
          # item["names"]=name
           item["text"]=elem
           items.append(item)#sticks the next returned list into the items list
        return items # returns the list

