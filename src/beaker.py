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
        self._volume_remaining = self._get_volume_remaining()

    def _volume_is_legal(self) -> bool:
        return self._occupied_volume <= self._capacity

    def _calculate_volume(self) -> int:
        if not self._contents:
            return 0
        volume = 0
        for liquid in self._contents:
            volume += liquid.get_volume()
        return volume

    def _get_volume_remaining(self) -> int:
        return self._capacity - self._occupied_volume

    def pour(self, dest: "Beaker") -> bool:
        # TODO: complete pour logic
        start_color, start_volume = self._get_top_color(), self._get_top_volume()
        dest_color, dest_volume = dest._get_top_color(), dest._get_top_volume()
        if start_color is not dest_color:
            return False
        # TODO: handle destination beaker volume_remaining check
        if self._occupied_volume == 0:
            return True
        pass

    def _get_top_color(self) -> Color:
        return self._contents[-1].get_color()

    def _get_top_volume(self) -> int:
        return self._contents[-1].get_volume()


if __name__ == "__main__":
    print(Color.BLUE is Color.BLUE)
