from walkers import WalkerAnticlockwise
from simulation import Simulation



sim = Simulation()

sim.create_canvas(10, 15)
sim.add_walker(WalkerAnticlockwise())
walker = sim.walker
canvas = sim.canvas
sim.visualize_canvas()
sim.walker.get_position(), walker.get_relative_position()

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