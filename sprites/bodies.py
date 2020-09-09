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


#
# %%
u = core.Universe()
g = core.Galaxy('milky way', 'spiral', [0, 0], u)
s = Star('sol', 'G', g)
# %%
s2 = Star('another star', 'G', g, location=[1, 1])
s1 = Star('yet another star', 'G', g, location=[1, 2])


# %%
