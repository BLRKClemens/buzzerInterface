from gpiozero import Button
from signal import pause
import socketio

# Erstelle Socket.IO ClientsioLocal = socketio.Client()

sioLocal = socketio.Client()

@sioLocal.event
def connect():
    print("Verbunden zum local Server")

@sioLocal.event
def disconnect():
    print("Verbindung vom Local Server getrennt")

# Beispiel für eigenes Event (z.B. 'message')
@sioLocal.on('message')
def on_message(data):
    print('Nachricht vom local Server:', data)

# Verbinde zum Socket.IO Server
sioLocal.connect("http://localhost:3000")



buzzerL = Button(7,bounce_time=0.05) 
buzzerM = Button(9,bounce_time=0.05) 
buzzerR = Button(27,bounce_time=0.05) 


def buzzer_pressed(pos):
    print("Buzzer wurde gedrückt!")
    sioLocal.emit("buzzerPressed", pos)

buzzerL.when_pressed = buzzer_pressed(0)
buzzerM.when_pressed = buzzer_pressed(1)
buzzerR.when_pressed = buzzer_pressed(2)


print("Buzzer wartet auf Betätigung...")

# Bleibt aktiv, um Events zu empfangen
sioLocal.wait()
