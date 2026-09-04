# Exercise - Tasklist with undo and redo
# todo = [] -> tasklist
# todo = ['make coffee'] -> Append make coffee
# todo = ['make coffee', 'walk'] -> append walk
# undo = ['make coffee',] -> Redo ['walk']
# undo = [] -> Redo ['walk', 'make coffee']
# redo = todo ['make coffee']
# redo = todo ['make coffee', 'walk']
def toDo(task, tasklist):
    task = task.strip()
    if not task:
        print('None task was inserted')
        return # return in this case will stop function here.
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


def main():
    tasklist = []
    task_redo = []
    while True:
        print('---TASKLIST---')
        print('Type A or add to add tasks\n' \
        'Type U or undo to undo tasks\n' \
        'Type R or redo to redo tasks\n' \
        'Type L or list to list tasks\n' \
        'Type E or exit to exit the program')
        choice = input('Type: ').lower()

        if choice == 'a' or choice == 'add':
            task = input('Insert a task: ')
            toDo(task, tasklist)
        elif choice == 'u' or choice == 'undo':
            unDo(tasklist, task_redo)
        elif choice == 'r' or choice == 'redo':
            reDo(tasklist, task_redo)
        elif choice == 'l' or choice == 'list':
            toList(tasklist)
        elif choice == 'e' or choice == 'exit':
            print('Thanks for using the Tasklist!')
            print('Finishing the program...')
            break
main()

    

