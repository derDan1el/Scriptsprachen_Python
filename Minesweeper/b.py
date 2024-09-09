from a import Dummy
class KI_Minesweeper(buttons = []):
    def __init__(self, buttons):
        self.buttons = buttons
        self.dummy = Dummy()
    def get_next_move(self):
        return self.dummy.get_next_move()