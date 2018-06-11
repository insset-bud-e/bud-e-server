from flask import Flask, jsonify, request
from app import server, mongo
from bson.objectid import ObjectId


@server.route('/devices', methods=['GET'])
def find():
    try:
        dbRequest = mongo.db.things
    except:
        return jsonify({"message": "Not connected to database."}), 500
    devices = dbRequest.find()    
    output = []
    if not devices:
        return jsonify({"message": "No devices found."})
    else:
        for device in devices:
            output.append({'_id' : str(device['_id']),\
            'name' : device['name'],\
            'ip' : device['ip'],\
            'type' : device['type']
            })
        return jsonify({'res' : output})

@server.route('/device/<string:id>', methods=['GET'])
def findOne(id):
    try:
        dbRequest = mongo.db.things
    except:
        return jsonify({"message": "Not connected to database."}), 500
    output = []
    device = dbRequest.find_one({'_id': ObjectId(id)})
    if not device:
        return jsonify({"message": "No device found with the given ID."}), 404
    else:
        output.append({'_id' : str(device['_id']),\
            'name' : device['name'],\
            'ip' : device['ip'],\
            'type' : device['type']
            })
    return jsonify({'res' : output})