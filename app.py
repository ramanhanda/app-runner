from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def root_fn():
    return 'API is working fine'

@app.route('/time')
def time_now():
    t = time.localtime()
    return t

if __name__ == '__main__':
    app.run()
