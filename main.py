from flask import Flask 
from threading import Thread
import os #to get environment variable from AWS

api_key = os.environ['API_KEY']

application = Flask('__name__')

@application.route('/')
def hellow_world():
    return f"Hello. I am alive! {api_key}"

def run():
  application.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
