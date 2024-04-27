from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
from PIL import Image
import warnings

warnings.filterwarnings('ignore')


app = Flask(__name__)

CORS(app)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        data = request.json
        print(data)
        return jsonify(data)
    if request.method == 'GET':
        return jsonify({'message': 'Hello World!'})