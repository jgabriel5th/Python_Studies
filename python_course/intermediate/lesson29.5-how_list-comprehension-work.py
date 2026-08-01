'''
This actually is not a lesson, because I created this one to exercise the reading and the execution
of list comprehension.
In Python, the syntax of list comprehension is: [expression for variable in iterable if condition(optional)]
However, this is tricky, because the execution doesn't follow the syntax order. I think that's one of the main
reasons why it confuses new Python devs, so I studied a way to comprehend the execution and I'll apply here in order
to practice as well.
'''

# How it works - Syntax
# list_example = [expression for variable in iterable if condition]
# Order of reading: [for variable in iterable if condition expression] <- That's how Python will execute the code
list1 = [number if number > 1 else -1 for number in range(10) if number < 5]
print(list1)

# For a better comprehension of how Python executes list comprehension:
list1 = []
for number in range(10): # for variable in iterable 1°
    if number < 5: # if condition 2°
        if number > 1:
            list1.append(number) # expression 3°
        else:
            list1.append(-1)
print(list1)
# That's basically the same order that Python executes list1 on line 13.

'''
So, my advice is: when reading a list comprehension follow this order:
for variable in iterable - it'll happen first.
if condition - just if it is there.
expression - that'll be the last one.
'''


