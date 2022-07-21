from camera import Camera
from streamingoutput import StreamingOutput
from servo import Servo
from light import Light
from threading import Thread
import json
import websocket

# Server host
serverHost = "192.168.67.102:8000"
# Camera object
camera = Camera()
# Frame size
frame_size = (640, 480)
# Frame rate
frame_rate = 20
# Streaming output object
output = StreamingOutput()
# Servos
servoX = Servo(channel=0)
servoY = Servo(channel=1)
# Light
light = Light(pin = 17)

def on_message(wsapp, message):
    message = json.loads(message)
    if message['op'] == 'mv':
        # Movement
        dir = message['dir']
        if dir == 'L':
            # Left
            Thread(target = servoX.start_move(distance = +(message['dist']))).start()
        elif dir == 'R':
            # Right
            Thread(target = servoX.start_move(distance = -(message['dist']))).start()
        elif dir == 'D':
            # Down
            Thread(target = servoY.start_move(distance = +(message['dist']))).start()
        elif dir == 'U':
            # Up
            Thread(target = servoY.start_move(distance = -(message['dist']))).start()
        elif dir == 'C':
            # Centering
            Thread(target = servoX.center()).start()
            Thread(target = servoY.center()).start()
            
    elif message['op'] == 'lt':
        # Light
        on = message['on']
        if on == True:
            Thread(target = light.led_on).start()
        else:
            Thread(target = light.led_off).start()

try:
    # Start camera
    camera.start_camera(output, frame_size = frame_size, frame_rate = frame_rate)
    
    # Websocket App: Used for receiving control command from server
    wsapp = websocket.WebSocketApp(f"ws://{serverHost}/ws/control/device1/", on_message=on_message)
    try:
        # Run the websocket in different thread
        wst = Thread(target = wsapp.run_forever)
        wst.start()
    except Exception as e:
        print (f'{e}: Failed starting websocketapp connection. closing connection')
        wsapp.close()
        wst = None
    
    # Websocket: Used for sending frames to server
    ws = websocket.WebSocket()
    ws.connect(f"ws://{serverHost}/ws/frame/device1/")
    while True:
        with output.condition:
            output.condition.wait()
            frame = output.frame
            ws.send(frame, opcode=2)

except Exception as e:
    print (f'{e}: Camera Starting Error')
