# %%
from sprites import core


class celestialBody(core.PhysicalObject):
    """
    Celestial bodies are objects that you would see from a global view of a solar system.
    """

    def __init__(self, name, type_, parent, location):
        super().__init__(name, type_, parent, location)
        self.orbiting_bodies = []


class Star(celestialBody):
    """
    Stars are celestialBodies floating in space
    type_ = O, B, A, F, G, K, and M
    """

    def __init__(self, name, type_, parent, location=[0, 0]):
        super().__init__(name, type_, location, parent)
        self.orbiting_bodies = []

    def __repr__(self):
        return f"<Star {self.type}:{self.name}:{self.id}>"


class Planet(celestialBody):
    """
    Planets are celestialBodies that orbit stars
    type_ = [terrestrial, gas, ice]
    location is expressed in millions of miles
    """

    def __init__(self, name, type_, parent, location, **kwargs):
        super().__init__(name, type_, location, parent)
        self.orbiting_bodies = []

    def __repr__(self):
        return f"<Planet {self.type}:{self.name}:{self.id}>"

