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

    def AttachRight(self,  otherMapData):
        maxSize = max( len(self.m_mapData),  len(otherMapData.m_mapData))

        # 2개의 Row 데이터를 같게 만들어 준다.
        for i in range( maxSize - len(self.m_mapData) ):
            self.m_mapData.append( [0 for i in range(len(self.m_mapData[0]) ) ] )

        for i in range( maxSize - len(otherMapData.m_mapData) ):
            otherMapData.m_mapData.append( [0 for i in range(len(otherMapData.m_mapData[0]) ) ] )

        # otherMapData 를 오른쪽에 붙인다.
        for i in range(maxSize):
            self.m_mapData[i].extend(otherMapData.m_mapData[i])

    def AttachLeft(self,  otherMapData):
        maxSize = max( len(self.m_mapData),  len(otherMapData.m_mapData))
        
        # 2개의 Row 데이터를 같게 만들어 준다.
        for i in range( maxSize - len(self.m_mapData) ):
            self.m_mapData.append( [0 for i in range(len(self.m_mapData[0]) ) ] )
        
        for i in range( maxSize - len(otherMapData.m_mapData) ):
            otherMapData.m_mapData.append( [0 for i in range(len(otherMapData.m_mapData[0]) ) ] )
            
        # otherMapData 를 오른쪽에 붙인다.
        for i in range(maxSize):
            temp = otherMapData.m_mapData[i]
            temp.extend(self.m_mapData[i])
            self.m_mapData[i] = temp
        
    def AttachTop(self,  otherMapData):
        pass
        
    def AttachBottom(self,  otherMapData):
        maxSize = max( len(self.m_mapData),  len(otherMapData.m_mapData))

        # 2개의 Row 데이터를 같게 만들어 준다.
        for i in range( maxSize - len(self.m_mapData) ):
            self.m_mapData.append( [0 for i in range(len(self.m_mapData[0]) ) ] )

        for i in range( maxSize - len(otherMapData.m_mapData) ):
            otherMapData.m_mapData.append( [0 for i in range(len(otherMapData.m_mapData[0]) ) ] )

        # otherMapData 를 오른쪽에 붙인다.
        for i in range(maxSize):
            self.m_mapData[i].extend(otherMapData.m_mapData[i])
        
    def ExtendToSize(self,  x,  y):
        self.ExtendRight(x)
        self.ExtendDown(y)
        
    def FillAllData(self,  value):
        for data in self.m_mapData:
            for i in range(len(data)):
                data[i] = value

    def ExtendUp(self,  val = 1):
        for i in range(val):
            self.m_mapData.insert(0,  [0 for i in range(len(self.m_mapData[0]))])
            self.m_row = self.m_row + 1
        
    def ExtendDown(self, val = 1):
        for i in range(val):
            self.m_mapData.append([0 for i in range(len(self.m_mapData[0]))])
            self.m_row = self.m_row + 1
        
    def ExtendLeft(self, val = 1):
        for i in range(val):
            for colData in self.m_mapData:
                colData.insert(0, 0)

            self.m_col = self.m_col + 1
    
    def ExtendRight(self,  val = 1):
        for i in range(val):
            for colData in self.m_mapData:
                colData.append(0)

            self.m_col = self.m_col + 1

class Room(Graph):
    def __init__(self):
        super().__init__()

class EightDirectionRoom:
    m_identifier = -1
    
    m_posX = -1
    m_posY = -1

    m_roomData = None
    
    m_mapData = None
    m_roomSizeX = -1
    m_roomSizeY = -1
    
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
    
    def __init__(self,  ident):
        self.m_identifier = ident
        self.m_roomData = Room()
        self.m_directionData = [None for i in range(8)]
        
        self.m_mapData = None
        
        self.m_roomSizeX = -1
        self.m_roomSizeY = -1
        
    def GenerateRandomRoomData(self, minRowSize = 3,  minColSize = 3,  maxRowSize = 10,  maxColSize = 10):
        self.m_roomSizeX = randint(minRowSize,  maxRowSize)
        self.m_roomSizeY = randint(minColSize,  maxColSize)
        
        self.m_mapData = MapData()
        self.m_mapData.ExtendToSize(self.m_roomSizeX,  self.m_roomSizeY)
        self.m_mapData.FillAllData(1)
    
    def SetPosition(self,  x,  y):
        self.m_posX = x
        self.m_posY = y
        
    def GetPositionX(self):
        return self.m_posX
        
    def GetPositionY(self):
        return self.m_posY

# RoomGenerator
def MapGenerator(maxRoomNum):
    # 먼저 랜덤으로 방을 만든다. 최소 1개 부터 n개 까지, 이는 설정에 따른다.
    finishWorkedRoom = []

    # TODO: 설정에 따라 방의 갯수는 달라진다. 이를 수정해야 함.
    totalRoomNum = randint(int(maxRoomNum * 0.5),  maxRoomNum)
    
    generatedRoom = [EightDirectionRoom(i) for i in range(totalRoomNum)]
    
    # 생성된 방을 마구 섞고, 다음을 반복 한다.
    shuffle(generatedRoom)
    
    # 먼저 방을 1개 뺀다.
    endRoom = beginRoom = generatedRoom.pop()
    
    # 남은 방이 있다면, endroom을 변경.
    if len(generatedRoom) > 0:
        endRoom = generatedRoom.pop()
        
    # 그리고 마지막 방은 마지막에 추가 한다.
    generatedRoom.append(endRoom)
        
    # 이제 beginRoom 을 시작으로, endRoom 까지의 길을 만들자.
    selectedRoom = beginRoom
    selectedRoom.SetPosition(0,  0)
    selectedRoom.GenerateRandomRoomData()
    
    visitedRoom = { 0 : { 0 : True } }
    while len(generatedRoom) > 0:
        otherRoom = generatedRoom.pop()
        
        #selectedRoom.SetOtherRandomRoom(otherRoom)
        tempVal = [i for i in range(8)]
        shuffle(tempVal)
        
        while len(tempVal):
            dir = tempVal.pop()
            
            if selectedRoom.m_directionData[dir] is None:        
                prevDirection = dir + 4
                if prevDirection > 7:
                    prevDirection = prevDirection - 8
        
                # 현재 선택된 방의 위치를 얻고,
                x = selectedRoom.GetPositionX()
                y = selectedRoom.GetPositionY()
                
                # 선택된 방향의 위치로 전환 한 뒤, 해당 데이터가 있는지 검사한다.
                if dir == 0:
                    y = y + 1
                elif dir == 1:
                    x = x + 1
                    y = y + 1
                elif dir == 2:
                    x = x + 1
                elif dir == 3:
                    x = x + 1
                    y = y - 1
                elif dir == 3:
                    y = y - 1
                elif dir == 4:
                    x = x - 1
                    y = y - 1
                elif dir == 5:
                    x = x - 1
                elif dir == 6:
                    x = x - 1
                    y = y + 1
                    
                xList = visitedRoom.get(x)
                if xList is not None:
                    yList = xList.get(y)
                    
                    if yList is not None:
                        if visitedRoom[x][y] == True:
                            continue
                    else:
                        yList = {y : True }
                else:
                    xList = {x : { y : True } }

                # 서로를 연결 한다.
                selectedRoom.m_directionData[dir] = otherRoom
                otherRoom.m_directionData[prevDirection] = selectedRoom

                # 다른 방의 위치를 설정한다.
                otherRoom.SetPosition(x,  y)

                # 현재방을 꾸미자.
                otherRoom.GenerateRandomRoomData()

                break

        finishWorkedRoom.append(selectedRoom)
        selectedRoom = otherRoom
    
    finishWorkedRoom.append(selectedRoom)
    finishWorkedRoom.append(endRoom)
    
    # 이제 공식적으로 맵은 완성.
    # 이제 잔잔한 방들을 추가하여 좀 더 보기 좋게 꾸미자.

    return finishWorkedRoom
