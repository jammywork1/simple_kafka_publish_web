#!/usr/bin/python3
# -*- coding: utf-8 -*-

from confluent_kafka import Producer

class Publisher:
    _publishResult = None
    
    def __init__(self, bs):
        if not bs:
            raise Exception("bs not be empty")
        self._client = Producer({
            'bootstrap.servers': bs,
            # 'socket.timeout.ms': 3000
        })

    def _delivery_callback(self, err, msg):
        if err:
            self._publishResult = 'send error: {0}'.format(err)
        else:
            self._publishResult = 'send success. offset: {0}'.format(msg.offset())

    def publish(self, topic, bdata):
        if not topic:
            raise Exception("topic not be empty")
        self._client.produce(topic, bdata, callback=self._delivery_callback)

        self._client.flush()

        return self._publishResult
