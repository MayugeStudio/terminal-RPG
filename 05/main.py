MENU   = 'menu'
GAME   = 'game'

scene = MENU

mapping = ['village', 'mountain', 'hills', 'fields', 'mountain', 'mayor', 'hills', 'fields', 'cave']
pos = 0

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
        tile = mapping[pos]
        print("----------------------------------------")
        print(f"Tile: {tile}")
        print("----------------------------------------")
        print('1: Walk')
        print('2: Run')
        print('3: Save and quit game')
        print('4: Stay here')
        print("----------------------------------------")
        choice = input('>> ')
        if choice == '1':
            pos += 1
        elif choice == '2':
            
        elif choice == '3':
            exit()
        else:
            pass
