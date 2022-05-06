import os
import json
import redis
from flask import Flask, jsonify, request


app = Flask(__name__)

class RedisResource:
    REDIS_QUEUE_LOCATION = os.getenv('REDIS_QUEUE', 'localhost')
    QUEUE_NAME = 'queue:factoring'

    host, *port_info = REDIS_QUEUE_LOCATION.split(':')
    port = tuple()
    if port_info:
        port, *_ = port_info
        port = (int(port),)

    conn = redis.Redis(host=host, *port)

@app.route('/factor', methods=['POST'])
def post_factor_job():
    body = request.json
    json_packed = json.dumps(body)
    print('packed:', json_packed)
    RedisResource.conn.rpush(
        RedisResource.QUEUE_NAME,
        json_packed)
    
    return jsonify({'status': 'OK'})
