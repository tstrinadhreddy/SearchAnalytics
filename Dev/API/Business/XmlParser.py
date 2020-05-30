import requests
import feedparser
from dateutil.parser import parse
from datetime import datetime
from ..Database import GoogleSearchData

def loadRSS():
    # url of rss feed
    url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=US'
    # creating HTTP response object from given url
    feed = feedparser.parse(url)
    # saving the xml file
    print(feed)
    print(feed.entries[0].title)
    print(feed.entries[0].ht_approx_traffic)
    print(feed.entries[0].summary)
    print(feed.entries[0].link)
    print(feed.entries[0].published)
    print(feed.entries[0].ht_news_item_snippet)
    print(feed.entries[0].ht_news_item_url)
    print(feed.entries[0].ht_news_item_source)
    FeedList = list()
    for x in feed.entries:
        EntryDict={}
        #print(type(x.published))
        #Test to build Keyvaluepair
        #print(parse(x.published).date().strftime('%m/%d/%Y') + ':' + x.title.replace(' ','_'))
        #https://www.journaldev.com/23365/python-string-to-datetime-strptime
        #https://wiki.freepascal.org/RFC_1123_Time_Format

        EntryDict.update({'key_value': parse(x.published).date().strftime('%m/%d/%Y') + ':' + x.title.replace(' ','_') ,'title': x.title, 'approx_traffic':int(x.ht_approx_traffic.replace('+','').replace(',','')),'summary':x.summary,'link_url':x.link,
                          'published_date':datetime.strptime(x.published, '%a, %d %b %Y %H:%M:%S %z'),'news_snippet':x.ht_news_item_snippet,'news_title':x.ht_news_item_title,'news_url': x.ht_news_item_url,
                          'news_source':x.ht_news_item_source,'lastmodified_date':datetime.now()})
        FeedList.append(EntryDict)
    return GoogleSearchData.Google_Search_Upsert(FeedList)