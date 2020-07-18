from datetime import datetime

def display(message):
    print(message)

def get_initial(name):
    initial = name[0:1].upper()
    return initial

# Imprimir la hora actual
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()