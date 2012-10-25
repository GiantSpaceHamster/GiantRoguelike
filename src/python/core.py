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
