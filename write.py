from flask import Flask
import pymongo
import json
from pymongo import Connection

connection=Connection('localhost',27017)
app = Flask(__name__, instance_path='/home/cs-burak/pilli')

@app.route("/")
def write():
    db=connection.pilli
    l=[]
    with app.open_instance_resource('read.txt') as f:
        for line in f.readlines():
            l=l+[line]
            db.things.insert({'line':json.dumps(line, sort_keys=True, indent=4)})
        return str(l)
        
    	
if __name__ == "__main__":
    app.config["DEBUG"]=True
    app.run()
