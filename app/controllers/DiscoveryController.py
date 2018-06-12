from flask import Flask, flash, request, json,\
render_template, redirect, url_for, send_from_directory, jsonify
from app import server
from app.lib.netdisco.discovery import NetworkDiscovery

@server.route('/', methods=['GET'])
def scan():
    interfaces = []
    netDiscovery = NetworkDiscovery()
    netDiscovery.scan()
    for interface in netDiscovery.discover():
        interfaces.append(interface)
    netDiscovery.stop()
    return jsonify({'interfaces': interfaces})
