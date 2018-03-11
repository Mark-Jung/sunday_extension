from flask import Flask, render_template, request
#import requests

app = Flask(__name__)

@app.route('/temperature')
def temperature():
    return temp

@app.route('/issues')
def issues():
    return issues

@app.route('/')
def tab():
    return render_template('tab.html')

if __name__ == '__main__':
    app.run(debug=True)
