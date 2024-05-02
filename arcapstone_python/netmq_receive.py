import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.PULL)
# socket.connect("tcp://localhost:12345")

# Quest 3 on CMU-DEVICE
socket.connect("tcp://172.26.188.87:12345")
# socket.connect("tcp://192.168.1.179:12345")

file = open("translation_testing_coordinates.txt", "w")
while True:
    # Receive message from remote server
    message = socket.recv()

    # Deserialize the JSON message
    try:
        data = json.loads(message.decode())
    except json.JSONDecodeError:
        print("Terminating the connection...")
        socket.close()
        context.term()
        break

    # Access the deserialized data
    left_controller = data["LeftController"]
    right_controller = data["RightController"]
    print("Right XYZ: " + right_controller["RightLocalPosition"],
          "Right rotation: " + right_controller["RightLocalRotation"])
    coords = f"Right XYZ\t{right_controller['RightLocalPosition']}\tRight rotation\t{right_controller['RightLocalRotation']}\n"
    file.write(coords)
file.close()
