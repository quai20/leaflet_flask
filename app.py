#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template
from process_ds import time_serie_on_point
import ast, json
import numpy as np

app = Flask(__name__)

@app.route("/")
def init_webpage():
    return render_template('index.html')

@app.route("/testfj", methods=['POST','GET'])
def test_req_from_js():
    lat = request.args.get('lat')
    lon = request.args.get('lon')        
    tsop = time_serie_on_point(float(lat),float(lon),depth=1.0)
    return json.dumps(tsop.tolist())

if __name__ == '__main__': 
    app.run()