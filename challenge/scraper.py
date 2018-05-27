#  imports
from lxml import html
import requests 

# globals
# sites
#sites=['http://docs.python-guide.org/en/latest/scenarios/scrape/','','']
sites=['http://localhost/blitz/twilio-jobs.html','','']


# site scrape
def scrape(site, paths):
    page = requests.get(site)
    tree = html.fromstring(page.content)
    
    positions = tree.xpath('//div[@id="joblist-container"]//li//a/text()')
 
    locations = tree.xpath('//div[@id="joblist-container"]//li//span/text()')

    links = tree.xpath('//div[@id="joblist-container"]//li//a/@href')

    categories = tree.xpath('//div[@id="joblist-container"]//span[@class="dept-title"]/text()')



    #contents = page.content
    #print (positions)
    #print (links)

    out=[positions,locations,links]

    return out


#main
if __name__=="__main__":
    scrape(sites[0], "")
