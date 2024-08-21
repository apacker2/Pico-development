
import math
from machine import Pin
from machine import PWM
from machine import I2C, SoftI2C
from time import sleep
from lib.lis2dw12 import LIS2DW12
from led.dimmer import Light

led_pwm = PWM(Pin(6))

led_pwm.freq(1000)

led_pwm.duty_u16(30000)
  

def dimmer():
  led1 = Light(2)
  led2 = Light(3)
  led3 = Light(6)
  i = 0
  while True:
    i += math.pi / 1000
    led1.dim(abs(math.sin(i)) * 20)
    sleep(0.01)

def servo():
  print("servo")
  servo_pin = PWM(Pin(10))
  servo_pin.freq(50)
  i = 0.2
  while True:
    print(i)
    servo_pin.duty_ns(int(i*1000000))
    i += 0.001
    sleep(0.01)
    if i > 2.6:
      i = 0.2

def i2c():
  i2c = I2C(1, scl=Pin(27), sda=Pin(26))
  # addresses: 25, 60
  # 25 (0x19): accelerometer
  # 60 (0x3C): OLED
  sensor = LIS2DW12(i2c, address=25)
  while True:
    print(sensor.acceleration)
    sleep(1)

print(__name__)
if __name__ == "__main__":
  
  dimmer()
  



  