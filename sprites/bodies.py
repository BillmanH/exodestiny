# %%
import core


class Star(core.PhysicalObject):
    '''
    Stars are single bodies floating in space
    type_ = O, B, A, F, G, K, and M
    '''

    def __init__(self, name, type_, galaxy, location=[0, 0]):
        super().__init__(name, type_, location, galaxy)
        self.orbiting_bodies = []

    def __repr__(self):
        return f"<Star {self.type}:{self.name}:{self.id}>"


class Planet(core.PhysicalObject):
    '''
    Planets are masses that orbit stars
    type_ = [terrestrial, gas, ice]
    '''

    def __init__(self, name, type_, star, location):
        super().__init__(name, type_, location, star)
        self.orbiting_bodies = []

    def __repr__(self):
        return f"<Planet {self.type}:{self.name}:{self.id}>"


# # %%
# u = core.Universe()
# g = core.Galaxy('milky way', 'spiral', [0, 0], u)
# s = Star('sol', 'G', g)
# # %%
# s2 = Star('Alpha Centauri', 'G', g, location=[1, 1])
# s1 = Star('Proxima Centauri', 'G', g, location=[1, 2])

# # %%
# p = Planet('Earth', 'terrestrial', s, location=[0, 0])
# p2 = Planet('Mars', 'terrestrial', s, location=[0, 1])

# # %%
