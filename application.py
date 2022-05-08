from flask import Flask
from threading import Thread

application = Flask('__name__')

@application.route('/')
def hellow_world():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
