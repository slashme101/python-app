from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'deployed from': 'kubernetes',
        'hostname': socket.gethostname(),
        'message': 'You are doing great Rodney!! :)!!!'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':

    app.run(host="0.0.0.0")




#'/api/v1/details'
#'/api/v1/healthz'