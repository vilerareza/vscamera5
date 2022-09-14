from functools import partial
from camera import Camera
from streamingoutput import StreamingOutput
from threading import Thread
import json
import websocket
import subprocess

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

def on_message(wsapp, message):
    message = json.loads(message)
    pass

try:
    # Start camera
    camera.start_camera(output, frame_size = frame_size, frame_rate = frame_rate)
    
    # Websocket: Used for sending frames to server
    ws = websocket.WebSocket()
    ws.connect(f"ws://{serverHost}:8000") 
    while True:
        with output.condition:
            output.condition.wait()
            frame = output.frame
            ws.send(frame, opcode=2)

except Exception as e:
    print (f'{e}: Camera Starting Error')
