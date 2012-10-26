from core import *
from utils import *

from data import *

# 메인 루프를 돌며, 플레이어의 입력을 기다린다.
while 1:
    # 기본적인 맵을 그린다.
    """
    for layer in fieldMap:
        for row in layer:
            for col in row:
                col.Draw()
            print()
    """
    r = 0
    c = 0

    while 1:
        print('[', end='')
        for i in range(3):
            fieldMap[i][c][r].Draw()
        print(']', end='')

        if r < row - 1:
            r = r + 1
        else:
            print()
            r = 0
            c = c + 1

            if c >= col:
                break

    # 사용자에게 입력을 받는다.
    userCommand = input()

    MovingCommand = ['w', 's', 'a', 'd']
    if not userCommand in MovingCommand:
        continue

    if userCommand == 'w':
        userCommand = "UP"
    if userCommand == 's':
        userCommand = "DOWN"
    if userCommand == 'a':
        userCommand = "LEFT"
    if userCommand == 'd':
        userCommand = "RIGHT"

    MoveCharacter(player, fieldMap, row, col, userCommand)
