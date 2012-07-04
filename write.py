from flask import Flask
import pymongo
from pymongo import Connection

connection=Connection('localhost',27017)
app = Flask(__name__, instance_path='/home/cs-burak/pilli')

@app.route("/")
def write():
    db=connection.pilli
    l=[]
    with app.open_instance_resource('read.txt') as f:
        for line in f.readlines():
            print line + "\n"
            l=l+[line]
            
            for i in range(len(l)):
                mongo.db.things.save({"{a:5,j:3}"})
        return str(l)
        f.close()
  	
if __name__ == "__main__":
    app.config["DEBUG"]=True
    app.run()