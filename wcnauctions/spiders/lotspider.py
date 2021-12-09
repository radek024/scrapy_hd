import scrapy
from wcnauctions.items import WcnauctionsItem
from scrapy.loader import ItemLoader
from datetime import datetime

auctions            = []

# init empty tab for plots purpose
# coinName_arr        = []
# coinCat_arr         = []
# condition_arr       = []
# price_arr           = []
# est_price_arr       = []
# bids_arr            = []
# views_arr           = []
# auctionEnd_d_arr    = []

class LotSpider(scrapy.Spider):
    name = 'lot' 
    start_urls = ['https://wcn.pl/eauctions?older=1']
    #item = WcnauctionsItem()

    def parse(self, response): # main page
        for auction in response.css('div.eauction-inactive'):
            auctionNumber = auction.css('a.nicer::text').get()
            #auctions.append(auctionNumber)
            yield scrapy.Request('https://wcn.pl/eauctions/{}'.format(auctionNumber), self.parse2)
            
    def parse2(self, response): # auction page
        auction_d = response.css('div.eauction-status::text').getall()
        #auctionStart_dt = auction_dt[0]
        auctionEnd_d = auction_d[1]
        for lot in response.css('table.items tbody > tr'):
            l = ItemLoader(item = WcnauctionsItem(), selector=lot)
            
            # optional info - spider_dt
            now = datetime.now()
            spider_dt = now.strftime("%d.%m.%Y %H:%M:%S")
            l.add_value('spider_dt', spider_dt)

            coinName = lot.css('td:nth-child(2) a::text').get().split(',',maxsplit=2)[1]
            l.add_value('name', coinName)
            
            coinCat = lot.css('td:nth-child(2) a::text').get().split(',',maxsplit=2)[0]
            l.add_value('category', coinCat)
            
            l.add_css('condition', 'td:nth-child(3)::text')
            coinPrice = l.add_css('price', 'td:nth-child(4) p:first-child::text')
            l.add_css('est_price', 'td:nth-child(4) p:nth-child(2)::text')
            l.add_css('bids', 'td:nth-child(5)::text')
            l.add_css('views', 'td:nth-child(4) p:last-child::text')
            # all auctions are "Zakonczone" so state isn't helpful 
            l.add_css('state', 'td:nth-child(6)::text')
            #l.add_css('photoUrl', 'td:first-child a::attr(href)')
            #l.add_css('link', 'td:nth-child(2) a::attr(href)')

            photoUrl = lot.css('td:nth-child(2) a::attr(href)').get()
            l.add_value('photoUrl', 'https:/'+photoUrl)

            fullUrl = lot.css('td:nth-child(2) a::attr(href)').get()
            l.add_value('link', 'https://wcn.pl'+fullUrl)
            
            l.add_value('auctionEnd_d', auctionEnd_d)

            yield l.load_item()
            
            # data for plots purpose
            # coinName_arr.append(coinName)
            
            # coinCat_arr.append(coinCat)
          
            # condition = l.get_collected_values('condition')
            # condition_arr.append(condition)
            
            # price = l.get_collected_values('price')
            # price_arr.append(price)
            
            # est_price = l.get_collected_values('est_price')
            # est_price_arr.append(est_price)
            
            # bids = l.get_collected_values('bids')
            # bids_arr.append(bids)
            
            # views = l.get_collected_values('views')
            # views_arr.append(views)
            
            # auctionEnd_d = l.get_collected_values('auctionEnd_d')
            # auctionEnd_d_arr.append(auctionEnd_d)
            
            #print(coinName_arr)
            #print(coinCat_arr)
            #print(condition_arr)
            #print(price_arr)
            #print(est_price_arr)
            #print(bids_arr)
            #print(views_arr)
            #print(auctionEnd_d_arr)
            
        next_page = response.css("#content .pagination a[rel='next']").attrib['href']
        if next_page is None: 
            yield scrapy.Request(self.parse) # if there is NOT next_page go to parse(1) and scrap next auction
        else:
            yield response.follow(next_page, callback=self.parse2) # if there is next_page go to parse(2) and scrap pages in current auction