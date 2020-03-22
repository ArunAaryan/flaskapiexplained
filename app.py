from flask import Flask, request
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017')



app = Flask(__name__, static_url_path='/Users/arunaaryan/Desktop/flaskapi/flaskapi/static')
db = client.flaskapi #client.databasename
flaskapi = db.flaskapi #databasename.collectionname



@app.route('/add', methods=['POST'])
def add():
    
    pd = {
        "name" : request.values['name'],
        "password" : request.values['password']
    }
    print(pd)
    result = flaskapi.insert_one(pd) #collectionname.methodname

    return {"add": "add successful"}, 200


@app.route('/show',methods=['POST'])
def show():
    query = request.values['name']
    showall = flaskapi.find({'name':query}, {"_id": 0})
    a = []
    for x in showall:
        # print(x)
        a.append(x)
    return(json.dumps(a))
       

    






if __name__ == '__main__':
    app.run(debug=True)
