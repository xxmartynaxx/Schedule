import pprint
from operator import itemgetter
from datetime import datetime

OPTIONS = ['TASKS', 'FUTURE TASKS', 'SCHEDULE', 'EXIT']
TASKS_OPTIONS = ['See the list of the tasks', 'Add the task', 'Remove the tasks', 'Go back']
FUTURE_TASKS_OPTIONS = ['See the list of the future tasks', 'Add the future task', 'Remove the future tasks', 
                        'Move the future tasks to daily tasks', 'Go back']
SCHEDULE_OPTIONS = ['See upcoming events', 'Add the event', 'Remove the event', 'See the uni timetable',
                    'Edit the uni timetable', 'Go back']


def main_options():

    print()
    print(' -- Choose one of the options below -- ')
    for i, option in enumerate(OPTIONS, start=1):
        print(f'{i}. {option}')
    choice = int(input())

    if choice == len(OPTIONS):
        # 'EXIT' should be the last option in OPTIONS
        exit()
    else:
        show_options(choice)


def show_options(t_f_s):
    # t_f_s means 'task or future or schedule' (1 for TASKS, 2 for FUTURE and 3 for SCHEDULE)
    print()
    print(' -- What would you like to do? -- ')

    if t_f_s == 1:
        for i, option in enumerate(TASKS_OPTIONS, start=1):
            print(f'{i}. {option}')
        choice = int(input())

        if choice == len(TASKS_OPTIONS):
            # 'go back' option should be the last option in TASKS_OPTIONS
            main_options()
        elif choice in [1,2,3]:
            for option in SWITCH:
                if option == choice:
                    SWITCH[option](t_f_s)

    elif t_f_s == 2:
        for i, option in enumerate(FUTURE_TASKS_OPTIONS, start=1):
            print(f'{i}. {option}')
        choice = int(input())

        if choice == len(FUTURE_TASKS_OPTIONS):
            # 'go back' option should be the last option in FUTURE_TASKS_OPTIONS
            main_options()
        elif choice in [1,2,3]:
            for option in SWITCH:
                if option == choice:
                    SWITCH[option](t_f_s)
        elif choice == 4: future_to_daily()


    elif t_f_s == 3:
        for i, option in enumerate(SCHEDULE_OPTIONS, start=1):
            print(f'{i}. {option}')
        choice = int(input())

        if choice == len(SCHEDULE_OPTIONS):
            # 'go back' option should be the last option in SCHEDULE_OPTIONS
            main_options()
        elif choice in [1,2,3]:
            for option in SWITCH:
                if option == choice:
                    SWITCH[option](t_f_s)
        elif choice == 4: show_timetable()
        elif choice == 5: edit_timetable()


def see_info(option):

    print()
    if option == 1:
        print(f' -- Here is your to-do list for {(datetime.now().date()).strftime('%d.%m.%y')} -- ')
        try:
            with open('tasksFile.txt', 'r', encoding='utf-8') as file:
                for i, line in enumerate(file, start=1):
                    print(f'{i}. {line.strip()}')
        except FileNotFoundError:
            print('Your to-do list is empty. To see the to-do list add the first task.')

    elif option == 2:
        print(f' -- Here is the list of your future tasks -- ')
        try:
            with open('futureTasksFile.txt', 'r', encoding='utf-8') as file:
                for i, line in enumerate(file, start=1):
                    print(f'{i}. {line.strip()}')
        except FileNotFoundError:
            print('Your list is empty. To see the list add the first future task.')

    elif option == 3:
        print(' -- Here is the list of your upcoming events -- ')
        try:
            with open('eventsFile.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    pretty_printing('e', line.split('-'))
            pprint.pprint(sorted(EVENTS, key=itemgetter('date'), reverse=False), width=30, depth=None)
        except FileNotFoundError:
            print('Your list of upcoming events is empty. To see the list add the first event.')

    go_back(option)


def add_info(option):

    print()
    if option == 1:
        print(' * What task do you want to add? * ')
        task_to_add = input()
        with open('tasksFile.txt', 'a') as file:
            file.write(task_to_add + '\n')
        print(' * Your task has been added successfully * ')
    
    elif option == 2:
        print(' * What future task do you want to add? * ')
        task_to_add = input()
        with open('futureTasksFile.txt', 'a') as file:
            file.write(task_to_add + '\n')
        print(' * Your future task has been added successfully * ')

    elif option == 3:
        print(' * What event do you want to add? * ')
        print(' * Format: name-date-time-place * ')
        event_to_add = input()
        with open('eventsFile.txt', 'a') as file:
            file.write(event_to_add + '\n')
        print(' * Your event has been added successfully * ')

    elif option == 4:
        print(' * What event do you want to add? * ')
        print(' * Format: day-hour-name * ')
        event_to_add = input()
        with open('calendarFile.txt', 'a') as file:
            file.write(event_to_add + '\n')
        print(' * Your event has been added successfully * ')
        edit_timetable

    show_options(option)


def remove_info(option):

    if option == 1:
        print(' * Which tasks do you want to remove? * ')
        # user should only write nums of the tasks they want to remove
        tasks_to_remove = sorted((input()).split(' '))
        # this is an array with sorted nums of the tasks to remove

        with open('tasksFile.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        i = 1
        while tasks_to_remove:
            del lines[int(tasks_to_remove[0]) - i]
            tasks_to_remove.pop(0)
            i += 1

        with open('tasksFile.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)

        print(' * Your tasks have been removed successfully * ')

    elif option == 2:
        print(' * Which future tasks do you want to remove? * ')
        # user should only write nums of the tasks they want to remove
        tasks_to_remove = sorted((input()).split(' '))
        # this is an array with sorted nums of the tasks to remove

        with open('futureTasksFile.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        i = 1
        while tasks_to_remove:
            del lines[int(tasks_to_remove[0]) - i]
            tasks_to_remove.pop(0)
            i += 1

        with open('futureTasksFile.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)

        print(' * Your future tasks have been removed successfully * ')


    elif option == 3:
        print(' * Which event do you want to remove? * ')
        event_to_remove = int(input())

        with open('eventsFile.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        del lines[event_to_remove - 1]
        with open('eventsFile.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)

        print(' * Your event has been removed successfully * ')

    elif option == 4:
        print(' * Which event do you want to remove? * ')
        print(' * Format: day-hour-name * ')
        event_to_remove = input()

        with open('calendarFile.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open('calendarFile.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                if line.strip() != event_to_remove:
                    file.write(line)

        print(' * Your event has been removed successfully * ')
        option = 2

    show_options(option)


def future_to_daily():
    
    print()
    print(' * Which future tasks do you want to move to daily tasks file? * ')
    # user should only write nums of the tasks they want to remove
    tasks_to_move = sorted((input()).split(' '))
    # this is an array with sorted nums of the tasks to remove

    with open('futureTasksFile.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 1
    while tasks_to_move:

        with open('tasksFile.txt', 'a') as file:
            file.write(lines[int(tasks_to_move[0]) - i])
        
        del lines[int(tasks_to_move[0]) - i]
        tasks_to_move.pop(0)
        i += 1

    with open('futureTasksFile.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)

    print(' * Your future tasks have been moved successfully * ')
    show_options(2)


def show_timetable():

    print()
    print(' -- Here is the timetable for this week -- ')
    try:
        with open('calendarFile.txt', 'r', encoding='utf-8') as file:
            for line in file:
                pretty_printing('t', line.split('-'))
    except FileNotFoundError:
        print('Your timetable is empty. To see the timetable add the first event.')

    for day, events in CALENDAR.items():
        CALENDAR[day] = sorted(events, key=lambda hour: list(hour))

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        print(day.upper())
        for event in CALENDAR[day][1:]:
            print(f'-> {event}')

    go_back(2)


def edit_timetable():

    print()
    print(' -- Do you want to add or remove the event in the timetable? -- ')
    print('1. Add the event\n2. Remove the event\n3. Go back')
    choice = int(input())

    if choice == 1:
        add_info(4)

    elif choice == 2:
        remove_info(4)

    elif choice == 3:
        show_options(2)


def go_back(option):

    print()
    back = input('--> Press ENTER to go back ')
    if back == '':
        show_options(option)


def pretty_printing(letter, line):

    if letter == 'e':
        # 'e' like 'event'
        EVENT = {
            'name': line[0],
            'date': str(datetime.strptime(line[1], '%d.%m.%y').date()),
            'time': line[2],
            'place': line[3].strip()
        }

        if EVENT not in EVENTS:
            EVENTS.append(EVENT)

    elif letter == 't':
        # 't' like 'timetable'
        day = line[0]
        TIMETABLE = {
            f'{line[1]}': str(line[2].strip())
        }

        if TIMETABLE not in CALENDAR[day]:
            CALENDAR[day].append(TIMETABLE)


""" modules common for every main option  """
SWITCH = \
{
    1: see_info,
    2: add_info,
    3: remove_info
}

EVENTS = []

CALENDAR = \
{
    'Monday': [''],
    'Tuesday': [''],
    'Wednesday': [''],
    'Thursday': [''],
    'Friday': ['']
}

main_options()
