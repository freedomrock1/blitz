#  imports
from lxml import html
import requests 
from bs4 import BeautifulSoup as bs
import time

# globals
companies=['Twillio','Airbnb','Yext']

#interval between scrapes in seconds
interval=15*60

sites=[]

sites=['https://www.twilio.com/company/jobs',
        'https://www.airbnb.com/careers/departments',
        'https://www.yext.com/careers/open-positions/']


sites+=['http://localhost/blitz/twilio-jobs.html',
        'http://localhost/blitz/airbnb/deparmentCareersAirbnb.html',
        'http://localhost/blitz/YextCareers.html']

    #Twillio    @Greenhouse [6]8
    #Yext       @Greenhouse [7]9
sites+=['https://boards.greenhouse.io/twilio/',
        'https://boards.greenhouse.io/yext/']

sites+=['http://localhost/blitz/GreenhouseTwilio.html',
        'http://localhost/blitz/GreenhouseYext.html']

paths=[]
    # twillio
paths+=[['//div[@id="joblist-container"]//li//a/text()',
        '//div[@id="joblist-container"]//li//span/text()',
        '//div[@id="joblist-container"]//li//a/@href',
        '//div[@id="joblist-container"]//span[@class="dept-title"]/text()']]

    #airbnb
paths+=[['//table[@class="table table-striped jobs"]//tr/td[1]/a/text()',
        '//table[@class="table table-striped jobs"]//tr/td[2]/a/text()',
        '//table[@class="table table-striped jobs"]//tr/td[1]/a/@href',
        '//main//a[@class="jobs-card link-reset"]/div/div/div/div/text()',
        '//main//a[@class="jobs-card link-reset"]/@href']]

  
    #yext
paths+=[['//div[@id="openpositions"]//div[contains(@class, "jobs__category-block") ]//span[@class="jobs__post-title"]//text()',
        '//div[@id="openpositions"]//div[contains(@class, "jobs__category-block") ]//span[@class="jobs__post-city"]//text()',
        '//div[@id="openpositions"]//div[contains(@class, "jobs__category-block") ]//a[@class="jobs__post-item"]/@href',
        '//div[@id="openpositions"]//div[contains(@class, "jobs__category-block") ]//span[@class="jobs__category-name"]//text()']]

    #Twillio    @Greenhouse [3]
    #Yext       @Greenhouse [3]

paths+=[['//div[@class="opening"]/a/text()',
        '//div[@class="opening"]/span/text()',
        '//div[@class="opening"]/a/@href',
        '//div[@id="main"]/section[@class="level-0"]/h2/text()']]


# site scrape
def scrape(site, path):
    page = requests.get(site)
    tree = html.fromstring(page.content)
    
    positions = tree.xpath(path[0])
    locations = tree.xpath(path[1])
    links = tree.xpath(path[2])

    categories = tree.xpath(path[3])

    out=[positions,locations,links, categories]

    return out

# site scraper 2 step
def scrape2(site, path):
    #get a list of URLs from main page
    doc = requests.get(site)
    tree = html.fromstring(doc.content)
    pages=tree.xpath(path[4])
    fullpages=[]
    thesite=site[:site.find('/', site.find('//')+2)]
    #print(thesite)
    ## complete the links to category pages
    for page in pages:
        if page.find('http')<0:
            page=thesite+page
        fullpages.append(page)
        pass
    pages=fullpages
    #print(pages)
    
    categories = tree.xpath(path[3])
    ###todo clean cats
    #print(categories)

    positions=[]
    locations=[]
    links=[]

    for page in pages:
        # for local testing 
        if not 'localhost' in page:  
            pass
            continue

        doc = requests.get(page)
        tree = html.fromstring(doc.content)
        
        positions += tree.xpath(path[0])
        locations += tree.xpath(path[1])
        links += tree.xpath(path[2])

    ## complete the links 
    fulllinks=[]
    for link in links:
        link=thesite+link
        fulllinks.append(link)
        pass
    links=fulllinks

    out=[positions,locations,links,categories]

    return out

def scrapers():
    out=[]
    out+=[scrape(sites[6+2], paths[3])]   #Twillio thru Greenhouse 6,8
    out+=[scrape2(sites[1+3], paths[1])]  #AirBnB
    out+=[scrape(sites[7+2], paths [3])]  #Yext thru Greenhouse   7,9
    return out

def update():
    pass


def test(site, path):
    r = requests.get(site)
    tree = html.fromstring(r.content)

    positions = tree.xpath(path[0])
    locations = tree.xpath(path[1])
    links = tree.xpath(path[2])
    categories = tree.xpath(path[3])

    out=[positions,locations,links, categories ]
    return out



#main
if __name__=="__main__":
    #scrape(sites[0], paths)
    #print(scrape2(sites[1], paths))
    stuff=test(sites[9],paths[3])
    #print(len(stuff[0][0]))
    
    print(stuff[0])
    print(len(stuff[0]) )
    print(len(stuff[1]) )
    print(len(stuff[2]) )