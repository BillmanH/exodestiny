from django.test import TestCase
from sprites import core, bodies
import generators

#

## Check that plannets can generate.
u = core.Universe()
g = core.Galaxy("milky way", "spiral", [0, 0], u)
s = bodies.Star("sol", "G", g)
# %%
s2 = bodies.Star("Alpha Centauri", "G", g, location=[1, 1])
s1 = bodies.Star("Proxima Centauri", "G", g, location=[1, 2])

# %%
# populate the solar system with default planets:
generators.generate_default_plannets(s, double=2)

