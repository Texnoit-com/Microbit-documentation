class TEMT():

    def __init__(self, set_pin):
        self.set = set

    def get_signal(self) -> int:
        return self.set.read_analog()
