from flask import Flask, render_template, request, jsonify
import os
import json
import requests

app = Flask(__name__, static_url_path='/static')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/redirect', methods=['POST'])
def redirect():
    json = request.get_json()
    print(json)
    return jsonify(status="correct")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
