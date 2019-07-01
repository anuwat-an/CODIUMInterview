f = open('todolist.txt', 'r')
chores = f.readlines()
f.close()
print('Current Chores: ')
all_chores = []
for i in range(len(chores)):
    chore = chores[i].strip('\n')
    all_chores.append(chore)
    print(chore)

uinput = input('Enter Chore: ')
while uinput != '':
    if uinput == 'REMOVE':
        rinput = input('Enter Chore to Remove: ')
        if rinput in all_chores:
            all_chores.remove(rinput)
            print('-Chore Removed-')
        else:
            print('-No Chore with That Name-')
    elif uinput not in all_chores:
        all_chores.append(uinput)
        print('-Chore Added-')
        print(all_chores)

    uinput = input('Enter Chore: ')

f = open('todolist.txt', 'w')
print('Current Chores: ')
for chore in all_chores:
    f.write(chore+'\n')
    print(chore)
f.close()
