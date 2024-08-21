import asyncio
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
btn_in = Pin(3, Pin.IN, Pin.PULL_DOWN)
btn_in.PULL_UP
print('Blinking LED Example')



def blink():
  while True:
    while btn_in.value() == 1:
      pass
    led.value(not led.value())
    
    sleep(0.5)



blink()