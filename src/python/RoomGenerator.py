from data import *
from utils import *

from random import *

class MapData:
    """ 방 생성시에 맵의 크기를 저장하기 위한 임시 맵 데이터. """
    m_row = 1
    m_col = 1
    
    m_mapData = [ [0] ]
    
    def __init__(self):
        self.m_mapData = [ [ 0 ] ]
        
    def ExtendUp(self):
        self.m_mapData.insert(0,  [0 for i in range(len(self.m_mapData[0]))])
        self.m_row = self.m_row + 1
        
    def ExtendDown(self):
        self.m_mapData.append([0 for i in range(len(self.m_mapData[0]))])
        self.m_row = self.m_row + 1
        
    def ExtendLeft(self):
        for colData in self.m_mapData:
            colData.insert(0, 0)

        self.m_col = self.m_col + 1
    
    def ExtendRight(self):
        for colData in self.m_mapData:
            colData.append(0)
        self.m_col = self.m_col + 1

class Room(Graph):
    def __init__(self):
        super().__init__()

class EightDirectionRoom:
    m_roomData = None
    
    """
     WS(7)    S(0)    SE(1)
     
     W  (6)                 E(2)
     
     WN(5)   N(4)    NE(3)
    """
    S = 0
    SE = 1
    E = 2
    NE = 3
    N = 4
    WN = 5
    W = 6
    WS = 7
    
    m_directionData = []
    
    def __init__(self):
        self.m_roomData = Room()
        self.m_directionData = [None for i in range(8)]
        
    def SetOtherRoom(self,  val,  otherRoom):
        if val < 8:
            self.m_directionData[val] = otherRoom
            
            prevDirection = val + 4
            if prevDirection > 7:
                prevDirection = prevDirection - 8
            
            # 서로를 연결 한다.
            otherRoom.m_directionData[prevDirection] = self
        else:
            return
            
    def SetOtherRandomRoom(self,  otherRoom):
        setComplete = False

        tempVal = [i for i in range(8)]
        shuffle(tempVal)
        
        while len(tempVal):
            dir = tempVal.pop()
            
            if self.m_directionData[dir] is None:
                self.m_directionData[dir] = otherRoom
        
                prevDirection = dir + 4
                if prevDirection > 7:
                    prevDirection = prevDirection - 8
        
                # 서로를 연결 한다.
                otherRoom.m_directionData[prevDirection] = self

                setComplete = True

                break

        return setComplete

# RoomGenerator
def MapGenerator(maxRoomNum):
    # 먼저 랜덤으로 방을 만든다. 최소 1개 부터 n개 까지, 이는 설정에 따른다.
    finishWorkedRoom = []

    totalRoomNum = randint(1,  maxRoomNum)
    
    generatedRoom = [EightDirectionRoom() for i in range(totalRoomNum)]
    
    # 생성된 방을 마구 섞고, 다음을 반복 한다.
    shuffle(generatedRoom)
    
    # 먼저 방을 1개 뺀다.
    endRoom = beginRoom = generatedRoom.pop()
    
    # 남은 방이 있다면, endroom을 변경.
    if len(generatedRoom) > 0:
        endRoom = generatedRoom.pop()
        
    # 이제 beginRoom 을 시작으로, endRoom 까지의 길을 만들자.
    selectedRoom = beginRoom
    while len(generatedRoom) > 0:
        otherRoom = generatedRoom.pop()
        selectedRoom.SetOtherRandomRoom(otherRoom)
        
        finishWorkedRoom.append(selectedRoom)
        selectedRoom = otherRoom
    
    # 다 했다면, 마지막으로 selectedRoom and endRoom.
    selectedRoom.SetOtherRandomRoom(endRoom)
    finishWorkedRoom.append(selectedRoom)
    finishWorkedRoom.append(endRoom)
    
    # 이제 공식적으로 맵은 완성.
    # 이제 잔잔한 방들을 추가하여 좀 더 보기 좋게 꾸미자.
    
    
    return finishWorkedRoom
