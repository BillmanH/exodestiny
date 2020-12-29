#%%
from django.test import TestCase
from modules.sprites import core, bodies
from modules import generators
from pprint import pprint

# baseline stuff
test_world_name = "billmanh"

print(f"using {test_world_name}")

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

u = generators.new_universe(test_world_name)
# The root path is different when running tests.
generators.save_universe(u, test_world_name, root_path="")
u = generators.load_universe(test_world_name, root_path="")
print("CAN SAVE AND LOAD UNIVERSE")

# solar system screen
planet_data = u.children[0].children[0].get_planet_data()
pprint(planet_data)


# %%
