from walkers import Walker, WalkerAnticlockwise
from simulation import Simulation

sim = Simulation()

sim.create_canvas(200, 100)
walker = sim.walker
canvas = sim.canvas
sim.add_walkers([
    WalkerAnticlockwise(view_depth = 2),
    Walker(view_depth = 2),
    WalkerAnticlockwise(view_depth = 2)
])
sim.visualize_canvas()
print(f'Walkers: {sim.walkers}')

sim = Simulation()

sim.create_canvas(200, 100)
sim.add_walker(WalkerAnticlockwise(view_depth = 2))
walker = sim.walker
canvas = sim.canvas
sim.visualize_canvas()
print(sim.walker.get_position(), walker.get_relative_position())
print(f'Walkers: {sim.walkers}')

sim.walker.visualize_view(), walker.visualize_memory()
sim.walker.get_position(), walker.get_relative_position()


sim.move_walker("up")
sim.visualize_canvas()
sim.walker.get_position(), walker.get_relative_position()

sim.move_walker("left")
sim.visualize_canvas()
sim.walker.get_position(), walker.get_relative_position()

sim.move_walker("down")
sim.visualize_canvas()
sim.walker.get_position(), walker.get_relative_position()

sim.move_walker("right")
sim.visualize_canvas()
sim.walker.get_position(), walker.get_relative_position()

sim.walker.visualize_view(), walker.visualize_memory()
sim.walker.get_position(), walker.get_relative_position()