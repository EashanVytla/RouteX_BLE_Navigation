from bluepy.btle import Scanner
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

def scan_ble_and_emit():
    scanner = Scanner()
    devices = scanner.scan(10)  # Scan for 10 seconds

    strongest_signal = max(devices, key=lambda x: x.rssi)
    beacon_data = {
        'id': strongest_signal.addr,
        'rssi': strongest_signal.rssi
    }
    socketio.emit('beacon_data', beacon_data)

if __name__ == "__main__":
    socketio.run(app, debug=True)
