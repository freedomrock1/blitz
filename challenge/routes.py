#imports
from flask import Flask
from flask import render_template, g 
import scraper


#globals
app = Flask(__name__)

stuff=scraper.scrape(scraper.sites[0], None)

#defs



#routes 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/jobs')
def jobs0():
    company="Twillio"
    redderedDoc=render_template('jobs.html', company_name=company, 
        positions=stuff[0], locations=stuff[1], links=stuff[2], jobs=stuff)
    print(company+"\n")
    return redderedDoc

@app.route('/jobs/<company>')
def jobs(company):
    return render_template('jobs.html')




# main

if __name__=="__main__":
    app.debug = True
    app.run()
