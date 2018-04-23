#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from publisher import Publisher

app = Flask(__name__)

@app.route('/publish', methods=['POST'])
def publish():
    bs = request.args.get('bs')
    topic = request.args.get('topic')

    try:
        p = Publisher(bs)
        result = p.publish(topic, request.get_data())
    except Exception as e:
        result = '{0}'.format(e)

    return '{0}'.format(result)