MENU   = 'menu'
GAME   = 'game'

scene = MENU

if scene == MENU:
    print("----------------------------------------")
    print('1: Play game')
    print('2: Quit game')
    print("----------------------------------------")
    input('#')

elif scene == GAME:
    print("----------------------------------------")
    print('1: Walk')
    print('2: Save and quit game')
    print('3: Stay here')
    print("----------------------------------------")
    input('#')

