#  imports
from lxml import html
import requests 

# globals



companies=['Twillio','Airbnb','Yext']


sites=['http://localhost/blitz/twilio-jobs.html',
        'http://localhost/blitz/airbnb/deparmentCareersAirbnb.html',
        'http://localhost/blitz/YextCareers.html']

#sites=['https://www.twilio.com/company/jobs',
# 'https://www.airbnb.com/careers/departments',
# 'https://www.yext.com/careers/open-positions/']

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




# site scrape
def scrape(site, path):
    page = requests.get(site)
    tree = html.fromstring(page.content)
    
    positions = tree.xpath(path[0])
 
    locations = tree.xpath(path[1])

    links = tree.xpath(path[2])

    categories = tree.xpath(path[3])



    #contents = page.content
    #print (positions)
    #print (links)

    out=[positions,locations,links]

    return out

# site scraper 2 step
def scrape2(site, path):
    #get a list of URLs from main page
    doc = requests.get(site)
    tree = html.fromstring(doc.content)
    pages=tree.xpath(path[4])
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
            continue
        #print(page+' local')
        doc = requests.get(page)
        tree = html.fromstring(doc.content)
        
        positions += tree.xpath(path[0])
        locations += tree.xpath(path[1])
        links += tree.xpath(path[2])

    out=[positions,locations,links]
    #out=pages

    return out

def scrapers():
    out=[]
    out+=[scrape(sites[0], paths[0])]
    out+=[scrape2(sites[1], paths[1])]
    out+=[scrape(sites[2], paths [2])]
    return out


def update():
    pass

#main
if __name__=="__main__":
    #scrape(sites[0], paths)
    #print(scrape2(sites[1], paths))
    stuff=scrapers()
    print(len(stuff[2][0]))
    print(stuff[2])