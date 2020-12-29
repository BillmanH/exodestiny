from django.test import TestCase
from sprites import core, bodies
import generators

#  The galaxy
## Check that plannets can generate.
u = core.Universe()
g = core.Galaxy("milky way", "spiral", [0, 0], u)
s = bodies.Star("sol", "G", g)
# %%
s2 = bodies.Star("Alpha Centauri", "G", g, location=[1, 1])
s1 = bodies.Star("Proxima Centauri", "G", g, location=[1, 2])
generators.generate_default_plannets(s, double=2)
print("PLANETS ARE ABLE TO LOAD")


# Build a new universe
u = generators.new_universe("billmanh")
generators.save_universe(u, "billmanh")
u = generators.load_universe("billmanh")
print("CAN SAVE AND LOAD UNIVERSE")

