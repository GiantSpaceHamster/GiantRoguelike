from utils import *

from random import *

class MapData:
    """ 방 생성시에 맵의 크기를 저장하기 위한 임시 맵 데이터. """
    m_row = 1
    m_col = 1
    
    m_upSize = 0
    m_downSize = 0
    m_leftSize = 0
    m_rightSize = 0
    
    m_mapData = { 0 : { 0 : None } }
    
    def __init__(self):
        self.m_mapData = { 0 : { 0 : 0 } }
        
        self.m_upSize = 0
        self.m_downSize = 0
        self.m_leftSize = 0
        self.m_rightSize = 0

    def __call__(self):
        print("Data : ",  self.m_mapData)
        
    def __getitem__(self,  index):
        return self.m_mapData[index]

    def PrintMap(self):
        for j in range(self.m_upSize, self.m_downSize - 1, -1):
            for i in range(self.m_leftSize, self.m_rightSize + 1):
                print(self.m_mapData[i][j], end='')
            print("")

    def AttachRight(self,  otherMapData):
        maxSize = max(len(self.m_mapData[0]), len(otherMapData[0]))
        
        # 세로 크기가 다르다면, 맞춰 준다.
        self.ExtendDown(maxSize - len(self.m_mapData[0]))
        otherMapData.ExtendDown(maxSize - len(otherMapData[0]))

        # 맞춰진 데이터는 self를 기준으로 합친다.
        # 먼저, self를 오른쪽의 데이터 크기 만큼 오른쪽으로 확장 한다.
        startPosition = self.m_rightSize + 1
        self.ExtendRight(len(otherMapData.m_mapData))

        # 이제 데이터를 하나하나 옮겨보자.
        otherXList = list(range(otherMapData.m_leftSize, otherMapData.m_rightSize + 1))
        selfXList = list(range(self.m_leftSize, self.m_rightSize + 1))
        
        for i in range(len(otherXList)):
            otherYList = list(range(otherMapData.m_upSize, otherMapData.m_downSize - 1, -1))
            selfYList = list(range(self.m_upSize, self.m_downSize -1, -1))

            for j in range(len(selfYList)):
                self.m_mapData[startPosition][selfYList[j]] = otherMapData.m_mapData[otherXList[i]][otherYList[j]]
            
            startPosition = startPosition + 1

    def AttachLeft(self,  otherMapData):
        maxSize = max(len(self.m_mapData[0]), len(otherMapData[0]))
        
        # 세로 크기가 다르다면, 맞춰 준다.
        self.ExtendDown(maxSize - len(self.m_mapData[0]))
        otherMapData.ExtendDown(maxSize - len(otherMapData[0]))

        # 맞춰진 데이터는 self를 기준으로 합친다.
        # 먼저, self를 오른쪽의 데이터 크기 만큼 오른쪽으로 확장 한다.
        self.ExtendLeft(len(otherMapData.m_mapData))
        startPosition = self.m_leftSize

        # 이제 데이터를 하나하나 옮겨보자.
        otherXList = list(range(otherMapData.m_leftSize, otherMapData.m_rightSize + 1))
        selfXList = list(range(self.m_leftSize, self.m_rightSize + 1))
        
        for i in range(len(otherXList)):
            otherYList = list(range(otherMapData.m_upSize, otherMapData.m_downSize - 1, -1))
            selfYList = list(range(self.m_upSize, self.m_downSize -1, -1))

            for j in range(len(selfYList)):
                self.m_mapData[startPosition][selfYList[j]] = otherMapData.m_mapData[otherXList[i]][otherYList[j]]
            
            startPosition = startPosition + 1
        
    def AttachTop(self,  otherMapData):
        maxSize = max(len(self.m_mapData), len(otherMapData.m_mapData))
        
        # 가로 크기가 다르다면, 맞춰 준다.
        self.ExtendRight(maxSize - len(self.m_mapData))
        otherMapData.ExtendRight(maxSize - len(otherMapData.m_mapData))

        # 맞춰진 데이터는 self를 기준으로 합친다.
        # 먼저, self를 위쪽의 데이터 크기 만큼 위쪽으로 확장 한다.
        startPosition = self.m_upSize + 1
        self.ExtendUp(len(otherMapData.m_mapData[0]))

        # 이제 데이터를 하나하나 옮겨보자.
        otherXList = list(range(otherMapData.m_leftSize, otherMapData.m_rightSize + 1))
        selfXList = list(range(self.m_leftSize, self.m_rightSize + 1))
        
        for i in range(len(otherXList)):
            otherYList = list(range(otherMapData.m_upSize, otherMapData.m_downSize - 1, -1))
            selfYList = list(range(self.m_upSize, self.m_downSize -1, -1))

            for j in range(len(otherYList)):
                self.m_mapData[selfXList[i]][selfYList[j]] = otherMapData.m_mapData[otherXList[i]][otherYList[j]]
        
    def AttachBottom(self, otherMapData):
        maxSize = max(len(self.m_mapData), len(otherMapData.m_mapData))
        
        # 가로 크기가 다르다면, 맞춰 준다.
        self.ExtendRight(maxSize - len(self.m_mapData))
        otherMapData.ExtendRight(maxSize - len(otherMapData.m_mapData))

        # 맞춰진 데이터는 self를 기준으로 합친다.
        # 먼저, self를 아래쪽의 데이터 크기 만큼 위쪽으로 확장 한다.
        startPosition = self.m_downSize - 1
        self.ExtendDown(len(otherMapData.m_mapData[0]))

        # 이제 데이터를 하나하나 옮겨보자.
        otherXList = list(range(otherMapData.m_leftSize, otherMapData.m_rightSize + 1))
        selfXList = list(range(self.m_leftSize, self.m_rightSize + 1))
        
        for i in range(len(otherXList)):
            otherYList = list(range(otherMapData.m_upSize, otherMapData.m_downSize - 1, -1))
            selfYList = list(range(startPosition, self.m_downSize -1, -1))

            for j in range(len(otherYList)):
                self.m_mapData[selfXList[i]][selfYList[j]] = otherMapData.m_mapData[otherXList[i]][otherYList[j]]
        
    def ExtendToSize(self,  x,  y):
        self.ExtendRight(x)
        self.ExtendUp(y)

    def ExtendToReverseSize(self,  x,  y):
        self.ExtendLeft(x)
        self.ExtendDown(y)

    def FillAllCorner(self,  value):
        for i in range(self.m_leftSize, self.m_rightSize + 1):
            self.m_mapData[i][self.m_upSize] = value
            self.m_mapData[i][self.m_downSize] = value
                
        for j in range(self.m_upSize, self.m_downSize - 1, -1):
            self.m_mapData[self.m_leftSize][j] = value
            self.m_mapData[self.m_rightSize][j] = value

    def FillAllData(self,  value):
        for key in self.m_mapData:
            for data in self.m_mapData[key]:
                self.m_mapData[key][data] = value

    def ExtendUp(self,  val = 1):
        for i in range(val):
            #for colData in self.m_mapData:
                #colData.append(0)
                
            for key in self.m_mapData:
                self.m_mapData[key][self.m_upSize + 1] = 0
                
            self.m_upSize = self.m_upSize + 1
    
    def ExtendDown(self, val = 1):
        for i in range(val):
            #for colData in self.m_mapData:
                #colData.insert(0, 0)
                
            for key in self.m_mapData:
                self.m_mapData[key][self.m_downSize - 1] = 0

            self.m_downSize = self.m_downSize - 1
        
    def ExtendLeft(self, val = 1):
        for i in range(val):
            #self.m_mapData.append([0 for i in range(len(self.m_mapData[0]))])
            #self.m_row = self.m_row + 1
            self.m_mapData[self.m_leftSize - 1 ] = dict(self.m_mapData[self.m_leftSize])
            
            for key in self.m_mapData[self.m_leftSize - 1]:
                self.m_mapData[self.m_leftSize - 1][key] = 0
                
            self.m_leftSize = self.m_leftSize - 1
    
    def ExtendRight(self,  val = 1):
        for i in range(val):
            #self.m_mapData.insert(0,  [0 for i in range(len(self.m_mapData[0]))])
            #self.m_row = self.m_row + 1
            self.m_mapData[self.m_rightSize + 1 ] = dict(self.m_mapData[self.m_rightSize])
            
            for key in self.m_mapData[self.m_rightSize + 1]:
                self.m_mapData[self.m_rightSize + 1][key] = 0
                
            self.m_rightSize = self.m_rightSize + 1

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
        self.m_mapData.FillAllCorner(1)
    
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
    
    #visitedRoom = { 0 : { 0 : True } }
    visitedRoom = MapData()
    visitedRoom[0][0] = True
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

                if visitedRoom.m_rightSize < x:
                    visitedRoom.ExtendRight()

                if visitedRoom.m_leftSize > x:
                    visitedRoom.ExtendLeft()

                if visitedRoom.m_upSize < y:
                    visitedRoom.ExtendUp()

                if visitedRoom.m_downSize > y:
                    visitedRoom.ExtendDown()

                if visitedRoom[x][y] == True:
                    continue

                # 서로를 연결 한다.
                weightValue = randint(1,  10)
                selectedRoom.m_directionData[dir] = [otherRoom,  Edge(weightValue)]
                otherRoom.m_directionData[prevDirection] = [selectedRoom,  Edge(weightValue)]
                visitedRoom[x][y] = True

                # 다른 방의 위치를 설정한다.
                otherRoom.SetPosition(x,  y)

                # 현재방을 꾸미자.
                otherRoom.GenerateRandomRoomData()

                break

        finishWorkedRoom.append(selectedRoom)
        selectedRoom = otherRoom
    
    finishWorkedRoom.append(selectedRoom)
    
    # 이제 공식적으로 맵은 완성.
    # 이제 잔잔한 방들을 추가하여 좀 더 보기 좋게 꾸미자.

    return finishWorkedRoom

# GenerateRandomRoom(size)
def GenerateRandomRoom(roomSize):
    madedRoom = MapGenerator(roomSize)
    tempMapData = MapData()

    for room in madedRoom:
        if tempMapData.m_rightSize < room.m_posX:
            tempMapData.ExtendRight()

        if tempMapData.m_leftSize > room.m_posX:
            tempMapData.ExtendLeft()

        if tempMapData.m_upSize < room.m_posY:
            tempMapData.ExtendUp()

        if tempMapData.m_downSize > room.m_posY:
            tempMapData.ExtendDown()
            
        tempMapData[room.m_posX][room.m_posY] = room

    finalResult = MapData()
    
    def AddEdge(data,  result):
        tempEdge = MapData()
        
        if data.m_directionData[0] != None:
            tempEdge.ExtendUp(data.m_directionData[0][1].m_weight - 1)
            
            result.AttachTop(tempEdge)
            
        if data.m_directionData[1] != None:
            tempEdge.ExtendUp(data.m_directionData[1][1].m_weight - 1)
            tempEdge.ExtendRight(data.m_directionData[1][1].m_weight - 1)
            
            result.AttachRight(tempEdge)
            
        if data.m_directionData[2] != None:
            tempEdge.ExtendRight(data.m_directionData[2][1].m_weight - 1)
            
            result.AttachRight(tempEdge)
            
        if data.m_directionData[3] != None:
            tempEdge.ExtendRight(data.m_directionData[3][1].m_weight - 1)
            tempEdge.ExtendDown(data.m_directionData[3][1].m_weight - 1)
            
            result.AttachRight(tempEdge)
            
        if data.m_directionData[4] != None:
            tempEdge.ExtendDown(data.m_directionData[4][1].m_weight - 1)
            
            result.AttachBottom(tempEdge)
            
        if data.m_directionData[5] != None:
            tempEdge.ExtendDown(data.m_directionData[5][1].m_weight - 1)
            tempEdge.ExtendLeft(data.m_directionData[5][1].m_weight - 1)
            
            result.AttachLeft(tempEdge)
            
        if data.m_directionData[6] != None:
            tempEdge.ExtendRight(data.m_directionData[6][1].m_weight - 1)

            result.AttachLeft(tempEdge)
            
        if data.m_directionData[7] != None:
            tempEdge.ExtendRight(data.m_directionData[7][1].m_weight - 1)
            tempEdge.ExtendUp(data.m_directionData[7][1].m_weight - 1)

            result.AttachLeft(tempEdge)
    
    for y in range(tempMapData.m_upSize, tempMapData.m_downSize - 1, -1):
        xResult = MapData()
        isFirstMeet = False
        
        for x in range(tempMapData.m_leftSize, tempMapData.m_rightSize + 1):
            if isinstance(tempMapData[x][y], EightDirectionRoom):
                if isFirstMeet == False:
                    xResult = tempMapData[x][y].m_mapData
                    
                    AddEdge(tempMapData[x][y],  xResult)

                    isFirstMeet = True
                    continue
                    
                AddEdge(tempMapData[x][y],  xResult)
                
                if x < 0:
                    xResult.AttachLeft(tempMapData[x][y].m_mapData)
                else:
                    xResult.AttachRight(tempMapData[x][y].m_mapData)

        finalResult.AttachBottom(xResult)
                
    return finalResult
