from flask import Flask, request, jsonify, redirect
from datetime import datetime 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def info():
    return jsonify({'ip': request.remote_addr, 'Host' : request.host, 'Port': request.environ.get('REMOTE_PORT'), 'date':str(datetime.now())})

@app.route("/status/")
def routetourl():
    return "PLEASE ENTER A VALID URL"
@app.get("/status/<string:url>")
def redirect_to_url(url):
     s = str(url)
     url = s.replace('-', '.')
     return redirect(f"http://{url}")

if __name__ == '__main__':
    app.run(debug=True)
