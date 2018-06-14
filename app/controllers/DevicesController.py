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

@server.route('/device/save', methods=['POST'])
def create():
    try:
        devices = mongo.db.things
    except:
        return jsonify({"message": "Database connection impossible."}), 400
    try:
        new_device = devices.insert({
            'name': 'New device',\
            'ip': '0.0.0.0',\
            'type': 'Dummy device',\
            'hostname':"arduino"
        })
        data = devices.find_one({'_id': new_device})
        output = []
        output.append({'_id' : str(data['_id']),\
            'name' : data['name'],\
            'ip' : data['ip'],\
            'type' : data['type'],\
            'hostname': "arduino"
        })
        return jsonify({"res": output[0], "message": "Device added successfully."})
    except:
        return jsonify({"message": "Something went wrong."}), 400
    

@server.route('/device/remove/<string:id>', methods=['POST'])
def remove(id):
    try:
        devices = mongo.db.things
    except:
        return jsonify({"message": "Database connection impossible."}), 400
    try:
        devices.remove({"_id": ObjectId(id)})
        return jsonify({"message": "Device forgotten."})
    except:
        return jsonify({"message": "Something went wrong."}), 400