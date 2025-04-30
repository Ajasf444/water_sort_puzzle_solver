from game_parameters import BEAKER_CAPACITY
from liquid import Liquid


class Beaker:
    def __init__(self, contents: list[Liquid] = None):
        self._contents = contents if contents else []
        self._capacity = BEAKER_CAPACITY
        self._occupied_volume = self._calculate_volume()
        if self._occupied_volume > self._capacity:
            raise Exception("Volume of contents exceeds beaker capacity.")
        self._volume_remaining = self._get_volume_remaining()

    def _calculate_volume(self):
        if not self._contents:
            return 0
        volume = 0
        for liquid in self._contents:
            volume += liquid.get_amount()
        return volume

    def _get_volume_remaining(self):
        return self._capacity - self._occupied_volume


if __name__ == "__main__":
    pass
