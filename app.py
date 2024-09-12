from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def fetch_data():
    url = "https://api.fastforex.io/fetch-all?api_key=8af093cb86-45b4e93120-sjkn6c"
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



