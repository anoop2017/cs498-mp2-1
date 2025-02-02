from flask import Flask, request, jsonify
import json

app = Flask(__name__)

value = 0
DATA_FILE = 'data.json'


def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)['num']
    except FileNotFoundError:
        return {}


def save_data(newVal):
    isSuccess = True
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(newVal, f)
            return isSuccess
    except:
        isSuccess = False
        return isSuccess


@app.route('/', methods=['POST'])
def post_data():
    if request.method == 'POST':
        try:
            new_data = request.get_json()
            # newVal = new_data['num']
            # print(newVal)
            isSuccess = save_data(new_data)
            if isSuccess:
                return jsonify(message='Data saved successfully'), 201
            else:
                return jsonify(message='There is error'), 500
        except:
            return jsonify(message='There is error'), 500
    return jsonify(message='There is error'), 500


@app.route('/', methods=['GET'])
def get_data():
    data = read_data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=80, debug=True)
