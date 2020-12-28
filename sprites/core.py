# The core of all objects the sprite
# %%
import uuid
import yaml


class TwoObjectsCannotOccupyTheSameSpaceException(Exception):
    pass


class Sprite:
    """
    The core of all objects is a sprite. 
    """

    _instances = set()

    def __init__(self):
        self.id = str(uuid.uuid1())


class PhysicalObject(Sprite):
    """
    Physical objects have a location, because they exist in space.
    """

    def __init__(self, name, type_, location, parent=None):
        super().__init__()
        self.parent = parent
        self.name = name
        self.type = type_
        if parent != None:
            if any([s.location == location for s in parent.children]):
                print(
                    f"{[c.name for c in parent.children if c.location == location]} conflicts at that location:{location}"
                )
                raise TwoObjectsCannotOccupyTheSameSpaceException
            else:
                self.location = location
                self.parent.children.append(self)
        self.children = []


class Abstraction(Sprite):
    """
    Abstractions don't exist in physical space, but are bore by annother object.
    """

    def __init__(self, bearer):
        super().__init__()
        self.bearer = bearer


class Universe(PhysicalObject):
    """
    the universe is the core object, all other objects are connected to it.
    """

    def __init__(self):
        super().__init__("the universe", "normal", None, None)

        print("A universe is born!")


class Galaxy(PhysicalObject):
    """
    A galaxy is a collection of Stars
    """

    def __init__(self, name, type_, location, parent=None):
        super().__init__(name, type_, location, parent)

    def __repr__(self):
        return f"<Galaxy {self.type}:{self.name}:{self.id}>"

