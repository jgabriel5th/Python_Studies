'''
Closure and functions that return other functions
'''

def createGreeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet # By returning the function without closing () it'll create a closure afterwards.

# If return a function closing () it'll work normally but it won't create a closure.
# Example:
def mathNumbers(x, y):
    def sumNumbers():
        return x + y
    return sumNumbers()

sum1 = mathNumbers(3, 4)
print(sum1)

good_morning = createGreeting('Good morning')
good_afternoon = createGreeting('Good afternoon')
print(good_morning('John')) # <- Closure 
print(good_afternoon('Elícia')) # <- Closure

for name in ['Mary', 'Abraão', 'Louise']:
    print(good_morning(name))
    print(good_afternoon(name))