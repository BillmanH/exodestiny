#%%
import numpy as np
import yaml
from . import sprites
import pickle
import os

#%%
# Likely use default values in solar system for now, but I might change this later.


def load_default_solars_ystem():
    solar_system = yaml.safe_load(open("resources/default_solar_system.yaml"))
    return solar_system


def generate_default_plannets(s, double=2):
    solar_system = load_default_solars_ystem()
    location = [41.317, 41.317]  # current distance of Mercury from sun.
    for p in solar_system["planets"].items():
        location = [location[0] * double, location[1] * double]
        sprites.bodies.Planet(p[0], p[1]["type"], s, location)


# %%
def new_universe(user):
    u = sprites.core.Universe()
    g = sprites.core.Galaxy("milky way", "spiral", [0, 0], u)
    s = sprites.bodies.Star("sol", "G", g)
    sprites.bodies.Star("Alpha Centauri", "G", g, location=[1, 1])
    sprites.bodies.Star("Proxima Centauri", "G", g, location=[1, 2])
    generate_default_plannets(s, double=2)
    return u


def load_universe(user, root_path="exodest/"):
    u = pickle.load(open(root_path + "pickles/" + user + "_u.p", "rb"))
    return u


def save_universe(u, user, root_path="exodest/"):
    pickle.dump(u, open(root_path + "pickles/" + user + "_u.p", "wb"))

