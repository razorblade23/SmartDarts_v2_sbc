from typing import Protocol


class GPIOInterface(Protocol):
    DEBOUNCE_TIME: float

    def setup_output(self, pin: int): ...

    def setup_input(self, pin: int): ...

    def set_pin_high(self, pin: int): ...

    def set_pin_low(self, pin: int): ...

    def read_pin(self, pin: int) -> bool: ...
