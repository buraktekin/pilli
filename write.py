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
<<<<<<< HEAD
            db.things.insert({'line':json.dumps(line, sort_keys=False, indent=1)})
        return str(l)
        
		
=======
            db.things.insert({'line':json.dumps(line, sort_keys=True, indent=4)})
        return str(l)
        
    	
>>>>>>> 92e008cef92748179869c442d59d94ed2b632d58
if __name__ == "__main__":
    app.config["DEBUG"]=True
    app.run()
