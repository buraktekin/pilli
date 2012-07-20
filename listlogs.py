#IMPORTING THE LIBS AND BUILT_IN CLASSES
import time
from flask import Flask,request
from flask import render_template
import pymongo
from pymongo import Connection
connection=Connection('localhost',27017)
app = Flask(__name__, instance_path='/home/cs-burak/pilli')
  

@app.route("/", methods=["POST", "GET"])
def listlog(host=None, msg=None, line=None, page=None, np=None, lastp=None):
    error=None
    numofel=None
    tag=None
    Level=None
    Function=None
    File=None
    Time=None
    #--REGISTERING...
    db=connection.pilli
    f=db.things.find()
    #--MY VARIABLES...
    a = request.args["from"]
    a = int(a)
    b=a/10
    l=0
    c=0
    #--MYLISTS...
    host = []
    msg = []
    lineno=[]
    tag=[]
    level=[]
    func=[]
    File=[]
    Time=[]
    fltr=[]
    srch=""
    ##--FOR LOOP AND WRITING FUNCTION...
    for i in f.skip(a).limit(10):
      host= host + [i["host"]]
      msg=msg + [i["msg"]]
      lineno=lineno + [int(i["line_no"])]
      tag=tag + [i["tag"]]
      if srch=="":
	level=level+[i["level"]]
      else:
	finder()
      func=func+[i["funcname"]]
      File=File+[i["file"]]
      Time=Time+[time.ctime(i["time"])]
      l=l+1
      c=c+1
      
    return render_template('result.html',host=host, msg=msg, line=lineno, page=a, np=b, numofel=c, tag=tag, Level=level, Function=func, File=File, Time=Time)
    
def finder():
  if request.method == 'POST':
    srch==request.form("_search")
  for e in f:
    x=e["level"]
    if x.__contains__(srch):
      f=e
    
    
if __name__ == "__main__":
  app.config["DEBUG"]=True
  app.run()
    