# Interactable 인터페이스
class Interactable():
    def IsInteractable(self):
        return False

    def Interaction(self):
        pass

# Block 여부를 파악 하는 인터페이스
class CanMoveable():
    def CanMoveThis(self):
        return True

# 더미로 만들 수 있는 그릴 수 있는 오브젝트
class DummyDrawable():
    def Draw(self):
        pass

# 캐릭터를 조작할 수 있는 경우는 Moveable 인터페이스를 상속 받는다.
class Moveable():
    def SetPosition(self, x, y):
        pass

    def GetX():
        pass

    def GetY():
        pass
    
    def MoveUp(self):
        pass

    def MoveDown(self):
        pass

    def MoveLeft(self):
        pass

    def MoveRight(self):
        pass

# 기본 Object 클레스
class Object(Interactable, DummyDrawable, CanMoveable):
    pass

# 기본 2단 레이어 구성.
# 캐릭터 / 물체 등을 표시하는 최 상단 레이어. - 블록 오브젝트
# 아이템 등을 표시하는 중간 레이어. - 아이템 오브젝트
# 바닥 등을 표시하는 바닥 레이어. - 필드 오브젝트

# 기본 Object를 상속받은 FieldObject
class FieldObject(Object):
    def IsInteractable(self):
        return True
    
    pass

# FieldObject 를 상속 받아 만든 Board
class Board(FieldObject):
    def Interaction(self):
        print("나는 보드다!")

    def Draw(self):
        print(" ", end='')

# 기본 Object를 상속받은 ItemObject 객체
class ItemObject(Object):
    def IsInteractable(self):
        return True

    pass

# 기본 Object를 상속받은 BlockObject 객체
class BlockObject(Object):
    def IsInteractable(self):
        return True

    def CanMoveThis(self):
        return False

# BlockObject를 상속 받아 만든 Wall
class Wall(BlockObject):
    def Interaction(self):
        print("나는 벽이다!")

    def Draw(self):
        print("Q", end='')

# Wall 를 상속 받아 만든 BreakableWall
class BreakableWall(Wall):
    def Interaction(self):
        print("나는 부서지는 벽이다!")

    def Draw(self):
        print("w", end='')

# Wall 를 상속 받아 만든 BreakdisableWall
class BreakdisableWall(Wall):
    def Interaction(self):
        print("나는 부서지지 않 벽이다!")

    def Draw(self):
        print("W", end='')

# BlockObject 를 상속 받아 만든 Door
class Door(BlockObject):    
    def Interaction(self):
        print("나는 문이다!")

    def Draw(self):
        print("D", end='')

# CharacterObject를 상속 받아 만든 PlayableCharacter - Moveable이 추가로 상속 됨.
class PlayableCharacter(BlockObject, Moveable):
    m_x = 0
    m_y = 0

    def SetPosition(self, x, y):
        self.m_x = x
        self.m_y = y

    def GetX(self):
        return self.m_x

    def GetY(self):
        return self.m_y
    pass

# PlayableCharacter를 상속 받아 만든 PlayerCharacter
class PlayerCharacter(PlayableCharacter):
    def Interaction(self):
        print("나는 캐릭터이다!")

    def Draw(self):
        print("C", end='')
    
    def MoveUp(self):
        print("will move up!")
        pass

    def MoveDown(self):
        print("will move down!")
        pass

    def MoveLeft(self):
        print("will move left!")
        pass

    def MoveRight(self):
        print("will move right!")
        pass

# PlayableCharacter를 상속 받아 만든 NonPlayerCharacter
class NonPlayerCharacter(PlayableCharacter):
    def Interaction(self):
        print("나는 NPC다!")
        
    def Draw(self):
        print("N", end='')

# PlayableCharacter를 상속 받아 만든 EnemyCharacter
class EnemyCharacter(PlayableCharacter):
    def Interaction(self):
        print("나는 적이다!")

    def Draw(self):
        print("E", end='')

# Resource를 관리할 ResourceManager
# Python으로 구현한 싱글톤.
# Get() 메소드는 ResourceManager를 호출하고, ResourceManager는 호출시 자신의
# 인스턴스를 넘겨 준다.
class ResourceManager():
    """ 싱글톤 디자인 패턴. """
    m_instance = None

    def __call__(self):
        if self.m_instance is None:
            self.m_instance = ResourceManager()
        return self.m_instance

    def Get():
        return ResourceManager()

    """아래부터는 메인 함수 부분."""
    def Initizlie(self):
        pass

    def LoadAllResource(self):
        pass

    def InsertResource(self, tag, data):
        pass

    def GetResource(self, tag):
        pass

# 아래와 같은 맵을 만든다.
#[][][][][][]
#[]        []
#[]        []
#[]        []
#[][][][][][]
#
# 1. 맵 구조 생성은 1층 부분에서 이루어 진다.
# 2. 벽과 같은 구조는 1층을 참고하여 3층에 이루어진다.
# 3. 나머지 아이템들 역시 1층과 3층을 참고하여 각각 생성 된다.
# 4. 마지막으로 캐릭터들이 1층과 3층을 참고하여 3층에 배치가 된다.
# 5. 이때, 각 오브젝트들은 자신의 위치를 안다.
player = PlayerCharacter()
player.SetPosition(2, 2)

"""
fieldMap = [
        [
            [ Wall(), Wall(), Door(), Wall(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Object(), Object(), Object(), Wall() ],
            [ Wall(), Wall(), Wall(), Wall(), Wall() ]
        ]
    ,
        [
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ],
            [ Object(), Object(), Object(), Object(), Object() ]
        ]
    ,
        [
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ],
            [ Board(), Board(), Board(), Board(), Board() ]
        ]
    ]
"""

def GenerateMap(x, y, mapData):
    mapData[0] = list(range(x))
    mapData[1] = list(range(x))
    mapData[2] = list(range(x))
        
    for i in range(x):
        mapData[0][i] = list(range(y))
        mapData[1][i] = list(range(y))
        mapData[2][i] = list(range(y))
        
        for j in range(y):
            mapData[0][i][j] = Object()
            mapData[1][i][j] = Object()
            mapData[2][i][j] = Board()

    """
    외곽에 벽을 설치한다.
    """
    for i in range(x):
        mapData[0][i][0] = Wall()
        mapData[0][i][y - 1] = Wall()

    for j in range(y):
        mapData[0][0][i] = Wall()
        mapData[0][x - 1][i] = Wall()

row = 10
col = 10

fieldMap = [[], [], []]
GenerateMap(row, col, fieldMap)            

fieldMap[0][player.GetX()][player.GetY()] = player
fieldMap[0][4][4] = EnemyCharacter()

def CheckValidMap(x, y, r, w):
    if x < 0 or x > r - 1:
        return False

    if y < 0 or y > w - 1:
        return False

    return fieldMap[2][x][y].CanMoveThis() and fieldMap[0][x][y].CanMoveThis()


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

    print(destX)
    print(destY)

    if userCommand == 'w':
        destX = destX - 1

    if userCommand == 's':
        destX = destX + 1

    if userCommand == 'a':
        destY = destY - 1

    if userCommand == 'd':
        destY = destY + 1

    print(destX)
    print(destY)

    # 해당 위치의 사물과 상호 작용 가능한지 확인
    if fieldMap[0][destX][destY].IsInteractable() is True:
        fieldMap[0][destX][destY].Interaction()
    
    # 위치가 옮겨지는지 확인하고
    if CheckValidMap(destX, destY, row, col) is False:
        print("Can't move!")
    else:
        fieldMap[0][player.GetX()][player.GetY()] = Object()
        player.SetPosition(destX, destY)
        fieldMap[0][destX][destY] = player
