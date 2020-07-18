if __name__ == '__main__':
    # print('Cuantas veces quieres ejecutar:')
    N = int(input())
    

    list = []
    
    for iteration in range(N):
        # print('Introduce la opción:')
        action = input()
        # print('Ejecutando: ' + action)
        
        if 'insert' in action:
            list.insert(int(action.split()[1]), int(action.split()[2]))
        elif 'print' in action:
            print(list)
        elif 'remove' in action:
            list.remove(int(action.split()[1]))
        elif 'append' in action:
            list.append(int(action.split()[1]))
        elif 'pop' in action:
            list.pop()
        elif 'sort' in action:
            list.sort()
        elif 'reverse' in action:
            list.reverse()
