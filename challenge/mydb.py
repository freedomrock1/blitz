#imports
import pymysql

#globals
mydb=pymysql.connect()
myCursor = mydb.cursor()

#connect
def dbconnect():
    # Open database connection
    db = pymysql.connect("localhost","root","","InternBlitz" )
    cursor = db.cursor()
    cursor.execute("use internblitz")
    db.close()


def gettabels():
    db = pymysql.connect("localhost","root","","InternBlitz" )
    cursor = db.cursor()
    query="show tables;"
    
    cursor.execute(query)
    for row in cursor:
        print(row)

    db.close()

def instertJob(job):
    pass

def instertJobs(jobs):
    pass

#return a list of jobs
def getJobs():
    jobs=[]
    db = pymysql.connect("localhost","root","","InternBlitz" )
    cursor = db.cursor()
    query="select * from jobs where cid="+1+";"
    
    cursor.execute(query)

    #put back into array
    for row in cursor:
        print(row['jid'])




    db.close()

    return jobs



#main
if __name__=="__main__":
    dbconnect()
    gettabels()
