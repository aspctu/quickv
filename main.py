from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
from replit import db
from utils import checkIsList, checkKeyExists

app = Flask(__name__)
CORS(app)

@app.route('/get')
def getKey():
    key = request.args.get('key')
    if not checkKeyExists(key):
        return {"success": False, "error": "key does not exist"}, 500
    value = db[key]
    if checkIsList(value):
        # Hack to be able to jsonify the internal list (aka ObservableList)
        value = list(value)
        return {"success": value}, 200
    value = db[key]
    return {"success": value}, 200

@app.route('/add', methods=['POST'])
def addKey():
    key = request.json['key']
    value = request.json['value']
    if checkKeyExists(key):
        return {"success": False, "error": "key already exists"}, 500
    db[key] = value
    return {"success": True}, 200


@app.route('/update', methods=['POST'])
def updateKey():
    key = request.json['key']
    value = request.json['value']
    if not checkKeyExists(key):
        return {"success": False, "error": "key doesn't exist"}, 500
    if checkIsList(db[key]):
        # If the value is of type List, the UPDATE operation must append
        # the value instead of replacing the existing value
        db[key].append(value)
        return {"success": True}, 200
    else:
        # Else, replace the value
        db[key] = value
        return {"success": True}, 200


@app.route('/delete', methods=['POST'])
def deleteKey():
    key = request.json['key']
    if not checkKeyExists(key):
        return {"success": False, "error": "key doesn't exist"}, 500
    del db[key]
    return {"success": True}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)