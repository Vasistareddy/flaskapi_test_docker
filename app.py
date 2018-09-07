import os
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Give proper 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# test API
@app.route('/api/v1/test1', methods=['GET'])
def test_api_1():
    if request.method == 'GET':
        return jsonify({'status_code':200, 'message':'first end point "test1" is called'})

# test API
@app.route('/api/v1/test2', methods=['GET'])
def test_api_2():
    if request.method == 'GET':
        return jsonify({'status_code':200, 'message':'second end point "test2" is called'})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5055, debug=False)

