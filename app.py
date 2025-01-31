from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def root_fn():
    return 'API is working fine'

@app.route('/time')
def time_now():
    t = time.localtime()
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', t)  # Format the time as a string
    return formatted_time

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)  # Run on port 3000
