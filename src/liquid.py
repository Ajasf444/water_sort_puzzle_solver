from color import Color


class Liquid:
    def __init__(self, color: Color = None, volume: int = None):
        self._color = color
        self._volume = volume

    def __iadd__(self, other: "Liquid") -> "Liquid":
        self._volume += other._volume
        return self

    def get_color(self) -> Color:
        return self._color

    def get_volume(self) -> int:
        return self._volume

    def __repr__(self):
        return f"({self.get_color()}, {self.get_volume()})"


if __name__ == "__main__":
    test_liquid = Liquid(Color.YELLOW, 2)
    print(test_liquid)
