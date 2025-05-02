from game_parameters import BEAKER_CAPACITY
from liquid import Liquid
from color import Color


class Beaker:
    def __init__(self, contents: list[Liquid] = None) -> None:
        self._contents = contents if contents else []
        self._capacity = BEAKER_CAPACITY
        self._occupied_volume = self._calculate_volume()
        if not self._volume_is_legal():
            raise Exception("Volume of contents exceeds beaker capacity.")
        self._volume_remaining = self.calculate_volume_remaining()

    def _volume_is_legal(self) -> bool:
        return self._occupied_volume <= self._capacity

    def _calculate_volume(self) -> int:
        if not self._contents:
            return 0
        volume = 0
        for liquid in self._contents:
            volume += liquid.get_volume()
        return volume

    def _calculate_volume_remaining(self) -> int:
        return self._capacity - self._occupied_volume

    def _get_volume_remaining(self) -> int:
        return self._volume_remaining

    def pour(self, dest: "Beaker") -> bool:
        if self._valid_pour(dest):
            # TODO: complete pour logic
            return True
        return False

    def _get_top_color(self) -> Color:
        return self._contents[-1].get_color()

    def _get_top_volume(self) -> int:
        return self._contents[-1].get_volume()

    def _valid_pour(self, dest: "Beaker") -> bool:
        start_color, start_volume = self._get_top_color(), self._get_top_volume()
        dest_color, dest_volume = dest._get_top_color(), dest._get_top_volume()
        dest_is_empty = dest._get_volume_remaining() == 0
        return True or False


if __name__ == "__main__":
    print(Color.BLUE is Color.BLUE)
