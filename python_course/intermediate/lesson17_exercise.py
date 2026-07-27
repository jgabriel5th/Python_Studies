# Exercise - system of questions and answers.

question = [
    {
        'Question': 'Which is the only national football team that has won five world cup?',
        'Options': ['Argentina', 'Germany', 'England', 'Brazil', 'Italy'],
        'Answer': 'Brazil',
    },
    {
        'Question': 'Who has created Judo?',
        'Options': ['Hélio Gracie', 'Jigoro Kano', 'Tomita Tsunejiro', 'Gichin Funakoshi', 'Nai Khanom Tom'],
        'Answer': 'Jigoro Kano',
    },
    {
        'Question': 'Who has created Python?',
        'Options': ['Guido Van Rossum', 'Alan Turing', 'Brendan Eich', 'Rasmus Lerdorf', 'James Gosling'],
        'Answer': 'Guido Van Rossum',
    },
]
right_answers = 0
for option in range(3):
    question_name = question[option]['Question']
    print(question_name)
    options = question[option]['Options']
    right_answer = question[option]['Answer']
    for index, name in enumerate(options):
        print(f'{index}) {name}')
    answer = input('Type the right answer: ')
    if answer == right_answer:
        right_answers += 1
        print(f'Right answer! ✅{right_answers}/3')
    elif answer != right_answer:
        print(f'Wrong answer ❌{right_answers}/3')
    else:
        print('You typed an invalid value.')

def answerAnalyzer(x):
    if x == 3:
        return f'You got 100% of the answers right'
    elif x == 2:
        x = 100
        return f'You got {(0.66 * x)}% of the answer right'
    elif x == 1:
        x = 100
        return f'You got {(0.33 * x)}% of the answer right'
    else:
        return 'You got 0% of the test right.'

print(answerAnalyzer(right_answers))
