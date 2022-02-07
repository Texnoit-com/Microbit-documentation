from microbit import *

class Joystick:

    def __init__( self, x_axis:MicroBitAnalogDigitalPin, y_axis:MicroBitAnalogDigitalPin, button:MicroBitDigitalPin):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.button = button

    def get_x(self) -> int:
        return self.x_axis.read_analog()

    def get_y(self) -> int:
        return self.y_axis.read_analog()    

    def click(self) -> bool:
        if self.button.read_digital() == 1:
            return True 
        else: 
            return False
    
    def play_cross(self, limit=300) -> str:
        if self.x_axis.read_analog() < limit: return "Left"
        if self.x_axis.read_analog() > limit*2: return "Right"
        if self.y_axis.read_analog() < limit: return "Up"
        if self.y_axis.read_analog() > limit*2: return "Down"
        if self.y_axis.read_analog() > limit and self.y_axis.read_analog() < limit*2 and self.x_axis.read_analog() > limit and self.x_axis.read_analog() < limit*2:
            return "0"
    
    def play_diagonal(self, limit=300)-> str:
        if self.y_axis.read_analog()  < limit and limit < self.x_axis.read_analog()  < limit*2: return "Up"
        if self.y_axis.read_analog()  < limit and self.x_axis.read_analog()  > limit*2: return "Up-Right"
        if self.x_axis.read_analog()  > limit*2 and limit < self.y_axis.read_analog()  < limit*2: return "Right"
        if self.y_axis.read_analog()  > limit*2 and self.x_axis.read_analog()  > limit*2: return "Down-Right"
        if self.y_axis.read_analog()  > limit*2 and limit < self.x_axis.read_analog()  < limit*2: return "Down"
        if self.x_axis.read_analog()  < limit and self.y_axis.read_analog()  > limit*2 : return "Down-Left"
        if self.x_axis.read_analog()  < limit and limit < self.y_axis.read_analog()  < limit*2: return "Left"
        if self.x_axis.read_analog()  < limit and self.y_axis.read_analog()  < limit : return "Up-Left"
        if self.y_axis.read_analog() > limit and self.y_axis.read_analog() < limit*2 and self.x_axis.read_analog() > limit and self.x_axis.read_analog() < limit*2:
            return "0"

