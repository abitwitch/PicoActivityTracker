from machine import Pin, Timer
import ina219
import oled

led = Pin(25, Pin.OUT)
battery = ina219.INA219(addr=0x43)
timer = Timer()
screen = oled.OLED_1inch3()

def getBatteryPct():
    bus_voltage = battery.getBusVoltage_V()
    pct = (bus_voltage -3)/1.2*100
    if(pct<0):pct=0
    elif(pct>100):pct=100
    return(pct)







def blink(timer):
    led.toggle()
    if led.value():
        screen.fill(0x0000)
        screen.text("S M T W T F S",1,10,screen.white)
    else:
        screen.fill(0x0000) 
        screen.show()
        screen.rect(0,0,128,64,screen.white)
    screen.show()
    print("Percent:  {:6.1f} %".format(getBatteryPct()))

timer.init(freq=1.5, mode=Timer.PERIODIC, callback=blink)