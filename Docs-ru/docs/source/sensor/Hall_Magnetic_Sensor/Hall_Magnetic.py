class Hall_Magnetic():

    def __init__(self, set_pin):
        self.set_pin = set_pin

    def get_signal(self) -> int:
        return self.set_pin.read_analog()

    def get_status(self, base_status: int, span: int = 20) -> bool:
        return True if (base_status-span < self.set_pin.read_analog()
                        < base_status + span) else False
