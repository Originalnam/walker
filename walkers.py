import numpy as np
from visualize import visualize_values
class Walker:
    def __init__(self, x=0, y=0):
        self.position = (x, y)
        self.view = np.full((3, 3), -2)
        self.memory = self.view.copy()
        self.offset_x = 0
        self.offset_y = 0
        self.relative_position = (1 + self.offset_x, 1 + self.offset_y)
    def update_relative_position(self):
        self.relative_position = (1 + self.offset_x, 1 + self.offset_y)
    def get_relative_position(self):
        return self.relative_position
    def get_position(self):
        return self.position
    def set_position(self, position):
        self.position = position
    def update_view(self, canvas):
        self.view = np.array(canvas.get_position_info(self.get_position()))
    def visualize_view(self):
        visualize_values(self.view, (1, 1))
    def init_memory(self):
        self.memory = self.view.copy()
    def update_memory(self, direction = None):
        memory = self.memory.copy()

        if "up" == direction:
            # add row of unseen tiles (= -2) at top of memory if we're at the upper edge of our memory
            if self.offset_x == 0:
                new_row_top = np.full((1, memory.shape[1]), -2)
                self.memory = np.vstack([new_row_top, memory])

            # update memory at relative position with new view
            x, y = self.relative_position
            self.memory[x - 1:x + 2, y - 1:y + 2] = self.view.copy()

        elif "left" == direction:
            # add column of unseen tiles (= -2) left of memory if we're at the left edge of memory
            if self.offset_y == 0:
                new_first_column = np.full((memory.shape[0], 1), -2)
                self.memory = np.hstack([new_first_column, memory])

            # update memory at relative position with new view
            x, y = self.relative_position
            self.memory[x - 1:x + 2, y - 1:y + 2] = self.view.copy()

        elif "down" == direction:
            # add row of unseen tiles (= -2) at bottom of memory if we're past the lower edge of memory
            if self.offset_x > memory.shape[0]-3:
                new_row_bottom = np.full((1, memory.shape[1]), -2)
                self.memory = np.vstack([memory,new_row_bottom])

            # update memory at relative position with new view
            x, y = self.relative_position
            self.memory[x - 1:x + 2, y - 1:y + 2] = self.view.copy()

        elif "right" == direction:
            # add column of unseen tiles (= -2) right of memory if we're at the left edge of memory
            if self.offset_y > memory.shape[1]-3:
                new_last_column = np.full((1, memory.shape[1]), -2)
                self.memory = np.hstack([memory,new_last_column])

            # update memory at relative position with new view
            x, y = self.relative_position
            self.memory[x - 1:x + 2, y - 1:y + 2] = self.view.copy()

        else:
            print("update_memory() needs direction, 'up','down', 'left', 'right'")

    def visualize_memory(self):
        visualize_values(self.memory, self.get_relative_position())

    # copy the current view top row at relative position

#   if ...
            # copy current view at relative position
            # update memory

        # new_memory = np.full_like(self.memory, -1)
        # start_x = max(0, min(self.view.shape[0] + self.offset_x, self.memory.shape[0]))
        # start_y = max(0, min(self.view.shape[1] + self.offset_y, self.memory.shape[1]))
        # end_x = max(0, min(start_x + self.view.shape[0], self.memory.shape[0]))
        # end_y = max(0, min(start_y + self.view.shape[1], self.memory.shape[1]))
        # new_memory[start_x - self.offset_x:end_x - self.offset_x, start_y - self.offset_y:end_y - self.offset_y] = self.view[max(-self.offset_x, 0):min(self.view.shape[0] - self.offset_x, self.memory.shape[0] - self.offset_x), max(-self.offset_y, 0):min(self.view.shape[1] - self.offset_y, self.memory.shape[1] - self.offset_y)]
        # self.memory = new_memory

    def move_up(self):
        x, y = self.position
        self.position = (x - 1, y)
        # adjust offset from original position check for negative numbers; update relative_position
        self.offset_x -= 1
        if self.offset_x < 0:
            self.offset_x = 0
        self.update_relative_position()
    def move_left(self):
        x, y = self.position
        self.position = (x, y - 1)
        self.offset_y -= 1
        if self.offset_y < 0:
            self.offset_y = 0
        self.update_relative_position()
    def move_down(self):
        x, y = self.position
        self.position = (x + 1, y)
        self.offset_x += 1
        self.update_relative_position()

    def move_right(self):
        x, y = self.position
        self.position = (x, y + 1)
        self.offset_y += 1
        self.update_relative_position()

class WalkerAnticlockwise(Walker):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
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
