#imports
import pymysql

#globals
mydb=pymysql.connect()
myCursor = mydb.cursor()

#connect
def dbconnect():
    # Open database connection
    global mydb
    mydb = pymysql.connect("localhost","root","","InternBlitz" )
    cursor = mydb.cursor()
    cursor.execute("use internblitz")
    return cursor
    
def dbclose():
    global mydb
    mydb.close()

def gettabels():
    global mydb
    dbconnect()
    cursor = mydb.cursor()
    query="show tables;"
    
    cursor.execute(query)
    for row in cursor:
        print(row)

    mydb.close()

def instertJob(job):
    #
    pass

def instertJobs(jobs):
    pass

#return a list of jobs
def getJobs():
    jobs=[]
    cursor = dbconnect()
    query="select * from jobs where cid="+1+";"
    
    cursor.execute(query)

    #put back into array
    for row in cursor:
        print(row['jid'])




    mydb.close()

    return jobs



#main
if __name__=="__main__":
    dbconnect()
    dbclose()

    gettabels()
