from canvas import Canvas
from visualize import visualize_values
class Simulation:
    def __init__(self):
        self.canvas = None
        self.walker = None

    def create_canvas(self, n, m):
        self.canvas = Canvas(n, m)
        print(f"{n}x{m} canvas created.")
        return None

    def visualize_canvas(self):
        visualize_values(self.canvas.get_values())
        return None

    def add_walker(self, walker):
        self.walker = walker
        self.set_random_walker_position()
        self.color_position_walker()
        self.update_view_walker()
        self.walker.init_memory()
        return None
    def update_view_walker(self):
        self.walker.update_view(self.canvas)
    def color_position_walker(self):
        self.canvas.add_walked(self.walker)
    def set_random_walker_position(self):
        random_position = self.canvas.get_random_position()
        self.walker.set_position(random_position)
        print(f"Walker's position set to {self.walker.position}")
        return None
    def update_memory_walker(self, direction):
        self.walker.update_memory(direction)

    # # this function colours the current position
    # self.canvas.add_walked(self.walker)

    def move_walker(self,direction=None):
        if direction is None:
            print("move_walker() needs direction, 'up','down', 'left', 'right'")

        if "up" == direction:
            self.walker.move_up()
            self.color_position_walker()
            self.update_view_walker()
            self.update_memory_walker(direction)

        elif "left" == direction:
            self.walker.move_left()
            self.color_position_walker()
            self.update_view_walker()
            self.update_memory_walker(direction)

        elif "down" == direction:
            self.walker.move_down()
            self.color_position_walker()
            self.update_view_walker()
            self.update_memory_walker(direction)

        elif "right" == direction:
            self.walker.move_right()
            self.color_position_walker()
            self.update_view_walker()
            self.update_memory_walker(direction)

        else:
            pass