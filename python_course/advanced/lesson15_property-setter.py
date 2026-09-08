# @property + @setter - getter and setter in Pythonic mode
# - as getter
# - to avoid breaking client code
# - to enable setter
# - to execute actions upon obtaining an attribute
# Attributes that begin with one or two underlines must not
# be used out of the class.
class Pen:
    def __init__(self, color):
        # private protected
        self._color = color
        self._cap_color = None

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def cap_color(self):
        return self._cap_color

    @cap_color.setter
    def cap_color(self, value):
        self._cap_color = value


pen = Pen('Blue')
pen.color = 'Pink'
pen.cap_color = 'Black'
print(pen.color)
print(pen.cap_color)