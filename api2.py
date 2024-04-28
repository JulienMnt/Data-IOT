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

pwm_ledgreen = PWM(Pin(14,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledgreen.freq(1_000) # dont la frequence est de 1000 (default)

pwm_ledblue = PWM(Pin(15,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
pwm_ledblue.freq(1_000) # dont la frequence est de 1000 (default)

ssid = 'Julien Menet'
password = 'Julien_mnt'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/"
urlapi = "http://172.20.10.3:3001/iot/light/"
urlapipost = "http://172.20.10.3:3001/iot/postcard/"

def affichercouleur (r,v,b):
    pwm_ledred.duty_u16(round(r*30000/250))
    pwm_ledgreen.duty_u16(round(v*30000/250))
    pwm_ledblue.duty_u16(round(b*30000/250))

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while True:
    try:
        print("GET")
        r = urequests.get(url)
        data = r.json()
        character = random.choice(data)
        maison = character["house"]
        print(character["name"])
        print(maison)
        r.close()
        print('Post')
        dat = {"house" : maison , "name" : character["name"]}
        r = urequests.post(urlapipost, json = dat)
        dataapipost = r.json()
        print(dataapipost)
        print(dataapipost['house'])
        r.close()
        print("GET")
        headers = {"house" : dataapipost['house']}
        print(headers)
        r = urequests.get(urlapi, headers=headers)
        dataapi = r.json()
        print(int(dataapi[0]["green"]))
        affichercouleur(int(dataapi[0]["red"]),int(dataapi[0]["green"]),int(dataapi[0]["blue"]))
        r.close()
        utime.sleep(1)
    except Exception as e:
        print(e)