from flask import Flask, jsonify, request
from app import server, mongo
from bson.objectid import ObjectId
import re, json



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
            'ip' : device['ip'],\
            'type' : device['type'],\
            'hostname': device['hostname'],\
            'port': device['port']
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
            'hostname' : device['hostname'],\
            'ip' : device['ip'],\
            'type' : device['type'],\
            'port': device['port']
            })
    return jsonify({'res' : output})

@server.route('/device/save', methods=['POST'])
def create():
    try:
        devices = mongo.db.things
    except:
        return jsonify({"message": "Database connection impossible."}), 400
    try:
        if request.get_json():
            json = request.get_json()
            res = []
            for i in json['devices']:
                if devices.find_one({'ip': i['ip']}):
                    pass
                else:
                    hostname=i['hostname']
                    newHostname=hostname[hostname.find("_")+1:hostname.find(".")]
                    new_device = devices.insert({
                        'hostname': i['hostname'],\
                        'ip': i['ip'],\
                        'port': i['port'],\
                        'type': newHostname})
                    res.append(new_device)
            if res:
                return jsonify({"message": "Devices added successfully."})
            else:
                return jsonify({"message": "No new device to save."})
        else:
            new_device = devices.insert({
                'ip': '172.20.10.5',\
                'type': 'arduino',\
                'hostname':"_arduino.",\
                'port': 5000
            })
            data = devices.find_one({'_id': new_device})
            output = []
            output.append({'_id' : str(data['_id']),\
                'ip' : data['ip'],\
                'type' : data['type'],\
                'hostname': data['hostname'],\
                'port': data['port']
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