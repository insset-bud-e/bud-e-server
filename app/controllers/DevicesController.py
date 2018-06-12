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


# @app.route('/devices/save', methods=['POST'])
# def create():
#         try:
#             devices = mongo.db.things
#         except:
#             return jsonify({"message": "Database connection impossible."}), 400
#         try:
#             print("Post method fired ...")
#             files = request.files.getlist("files")
#             data = []
#             res = []
#             predId= predictions.insert({"prediction": predObject["predictions"],\
#             "creation_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),\
#             "suffix": request.form['suffix'],\
#             "numberOfFiles":request.form['nbFiles']})
#             return jsonify({"predID":str(predId),"message": "Prediction created with success."})
#         except:
#             return jsonify({"message": "Something went wrong."}), 400