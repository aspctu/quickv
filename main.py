from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request
from replit import db
from replit.database.database import ObservedList

app = Flask(__name__)
CORS(app)

def checkIsList(value):
    # Replit's internal implementaion of this list is actually
    # a ObservedList
    return type(value) == ObservedList

def checkKeyExists(key):
    # Check to see if the key exists in the DB
    return key in db.keys()

@app.route('/')
def getHome():
    return "<p>Domain not found</p>"

@app.route('/get')
def getKey():
    key = request.args.get('key')
    if not checkKeyExists(key):
        return jsonify({"success": False, "error": "key does not exist"})
    value = db[key]
    if checkIsList(value):
        # Hack to be able to jsonify the internal list (aka ObservableList)
        value = list(value)
        return jsonify({"success": value})
    value = db[key]
    return jsonify({"success": value})


@app.route('/add', methods=['POST'])
def addKey():
    key = request.json['key']
    value = request.json['value']
    if checkKeyExists(key):
        return jsonify({"success": False, "error": "key already exists"})
    db[key] = value
    return jsonify({"success": True})


@app.route('/update', methods=['POST'])
def updateKey():
    key = request.json['key']
    value = request.json['value']
    if not checkKeyExists(key):
        return jsonify({"success": False, "error": "key doesn't exist"})
    if checkIsList(db[key]):
        # If the value is of type List, the UPDATE operation must append
        # the value instead of replacing the existing value
        db[key].append(value)
        return jsonify({"success": True})
    else:
        # Else, replace the value
        db[key] = value
        return jsonify({"success": True})


@app.route('/delete', methods=['POST'])
def deleteKey():
    key = request.json['key']
    if not checkKeyExists(key):
        return jsonify({"success": False, "error": "key doesn't exist"})
    del db[key]
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)