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
    print('2: Run')
    print('3: Save and quit game')
    print("----------------------------------------")
    input('#')

