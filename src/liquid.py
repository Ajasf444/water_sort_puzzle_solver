from color import Color


class Liquid:
    def __init__(self, color: Color = None, amount: int = None):
        self._color = color
        self._amount = amount

    def get_color(self) -> Color:
        return self._color

    def get_amount(self) -> int:
        return self._amount

    def __repr__(self):
        return f"{self.get_color()}: {self.get_amount()}"


if __name__ == "__main__":
    test_liquid = Liquid(Color.YELLOW, 2)
    print(test_liquid)
