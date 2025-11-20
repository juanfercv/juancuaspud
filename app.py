from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <title>Bienvenido</title>
            <style>
                body { 
                    background-color: #f0f8ff; 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    margin-top: 100px;
                }
                h1 { color: #2e8b57; }
                p { font-size: 20px; }
            </style>
        </head>
        <body>
            <h1>Hola Juan Fernando Cuaspud Velasco</h1>
            <p>¡Bienvenido a tu aplicación Flask!</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2407)