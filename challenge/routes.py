#imports
from flask import Flask
from flask import render_template, g, abort
import scraper
import time

#globals
app = Flask(__name__)

#stuff=scraper.scrape(scraper.sites[0], None)
companylist=scraper.companies

stuff=scraper.scrapers()
lastscrape=time.time()
interval=scraper.interval

#defs



#routes 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/companies')
def companies():
    #print(companylist[0])
    return render_template('companies.html', companies=companylist, timestamp=time.asctime(time.localtime(lastscrape)))

@app.route('/jobs/')
def jobs0():
    company="Twillio"
    index=0
    redderedDoc=render_template('jobspage.html', company_name=company, 
        positions=stuff[index][0], locations=stuff[index][1], links=stuff[index][2], jobs=stuff,
        timestamp=time.asctime(time.localtime(lastscrape)))

    return redderedDoc

@app.route('/jobs/<company>')
def jobs(company):
    if company not in companylist:
        abort(404)
    index=companylist.index(company)
    redderedDoc=render_template('jobs.html', company_name=company, 
        positions=stuff[index][0], locations=stuff[index][1], links=stuff[index][2], jobs=stuff, 
        timestamp=time.asctime(time.localtime(lastscrape)))

    return redderedDoc

@app.before_request
def before_request():
    global lastscrape
    global stuff

    if time.time()-lastscrape>interval:
        lastscrape=time.time()
        stuff=scraper.scrapers()
        pass
    print("Last Scrape :  "+str(lastscrape)+" "+str(time.time()-lastscrape) +" seconds ago")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# main
if __name__=="__main__":
    app.debug = True
    app.run()
