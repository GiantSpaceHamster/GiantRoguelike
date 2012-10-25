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

    destX = player.GetX()
    destY = player.GetY()

    if userCommand == 'w':
        destX = destX - 1

    if userCommand == 's':
        destX = destX + 1

    if userCommand == 'a':
        destY = destY - 1

    if userCommand == 'd':
        destY = destY + 1

    # 해당 위치의 사물과 상호 작용 가능한지 확인
    if fieldMap[0][destX][destY].IsInteractable() is True:
        fieldMap[0][destX][destY].Interaction()
    
    # 위치가 옮겨지는지 확인하고
    if CheckValidMap(fieldMap, destX, destY, row, col) is False:
        print("Can't move!")
    else:
        fieldMap[0][player.GetX()][player.GetY()] = Object()
        player.SetPosition(destX, destY)
        fieldMap[0][destX][destY] = player
