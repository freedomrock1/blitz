#imports

import pymysql





#globals
db=None 

# credentials
HOST='localhost'
USER='root'
PASS=''
DATABASE='cars'

#defs
class MyClass(object):
    data=None
    conn=None
    
    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        self.data.append(1)
        return 'hello world'
# get db connection
    def thing(self):
        return len(self.data)

    @classmethod
    def thing0(cls):
        return cls.data[0]
        


# get cursor



# execute query



#main for testing
if __name__ == "__main__":
    pass