from flask import Flask, jsonify
from config import SECRET
from flask_pymongo import PyMongo

server = Flask(__name__)

server.secret_key = SECRET
server.config['MONGO_DBNAME'] = 'bude'
server.config['MONGO_URI'] = 'mongodb://mongodb:27017/bude'

mongo = PyMongo(server)

from app.controllers import DiscoveryController, DevicesController
