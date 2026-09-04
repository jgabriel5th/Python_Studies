import sys
def toDo(tasklist):
    task = input('Insert a task: ').strip()
    if not task:
        print('None task was inserted')
        return # return in this case will stop function here. Guard clause.
    tasklist.append(task)
    print(f'{task=} was added to tasklist!')

def toList(tasklist):
    if not tasklist:
        print('None task was informed')
        return 
    print('Tasks:')
    for task in tasklist:
        print(f'{task}')

def unDo(tasklist, task_redo):
    if not tasklist:
        print('None tasks to undo')
        return
    task = tasklist.pop()
    print(f'{task=} was removed from tasklist')
    task_redo.append(task)

def reDo(tasklist, task_redo):
    if not task_redo:
        print('None tasks to redo')
        return
    task = task_redo.pop()
    tasklist.append(task)
    print(f'{task=} was added again to tasklist')

def exitProgram():
    print('Thanks for using the Tasklist!\n' \
    'Finishing the program...')
    sys.exit()

def main():
    tasklist = []
    task_redo = []
    while True:
        print('---TASKLIST---')
        print('Type Add to add tasks\n' \
        'Type Undo to undo tasks\n' \
        'Type Redo to redo tasks\n' \
        'Type List to list tasks\n' \
        'Type Exit to exit the program')
        choice = input('Type: ').lower()
        commands = {
            'add': lambda: toDo(tasklist),
            'undo': lambda: unDo(tasklist, task_redo),
            'redo': lambda: reDo(tasklist, task_redo),
            'list': lambda: toList(tasklist),
            'exit': lambda: exitProgram(),
        }
        command = commands.get(choice)
        if command is not None:
            command()
        else:
            print('Invalid command')

main()