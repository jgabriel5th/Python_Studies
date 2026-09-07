# @property - a getter in Pythonic mode
# getter - a method to obtain an attribute
# color -> get_cor()
# Pythonic mode - Python mode to do things.
# @property is an object property, it is a
# method that behaves as an attribute.
# Usually it is used in the following situations:
# - as getter
# - to avoid breaking client code
# - to enable setter
# - to execute actions upon obtaining an attribute.
# Client code - it's the code that uses your code.
class Pen:
    def __init__(self, color, pen_cap):
        self.color_ink = color
        self.cap = pen_cap

    @property
    def color(self):
        print('PROPERTY')
        return self.color_ink

    @property
    def pen_cap(self):
        return self.cap
#############################

pen = Pen('Blue', 'Yellow')
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.pen_cap)
##############################

# class Pen:
#     def __init__(self, color):
#         self.color = color

#     def get_cor(self): # getter/it protects the attribute
#         print('GET COR') # action
#         return self.color

# #############################

# pen = Pen('Blue')
# print(pen.get_cor())
# print(pen.get_cor())
# print(pen.get_cor())
# print(pen.get_cor())
# print(pen.get_cor())