#!/usr/bin/env python3

from flask import Flask, request, render_template, make_response
import redis
import datetime
import json
import logging

# Create the redis object. Make sure that we decode our responses
r = redis.Redis(host='localhost', charset="utf-8", decode_responses=True)

# Create the Flask app
app = Flask(__name__)
app.debug = True


@app.route('/add', methods=['GET'])
def add():
    '''
    Add an agent's extip to the Redis cache
    '''
    agent = request.args.get('agent')
    extip = request.args.get('extip')
    print('Set %s\'s extip to %s' % (agent, extip))


    r.hmset(agent, {'extip': extip})

    return json.dumps({})


@app.route('/update', methods=['POST'])
def update():
    '''
    Update an agent sysinfo checkin details
    '''
    
    data = request.get_json()
    print('json: %s' % data)

    agent = data['agent']
    rdata = r.hgetall(agent)
    data.update(rdata)

    print('Set %s\'s sysinfo data to %s' % (agent, data))
    r.hmset(agent, data)

    return json.dumps({})


@app.route('/query', methods=['GET'])
def query():
    '''
        Return a json objet with the corresponding extip.
    '''
    agent = request.args.get('agent')
    res = r.hgetall(agent)

    print('Agent: %s: %s' % (agent, res))

    return json.dumps(res)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=42424)
