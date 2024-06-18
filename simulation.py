from canvas import Canvas
from visualize import visualize_values
class Simulation:
    def __init__(self):
        self.canvas = None
        self.walker = None
        self.walkers = {}

    def create_canvas(self, n, m):
        self.canvas = Canvas(n, m)
        print(f"{n}x{m} canvas created.")
        return None
    def visualize_canvas(self):
        visualize_values(self.canvas.get_values())
        return None
    def add_walkers(self, walkers):
        for walker in walkers:
            self.add_walker(walker)
    def update_walkerdict(self, walker):
        self.walkers[walker] = walker.get_position()
    def add_walker(self, walker):
        self.walker = walker
        self.set_random_walker_position()
        self.update_walkerdict(walker)
        self.color_position_walker()
        self.update_view_walker()
        self.walker.init_memory()
    def update_view_walker(self):
        self.walker.update_view(self.canvas)
    def color_position_walker(self):
        self.canvas.add_walked(self.walker)
    def set_random_walker_position(self):
        random_position = self.canvas.get_random_position()
        while random_position in self.walkers.values():
            random_position = canvas.get_random_position()
        self.walker.set_position(random_position)
        print(f"Walker's position set to {self.walker.position}")
    def update_memory_walker(self, direction):
        self.walker.update_memory(direction)
    def move_walkers(self, direction=None):
        if direction is None:
            print("move_walker() needs direction, 'up','down', 'left', 'right'")
        for walker in self.walkers:
            self.walker = walker
            if "up" == direction:
                self.move_walker("up")
            elif "left" == direction:
                self.move_walker("left")
            elif "down" == direction:
                self.move_walker("down")
            elif "right" == direction:
                self.move_walker("right")
            else:
                pass
    def move_walker(self, direction=None):
        if direction is None:
            print("move_walker() needs direction, 'up','down', 'left', 'right'")
            return
        if direction == "up":
            self.walker.move_up()
        elif direction == "left":
            self.walker.move_left()
        elif direction == "down":
            self.walker.move_down()
        elif direction == "right":
            self.walker.move_right()
        else:
            print(f"Invalid direction: {direction}")
            return
        self.color_position_walker(self.walker)
        self.update_view_walker(self.walker)
        self.update_memory_walker(self.walker, direction)
        self.update_walkerdict(self.walker)