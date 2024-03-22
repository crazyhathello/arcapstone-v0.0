import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.PULL)
# socket.connect("tcp://localhost:12345")
socket.connect("tcp://192.168.1.179:12345")

while True:
    # Receive message from remote server
    message = socket.recv()

    # Deserialize the JSON message
    try:
        data = json.loads(message.decode())
    except json.JSONDecodeError as e:
        print("Terminating the connection...")
        socket.close()
        context.term()
        break

    # Access the deserialized data
    left_controller = data["LeftController"]
    right_controller = data["RightController"]
    print("Right XYZ: " + right_controller["RightLocalPosition"],
          "Right rotation: " + right_controller["RightLocalRotation"])
