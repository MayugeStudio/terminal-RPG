MENU   = 'menu'
GAME   = 'game'

scene = MENU

while True:
    if scene == MENU:
        print("----------------------------------------")
        print('1: Play game')
        print('2: Quit game')
        print("----------------------------------------")
        choice = input('>> ')
        if choice == '1':
            print('What is your name?')
            name = input('>> ')
            scene = GAME
        else:
            exit()

    elif scene == GAME:
        print("----------------------------------------")
        print('1: Walk')
        print('2: Save and quit game')
        print('3: Stay here')
        print("----------------------------------------")
        choice = input('>> ')
        if choice == '1':
            pass
        elif choice == '2':
            exit()
        elif choice == '3':
            pass
