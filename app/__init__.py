from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

server = Flask(__name__)

CORS(server)
server.secret_key = "7bce579c0af059582f18bd5158f22ef78dae5055"
server.config['MONGO_DBNAME'] = 'bude'
# server.config['MONGO_URI'] = 'mongodb://root:rootpassword1@ds123725.mlab.com:23725/bud-e'
server.config['MONGO_URI'] = 'mongodb://localhost:27017/bude'

mongo = PyMongo(server)

from app.controllers import DiscoveryController, DevicesController
