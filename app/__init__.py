from flask import Flask, jsonify
from flask_pymongo import PyMongo

server = Flask(__name__)

server.secret_key = "7bce579c0af059582f18bd5158f22ef78dae5055"
server.config['MONGO_DBNAME'] = 'bude'
server.config['MONGO_URI'] = 'mongodb://localhost:27017/bude'

mongo = PyMongo(server)

from app.controllers import DiscoveryController, DevicesController