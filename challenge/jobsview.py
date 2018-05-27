from flask import Flask
from flask import render_template, request  # !Important


app = Flask(__name__)

import scraper
stuff=scraper.scrape(scraper.sites[0], None)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stuff")
def showstuff():
    company="Twillio"
    redderedDoc=render_template('jobs.html', company_name=company, 
        positions=stuff[0], locations=stuff[1], links=stuff[2])
    print(company+"\n")
    return redderedDoc




if __name__=="__main__":
    
    app.run()

