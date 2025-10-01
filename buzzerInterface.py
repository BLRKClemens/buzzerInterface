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
sioLocal.connect("http://192.168.11.59:3001")



buzzer0 = Button(24,bounce_time=0.01) 
buzzer1 = Button(9,bounce_time=0.01) 


def buzzer_pressed(pos):
    print("Buzzer wurde gedrückt!", pos)
    sioLocal.emit("buzzerPressed", pos)

buzzer0.when_pressed = lambda: buzzer_pressed(0)
buzzer1.when_pressed = lambda: buzzer_pressed(1)


print("Buzzer wartet auf Betätigung...")

# Bleibt aktiv, um Events zu empfangen
sioLocal.wait()
