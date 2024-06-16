import numpy as np

class Canvas:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.canvas = np.zeros((n, m), dtype=int)

    def add_walked(self, walker):
        x, y = walker.get_position()
        if 0 <= x < self.n and 0 <= y < self.m:
            self.canvas[x, y] = 1
        else:
            raise ValueError("Coordinates are out of bounds")

    def get_values(self):
        return self.canvas

    def get_random_position(self):
        x = np.random.randint(0, self.n)
        y = np.random.randint(0, self.m)
        return x, y

    def get_position_info(self, position, view_depth):
        x , y = position
        values = []
        for i in range(x - view_depth, x + 1 + view_depth):
            row_values = []
            for j in range(y - view_depth, y + 1 + view_depth):
                if 0 <= i < self.n and 0 <= j < self.m:
                    row_values.append(self.canvas[i, j])
                else:
                    row_values.append(-1)
            values.append(row_values)
        return values
