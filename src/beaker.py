from game_parameters import BEAKER_CAPACITY
from liquid import Liquid


class Beaker:
    def __init__(self, contents: list[Liquid] = None):
        self._contents = contents if contents else []
        self._capacity = BEAKER_CAPACITY
        self._occupied_volume = (
            None  # TODO: account for the amount of liquid in contents and capacity
        )
        self._volume_remaining = None  # TODO: account for occupied_volume


if __name__ == "__main__":
    pass
