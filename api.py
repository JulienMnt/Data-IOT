import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import time # importe dans le code la lib qui permet de gerer le temps
import utime
import random

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

pwm_ledred = PWM(Pin(13,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledred.freq(1_000) # dont la frequence est de 1000 (default)

pwm_ledgreen = PWM(Pin(15,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledgreen.freq(1_000) # dont la frequence est de 1000 (default)

pwm_ledblue = PWM(Pin(14,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledblue.freq(1_000) # dont la frequence est de 1000 (default)

ssid = 'Julien Menet'
password = 'Julien_mnt'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters"


def affichercouleur(maison):
    if maison == "Gryffindor":
        pwm_ledred.duty_u16(30000)
        pwm_ledgreen.duty_u16(0)
        pwm_ledblue.duty_u16(0)
    elif maison == "Slytherin":
        pwm_ledred.duty_u16(0)
        pwm_ledgreen.duty_u16(30000)
        pwm_ledblue.duty_u16(0)
    elif maison == "Hufflepuff":
        pwm_ledred.duty_u16(30000)
        pwm_ledgreen.duty_u16(30000)
        pwm_ledblue.duty_u16(0)
    elif maison == "Ravenclaw":
        pwm_ledred.duty_u16(0)
        pwm_ledgreen.duty_u16(0)
        pwm_ledblue.duty_u16(30000)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url)# lance une requete sur l'url
        data = r.json()
        print(random.choice(data)["house"])
        print(id)
        r.close() # ferme la demande
        time.sleep(1)  
    except Exception as e:
        print(e)
    