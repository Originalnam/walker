from canvas import Canvas
from visualise import visualise_values
class Simulation:
    def __init__(self):
        self.canvas = None
        self.walker = None

    def create_canvas(self, n, m):
        self.canvas = Canvas(n, m)
        print(f"{n}x{m} canvas created.")
        return None

    def visualise_canvas(self):
        visualise_values(self.canvas.get_values())
        return None

    def add_walker(self, walker):
        self.walker = walker
        return None

    def set_random_walker_position(self):
        # this function colours the starting position
        random_position = self.canvas.get_random_position()
        self.walker.set_position(random_position)
        self.canvas.add_walked(self.walker)
        print(f"Walker's position set to {self.walker.position}")
        return None

    def walk_walker(self):
        pass