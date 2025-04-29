from game_parameters import BEAKER_CAPACITY


class Beaker:
    def __init__(self, contents=None):
        self.contents = contents if contents else []
        self.capacity = BEAKER_CAPACITY
