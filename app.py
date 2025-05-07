from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/page2')
def page2():
    return send_from_directory('templates', 'page2.html')

@app.route('/page3')
def page3():
    return send_from_directory('templates', 'page3.html')

@app.route('/welcome')
def welcome():
    return send_from_directory('templates', 'welcome.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 