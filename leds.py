from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps
a=0

pinNumber = 17 # declaration d'une variable pinNumber à 17
led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)

pinoeoe = 14
ledoeoe = Pin(pinoeoe, mode=Pin.OUT)

pinbaba = 21
ledbaba = Pin(pinbaba, mode=Pin.OUT)

pinbinks = 10
ledbinks = Pin(pinbinks, mode=Pin.OUT)

def onpin(a):
    if a==0:
        led.on()
    elif a==1:
        ledbaba.on()
    elif a==2:
        ledbinks.on()
    elif a==3:
        ledoeoe.on()

while True:
    onpin(a)
    utime.sleep(0.1)
    led.off()
    ledoeoe.off()
    ledbaba.off()
    ledbinks.off()
    if a==3:
        a=0
    else:
        a+=1