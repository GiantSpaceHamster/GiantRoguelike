# Resource를 관리할 ResourceManager
# Python으로 구현한 싱글톤.
# Get() 메소드는 ResourceManager를 호출하고, ResourceManager는 호출시 자신의
# 인스턴스를 넘겨 준다.
from core import *
from resource import *
from definition import *

import os

# 프로그램의 기본 정보를 저장하는 유틸리티.
# definition 파일을 참조한다.(아직은 definition 소스를 참조)
class SingletonPattern():
    """ 싱글톤 디자인 패턴. """
    @classmethod
    def Get(cls, *arg, **args):
        if not hasattr(cls, "m_instance"):
            cls.m_instance = cls(*arg, **args)
        return cls.m_instance
    """ 아래부터는 메인 함수 부분."""

class ProgramInformation(SingletonPattern):
    m_defPrefix = ""

    def __init__(self):
        self.Initialize()
    
    def Initialize(self):
        self.__LoadDefinitionFile()

    def __LoadDefinitionFile(self):
        global defaultPrefix
        self.m_defPrefix = defaultPrefix

    def GetDefalutPrefix(self):
        return self.m_defPrefix


# 리소스 매니져
class ResourceManager(SingletonPattern):
    """ 싱글톤으로 구현된 리소스 매니져 입니다. """
    
    m_ableExtList = ( "png", "jpg", "bmp" )
    m_resourceMap = {}
    m_loadedResourceMap = {}

    def __init__(self):
        self.Initialize()
    
    def Initialize(self):
        """ 리소스 매니져를 초기화 합니다. """
        # 가능하다면, 초기화 시 모든 리소스를 로드 하게 한다.
        # 가능하다면, 리소스 매니져는 쓰레드로 빼자.(PC 기준)
        self.__LoadAllResource()

    def __StoreData(self, path, fileEntry):
        if fileEntry[-3:] in self.m_ableExtList:
            self.m_resourceMap[path + "/" + fileEntry[:-4]] = fileEntry
        else:
            print("this file has not support extension. : " + fileEntry)
        
    def __LoadAndStoreResource(self, path):
        for fileEntry in os.listdir(path):
            if os.path.isdir(path + "/" + fileEntry) is True:
                self.__LoadAndStoreResource(path + "/" + fileEntry)
            else:
                self.__StoreData(path, fileEntry)

    def __LoadAllResource(self):
        print("Loading Resources....")
        defaultPath = "Resource/" + ProgramInformation.Get().GetDefalutPrefix()

        self.__LoadAndStoreResource(defaultPath)
        print("Load Complete!")

    def InsertResource(self, tag, data):
        pass

    def GetResource(self, tag):
        """ tag 를 이용하여 해당 리소스를 얻어 냅니다. """
        if "Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag in self.m_resourceMap:
            print("Has!")
        else:
            print("Warning: ResourceManager doesn't have resource - Tag : " + tag)

    def LoadAndReflushImage(self, loader):
        """ loader를 이용하여 리소스를 실제로 로드 합니다. loader는 환경에 맞게 구성된 로더 데이터여야 합니다. """
        for path, filename in self.m_resourceMap.items():
            self.m_loadedResourceMap[path] = loader(path + filename[-4:])
                                        

    def GetLoadedResource(self, tag):
        """ 실제로 로드된 tag 데이터를 불러 옵니다. """
        if tag is None:
            return None
        
        if "Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag in self.m_loadedResourceMap:
            return self.m_loadedResourceMap["Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag]

        return None


# 맵 생성 함수
def GenerateMap(x, y):
    """ x, y 로 구성된 맵을 생성 합니다. """

    # Path Finding을 위해, x * y 크기의 노드를 만듭니다.
    mapNode = CreateNodeList(x * y)

    # 만들어진 mapNode 데이터를 토대로, 4방향 격자 그래프를 만듭니다.
    mapGraph = CreateQuadGridGraph(x, y, mapNode)

    # 맵 데이터를 생성 합니다.
    mapData = []

    mapData.append(list(range(x)))
    mapData.append(list(range(x)))
    mapData.append(list(range(x)))
    mapData.append(mapGraph)

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
        
        mapData[0][i][0].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")
        mapData[0][i][y - 1].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")

    for i in range(y):
        mapData[0][0][i] = Wall()
        mapData[0][x - 1][i] = Wall()
        
        mapData[0][0][i].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")
        mapData[0][x - 1][i].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")

    """
    TODO: 위 벽들을 기준으로, 각 그래프의 리스트들의 Edge도 재 조정해야 한다.
    """

    return mapData

# 맵 검사 함수
def CheckValidMap(mapData, x, y, r, w):
    if x < 0 or x > r - 1:
        return False

    if y < 0 or y > w - 1:
        return False

    return mapData[2][x][y].CanMoveThis() and mapData[0][x][y].CanMoveThis()

# 캐릭터 이동 함수
def MoveCharacter(char, mapData, row, col, userCommand):
    destX = char.GetX()
    destY = char.GetY()

    if userCommand == "LEFT":
        destX = destX - 1

    if userCommand == "RIGHT":
        destX = destX + 1

    if userCommand == "UP":
        destY = destY - 1

    if userCommand == "DOWN":
        destY = destY + 1

    # 해당 위치의 사물과 상호 작용 가능한지 확인
    if mapData[0][destX][destY].IsInteractable() is True:
        mapData[0][destX][destY].Interaction()
    
    # 위치가 옮겨지는지 확인하고
    if CheckValidMap(mapData, destX, destY, row, col) is False:
        print("Can't move!")
    else:
        mapData[0][char.GetX()][char.GetY()] = Object()
        char.SetPosition(destX, destY)
        mapData[0][destX][destY] = char

# 노드를 만드는 함수
def CreateNodeList(value):
    """ 필요한 양 만큼의 Node를 만들어 반환 합니다. """
    return [Node(i) for i in range(value)]

# 4각형 그리드의 그래프를 만드는 함
def CreateQuadGridGraph(width, height, nodeData):
    graphList = []
    
    for i in range(len(nodeData)):
        graph = Graph()
        graph.AddNode(nodeData[i])

        graphList.append(graph)

    for i in range(width):
        for j in range(height):
            for count in range(4):
                edge = Edge()
                edge.m_source = i * width + j

                # 왼쪽
                if count == 0:
                    if i > 0:
                        edge.m_destiny = (i - 1) * width + j
                    else:
                        continue
                
                # 위
                if count == 1:
                    if j > 0:
                        edge.m_destiny = i * width + j - 1
                    else:
                        continue
                
                # 오른쪽
                if count == 2:
                    if i < width - 1:
                        edge.m_destiny = (i + 1) * width + j
                    else:
                        continue
                    
                # 아래
                if count == 3:
                    if j < height - 1:
                        edge.m_destiny = i * width + j + 1
                    else:
                        continue

                graphList[i * width + j].AddEdge(edge)

    return graphList

# DFS로 패스를 찾는 함수.
def PathFindForDFS(src, dst, graph):
    """ 코드의 일부는 Programming Game AI by Example(Mat Buckland/사이텍 미디어) 을 참고 했습니다. """
    findPath = False
    routeNode = [-1 for i in range(len(graph))]
    visitedNode = [False for i in range(len(graph))]
    
    tempEdge = Edge()
    tempEdge.m_source = src
    tempEdge.m_destiny = src

    edgeNodeStack = [tempEdge]

    while len(edgeNodeStack):
        nextEdge = edgeNodeStack.pop()
        routeNode[nextEdge.m_destiny] = nextEdge.m_source

        visitedNode[nextEdge.m_destiny] = True

        if nextEdge.m_destiny == dst:
            findPath = True
            break

        # 모든 엣지를 스택에 임시로 저장
        for i in graph[nextEdge.m_destiny].m_edgeList:
            if visitedNode[i.m_destiny] == False:
                # 해당 엣지를 스택에 넣는다.
                edgeNodeStack.append(i)

    findedNode = []

    if findPath is True:
        findedDst = dst
        while True:
            findedNode.insert(0, findedDst)

            if findedDst == src:
                break

            findedDst = routeNode[findedDst]

    return findedNode

# BFS로 패스를 찾는 함수.
def PathFindForBFS(src, dst, graph):
    """ 코드의 일부는 Programming Game AI by Example(Mat Buckland/사이텍 미디어) 을 참고 했습니다. """
    findPath = False
    routeNode = [-1 for i in range(len(graph))]
    visitedNode = [False for i in range(len(graph))]
    
    tempEdge = Edge()
    tempEdge.m_source = src
    tempEdge.m_destiny = src

    edgeNodeStack = [tempEdge]

    while len(edgeNodeStack):
        nextEdge = edgeNodeStack[0]
        edgeNodeStack.remove(nextEdge)

        routeNode[nextEdge.m_destiny] = nextEdge.m_source

        visitedNode[nextEdge.m_destiny] = True

        if nextEdge.m_destiny == dst:
            findPath = True
            break

        # 모든 엣지를 스택에 임시로 저장
        for i in graph[nextEdge.m_destiny].m_edgeList:
            if visitedNode[i.m_destiny] == False:
                # 해당 엣지를 스택에 넣는다.
                edgeNodeStack.append(i)
                visitedNode[i.m_destiny] = True

    findedNode = []

    if findPath is True:
        findedDst = dst
        while True:
            findedNode.insert(0, findedDst)

            if findedDst == src:
                break

            findedDst = routeNode[findedDst]

    return findedNode

# BFS로 패스를 찾고, 해당 패스로 이동 명령을 내리는 함수
def PathFindAndMove(obj, mapData, x, y):
    return PathFindForBFS(obj.GetY() * 10 + obj.GetX(), y * 10 + x, mapData[3])
