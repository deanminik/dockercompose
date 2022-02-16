import time

import redis
from flask import Flask

app = Flask(__name__) # execute flask
cache = redis.Redis(host='redis', port=6379) # connection of redis host='redis' -> there is a 
# connection with that name (docker container)

def get_hit_count(): # a normal function to count the recharge page 
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/') # initial path 
def hello():
    count = get_hit_count()
    return 'Hello World! I have been see+++++++++++n {} times.\n'.format(count)

