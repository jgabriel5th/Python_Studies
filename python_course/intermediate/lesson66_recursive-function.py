# Recursive function and recursivity
# - functions that can call themselves
# - useful to share big problems in smaller parts
# Every recursive function must have:
# - A problem that can be split in smaller parts
# - A recursive case that solves the small problem
# - A base case that stops the recursion
# - factorial - n! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursive(begin=0, end=10):
    print(begin, end)
    # Base case
    if begin >= end:
        return end
    
    # Recursive case
    # count till reach the end
    begin += 1
    return recursive(begin, end)

print(recursive())