# %%
class Sprite:
    def __init__(self, id):
        self.id = id

    def get_id(self):
        print(self.id)


class PhysicalObject(Sprite):
    def __init__(self, id, location):
        super().__init__(id)
        self.location = location


class Abstraction(Sprite):
    def __init__(self, id, bearer):
        super().__init__(id)
        self.bearer = bearer


# %%
s = Sprite('1')

# %%
a = Abstraction("1", "Carl")
p = PhysicalObject("2", "ship")
# %%
