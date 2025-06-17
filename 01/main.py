MENU   = 'menu'
GAME   = 'game'

scene = MENU

if scene == MENU:
    print("----------------------------------------")
    print('1: play game')
    print('2: quit game')
    print("----------------------------------------")
    input('#')

elif scene == GAME:
    print("----------------------------------------")
    print('1: walk')
    print('2: run')
    print('3: save game')
    print("----------------------------------------")
    input('#')

