import os
import random
from winreg import SaveKey
from pytimedinput import timedInput
from colorama import Fore, init

flash_frequency = 3
score = 0
FIELD_HEIGHT = 16
FIELD_WIDTH = 32
CELLS = [(col, row) for row in range(FIELD_HEIGHT) for col in range(FIELD_WIDTH)]
eaten = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_apple = random.choice(alphabet)

#snake
snake_body = [(5, FIELD_HEIGHT//2), (4, FIELD_HEIGHT//2),(3, FIELD_HEIGHT//2)]
snake_char = {0:'s', 1:'n', 2:'a', 3:'k', 4:'e'}
DIRECTIONS = {'left':(-1, 0), 'right':(1, 0), 'up':(0, -1), 'down':(0, 1)}
direction = DIRECTIONS['right']

init(autoreset = True)


#map
def print_field():
    for cell in CELLS:
        if cell in snake_body:
            cell_index = snake_body.index(cell)
            if cell_index >= 4:
                print(Fore.GREEN + 'e', end = '')
            elif cell_index <4:
                print(Fore.GREEN + snake_char[cell_index], end = '')
        elif cell[0] in (0, FIELD_WIDTH-1) or cell[1] in (0, FIELD_HEIGHT-1):
            print('#', end = '')
        elif cell == apple_pos:
            print(Fore.RED + char_apple, end = '')
        else:
            print(' ', end = '')

        if cell[0] == FIELD_WIDTH-1:
            print('')


#update_snake
def update_snake():
    global eaten 
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]#tuples cannot sum！
    snake_body.insert(0, new_head)
    if( not eaten):
        snake_body.pop(-1)
    eaten = False

def apple_collision():
    global apple_pos, eaten, flash_frequency, score, char_apple
    if apple_pos == snake_body[0]:
        apple_pos = new_place_apple()
        char_apple = random.choice(alphabet)
        flash_frequency += 3
        score += flash_frequency
        eaten = True


def new_place_apple():
    col = random.randint(1,FIELD_WIDTH-2)
    row = random.randint(1,FIELD_HEIGHT-2)
    while (col, row) in snake_body:
            col = random.randint(1,FIELD_WIDTH-2)
            row = random.randint(1,FIELD_HEIGHT-2)
            #guarantee apple in not in snake!
    return (col, row)


apple_pos = (5, 10)
char_apple


while True:
    #CLEAR THE FIELD
    os.system('cls')#clear for windows
    print_field()
    txt,_ = timedInput('get input: ', timeout = (1/flash_frequency))
    match txt:
        case 'w':direction = DIRECTIONS['up']
        case 'a':direction = DIRECTIONS['left']
        case 's':direction = DIRECTIONS['down']
        case 'd':direction = DIRECTIONS['right']
        case 'q':
            os.system('cls')
            break
    update_snake()
    apple_collision()


#CHECK DEATH
    if snake_body[0][0] in (0, FIELD_WIDTH-1) or snake_body[0][1] in (0, FIELD_HEIGHT-1) or snake_body[0] in snake_body[1:]:
        os.system('cls')
        print("You have got {your_score} score!".format(your_score = score))
        break