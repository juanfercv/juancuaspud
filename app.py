from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return " Hola Juan Fernando Cuaspud Velasco "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2407)