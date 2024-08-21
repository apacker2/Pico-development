
import math
from machine import Pin
from machine import PWM
from machine import I2C, SoftI2C
from time import sleep
from lib.lis2dw12 import LIS2HH12

led_pwm = PWM(Pin(6))

led_pwm.freq(1000)

led_pwm.duty_u16(30000)


class LED: # class to allow controlling of LED brightness
  brightness: float
  state: int # 1 = on, 0 = off
  pin: PWM
  def __init__(self, pin_num: int, brightness=10.0, state=1) -> None:
    self.pin = PWM(Pin(pin_num))
    self.brightness = brightness
    self.state = state
    self.value(state)
  def value(self, val=None) -> int | None:
    if val == None:
      return self.state
    else:
      if val == 0:
        # turn off
        self.pin.deinit()
      elif val == 1:
        self.init()
  def dim(self, brightness: float):
    if brightness >= 0 and brightness <= 100:
      self.brightness = brightness
      self.init()

  def init(self):
    self.pin.freq(1000)
    self.pin.duty_u16(int(self.brightness / 100 * 65536 - 1))
  

        

def dimmer():
  led1 = LED(2)
  led2 = LED(3)
  led3 = LED(6)
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
  sensor = LIS2HH12(i2c, address=25)
 
  while True:
    sleep(0.01)



print(__name__)
if __name__ == "__main__":
  i2c()
  dimmer()
  



  