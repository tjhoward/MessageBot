from flask import Flask 
from threading import Thread
from main import start
import os #to get environment variable from AWS

api_key = os.environ['API_KEY']

application = Flask('__name__')

@application.route('/')
def hellow_world():

    keep_alive()
    start()
    return f"Hello. I am alive! {api_key}"

def run():
  return "HIIII"
  #application.run(host='0.0.0.0',port=4455)

def keep_alive():
    t = Thread(target=run)
    t.start()
