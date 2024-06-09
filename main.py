from walkers import WalkerAnticlockwise
from simulation import Simulation

sim = Simulation()

sim.create_canvas(10, 15)
sim.add_walker(WalkerAnticlockwise())

sim.set_random_walker_position()
sim.visualise_canvas()