#%%
import numpy as np
import yaml
import sprites

#%%
# Likely use default values in solar system for now, but I might change this later.


def load_default_solars_ystem(verbose=True):
    solar_system = yaml.safe_load(open("resources/default_solar_system.yaml"))
    if verbose:
        print(solar_system)
    return solar_system


def generate_default_plannets(s, double=2):
    solar_system = load_default_solars_ystem(verbose=True)
    location = [41.317, 41.317]  # current distance of Mercury from sun.
    for p in solar_system["planets"].items():
        print(location)
        location = [location[0] * double, location[1] * double]
        sprites.bodies.Planet(p[0], p[1]["type"], s, location)


# %%
