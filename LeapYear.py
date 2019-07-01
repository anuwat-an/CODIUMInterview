uinput = input()
while uinput != '':
    uinput = int(uinput)
    print(uinput % 400 == 0 or(uinput % 400 != 0 and uinput % 100 != 0 and uinput % 4 == 0))
    uinput = input()
