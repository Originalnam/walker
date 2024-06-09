import numpy as np
class Walker:
    def __init__(self, x=0, y=0):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def walk(self, position_info):
        pass
    def move_up(self):
        x, y = self.position
        self.position = (x - 1, y)

    def move_left(self):
        x, y = self.position
        self.position = (x, y - 1)

    def move_down(self):
        x, y = self.position
        self.position = (x + 1, y)

    def move_right(self):
        x, y = self.position
        self.position = (x, y + 1)

class WalkerAnticlockwise(Walker):
    def __init__(self, x=0, y=0):
        Walker.__init__(self, x=0, y=0)
    def walk(self, position_info):
        position_info = position_info
        up = position_info[0][1]
        left = position_info[1][0]
        down = position_info[2][1]
        right = position_info[1][2]

        if up == 0:
            self.move_up()

        elif left == 0:
            self.move_left()

        elif down == 0:
            self.move_down()

        elif right == 0:
            self.move_right()

        else:
            print("No unwalked tiles available")
