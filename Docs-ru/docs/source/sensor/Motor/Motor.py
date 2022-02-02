from microbit import MicroBitAnalogDigitalPin

class Motor():

    def __init__(self, fw_pin:MicroBitAnalogDigitalPin,
                        bw_pin:MicroBitAnalogDigitalPin,
                        sp_pin:MicroBitAnalogDigitalPin
                ):
        self.fw_pin = fw_pin
        self.bw_pin = bw_pin
        self.sp_pin = sp_pin
    
    def forward (self,speed=1024) ->None:
        self.fw_pin.write_digital(1)
        self.bw_pin.write_digital(0)
        self.sp_pin.analog_digital(speed)
    
    def backward (self,speed=1024) ->None:
        self.fw_pin.write_digital(0)
        self.bw_pin.write_digital(1)
        self.sp_pin.analog_digital(speed)
    
    def stop (self) ->None:
        self.fw_pin.write_digital(0)
        self.bw_pin.write_digital(0)
        self.sp_pin.analog_digital(0)

        