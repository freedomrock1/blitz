#imports
from flask import Flask
from flask import render_template, g 
import scraper


#globals
app = Flask(__name__)

#stuff=scraper.scrape(scraper.sites[0], None)
companylist=scraper.companies

stuff=scraper.scrapers()
#defs



#routes 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies')
def companies():
    print(companylist[0])
    return render_template('companies.html', companies=companylist)

@app.route('/jobs/')
def jobs0():
    company="Twillio"
    index=0
    redderedDoc=render_template('jobs.html', company_name=company, 
        positions=stuff[index][0], locations=stuff[index][1], links=stuff[index][2], jobs=stuff)
    print(company+"\n")
    return redderedDoc

@app.route('/jobs/<company>')
def jobs(company):
    index=companylist.index(company)
    #print(company+" = "+index)
    print(index)
    redderedDoc=render_template('jobs.html', company_name=company, 
        positions=stuff[index][0], locations=stuff[index][1], links=stuff[index][2], jobs=stuff)
    print(company+"\n")
    return redderedDoc

@app.before_request
def before_request():
    #check for updates
    pass


# main

if __name__=="__main__":
    app.debug = True
    app.run()
