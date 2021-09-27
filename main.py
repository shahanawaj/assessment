from flask import Flask , request, jsonify
from datetime import datetime
from time import gmtime, strftime




app = Flask(__name__)

@app.route("/")
def index():
    # body = jsonify{'ip': request.remote_addr, 'timestamp': datetime.now()}
    return jsonify({'timestamp': datetime.now() , 'ip': request.remote_addr })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)