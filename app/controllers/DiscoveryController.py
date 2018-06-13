from flask import Flask, flash, request, json,\
render_template, redirect, url_for, send_from_directory, jsonify
from app import server
from app.lib.netdisco.discovery import NetworkDiscovery



@server.route('/', methods=['GET'])
def scan():
    interfaces = []
    netdis = NetworkDiscovery()
    netdis.scan()
    for dev in netdis.discover():
        interfaces.append(netdis.get_info(dev)[0])
    netdis.stop()
    return jsonify({'interfaces': interfaces})
