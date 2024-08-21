from machine import Pin, PWM

class Light: # class to allow controlling of LED brightness
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
    # initialise LED with current brightness levels
    self.pin.freq(1000)
    self.pin.duty_u16(int(self.brightness / 100 * 65536 - 1))
  