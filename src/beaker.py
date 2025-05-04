from game_parameters import BEAKER_CAPACITY
from liquid import Liquid
from color import Color


class Beaker:
    def __init__(self, contents: list[Liquid] = None) -> None:
        self._contents = contents if contents else []
        self._capacity = BEAKER_CAPACITY
        self._occupied_volume = None
        self._volume_remaining = None
        self._update()
        if not self._volume_is_legal():
            raise Exception("Volume of contents exceeds beaker capacity.")

    def __repr__(self):
        if self.is_empty():
            return "Beaker is empty."
        contents = (
            f"Beaker contains: {', '.join(str(liquid) for liquid in self._contents)}."
        )
        return contents

    def _append_liquid(self, liquid: Liquid = None) -> None:
        self._contents.append(liquid)
        self._update()

    def add_liquid(self, liquid: Liquid = None) -> None:
        if self.is_empty():
            self._contents.append(liquid)
        else:
            self._contents[-1] += liquid
        self._update()

    def pour(self, dest: "Beaker") -> bool:
        if self._valid_pour(dest):
            liquid = self._extract_liquid()
            dest.add_liquid(liquid)
            return True
        return False

    def is_empty(self) -> bool:
        return self._occupied_volume == 0

    def _volume_is_legal(self) -> bool:
        return self._occupied_volume <= self._capacity

    def _calculate_volume(self) -> int:
        if not self._contents:
            return 0
        volume = 0
        for liquid in self._contents:
            volume += liquid.get_volume()
        return volume

    def _update(self) -> None:
        self._occupied_volume = self._calculate_volume()
        self._volume_remaining = self._calculate_volume_remaining()

    def _extract_liquid(self, index: int = -1) -> Liquid:
        liquid = self._contents.pop(index)
        self._update()
        return liquid

    def _calculate_volume_remaining(self) -> int:
        return self._capacity - self._occupied_volume

    def _get_volume_remaining(self) -> int:
        return self._volume_remaining

    def _get_top_color(self) -> Color:
        if not self._contents:
            return None
        return self._contents[-1].get_color()

    def _get_top_volume(self) -> int:
        return self._contents[-1].get_volume()

    def _valid_pour(self, dest: "Beaker") -> bool:
        start_color, start_volume = self._get_top_color(), self._get_top_volume()
        dest_color = dest._get_top_color()
        colors_match = start_color == dest_color
        dest_enough_volume = dest._get_volume_remaining() >= start_volume
        return colors_match and dest_enough_volume or dest.is_empty()


if __name__ == "__main__":
    liquid_0 = Liquid(Color.YELLOW, 1)
    liquid_1 = Liquid(Color.BLUE, 1)
    beaker_0 = Beaker()
    beaker_1 = Beaker()
    print(beaker_0)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    print("Adding liquid_0 to beaker_0")
    beaker_0._append_liquid(liquid_0)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    print(beaker_0)
    print("Adding liquid_1 to beaker_0")
    beaker_0._append_liquid(liquid_1)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    print(beaker_0)
    print(beaker_1)
    print("Pouring beaker_0 into beaker_1")
    beaker_0.pour(beaker_1)
    print(beaker_0)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    print(beaker_1)
    print(beaker_1._occupied_volume, beaker_1._volume_remaining)
    print("Adding liquid_1 to beaker_0")
    beaker_0._append_liquid(liquid_1)
    print(beaker_0)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    beaker_0.pour(beaker_1)
    print(beaker_0)
    print(beaker_0._occupied_volume, beaker_0._volume_remaining)
    print(beaker_1)
    print(beaker_1._occupied_volume, beaker_1._volume_remaining)
