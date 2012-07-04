from flask import Flask
import pymongo
import json
from pymongo import Connection

connection=Connection('localhost',27017)
app = Flask(__name__, instance_path='/home/cs-burak/pilli')

@app.route("/")
def write():
    db=connection.pilli
    with app.open_instance_resource('read.txt') as f:
        for line in f.readlines():
            print line
            a=json.dumps(line, sort_keys=True, indent=1)
            db.things.insert(a)
            return line
   
        
        
		
if __name__ == "__main__":
    app.config["DEBUG"]=True
    app.run()