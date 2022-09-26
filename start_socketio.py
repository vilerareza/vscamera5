import socketio
from camera import Camera
from streamingoutput import StreamingOutput


# Server host
serverHost = "192.168.0.101:8000"
# Camera object
camera = Camera()
# Frame size
frame_size = (640, 480)
# Frame rate
frame_rate = 5
# Streaming output object
output = StreamingOutput()


sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

try:
    # Start camera
    camera.start_camera(output, frame_size = frame_size, frame_rate = frame_rate)

    sio.connect('http://{serverHost}:8000', transports = 'websocket', namespaces='/device1')

    while True:
        with output.condition:
            output.condition.wait()
            frame = output.frame
            sio.emit('frame', data=frame, namespace='/device1')

except Exception as e:
    print (f'{e}: Camera Starting Error')
    sio.disconnect()