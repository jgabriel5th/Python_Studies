# Example of the use of sets
letters = set()
while True:
    letter = input('Type: ')
    letters.add(letter.lower())

    if 'l' in letters:
        print('CONGRATULATIONS')
        break

    print(letters)