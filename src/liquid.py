from color import Color


class Liquid:
    def __init__(self, color: Color = None, amount: int = None):
        self._color = color
        self._amount = amount

    def get_color(self):
        return self._color

    def get_amount(self):
        return self._amount
