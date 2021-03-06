from microbit import sleep


class Motor():

    SPEED: int = 1024

    def __init__(self, fw_pin, bw_pin, sp_pin):
        self.fw_pin = fw_pin
        self.bw_pin = bw_pin
        self.sp_pin = sp_pin

    def forward(self, speed=SPEED) -> None:
        self.fw_pin.write_digital(1)
        self.bw_pin.write_digital(0)
        self.sp_pin.analog_digital(speed)

    def backward(self, speed=SPEED) -> None:
        self.fw_pin.write_digital(0)
        self.bw_pin.write_digital(1)
        self.sp_pin.analog_digital(speed)

    def stop(self) -> None:
        self.fw_pin.write_digital(0)
        self.bw_pin.write_digital(0)
        self.sp_pin.analog_digital(0)


class Driver_Motor():

    SPEED: int = 1024

    def __init__(self, left_motor: Motor, rignt_motor: Motor):
        self.left_motor = left_motor
        self.rignt_motor = rignt_motor

    def forward(self, speed=SPEED) -> None:
        self.left_motor.forward(speed)
        self.rignt_motor.forward(speed)
        sleep(1)

    def backward(self, speed=SPEED) -> None:
        self.left_motor.backward(speed)
        self.rignt_motor.backward(speed)
        sleep(1)

    def stop(self) -> None:
        self.left_motor.stop()
        self.rignt_motor.stop()
        sleep(1)

    def left(self, speed=SPEED) -> None:
        self.left_motor.stop(0)
        self.rignt_motor.forward(speed)
        sleep(1)

    def right(self, speed=SPEED) -> None:
        self.left_motor.forward(speed)
        self.rignt_motor.stop()
        sleep(1)

    def left_tank(self, speed=SPEED) -> None:
        self.left_motor.backward(speed)
        self.rignt_motor.forward(speed)
        sleep(1)

    def rignt_tank(self, speed=SPEED) -> None:
        self.left_motor.forward(speed)
        self.rignt_motor.backward(speed)
        sleep(1)
