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
    m_ableExtList = ( "png", "jpg", "bmp" )
    m_resourceMap = {}
    m_loadedResourceMap = {}

    def __init__(self):
        self.Initialize()
    
    def Initialize(self):
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
        if "Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag in self.m_resourceMap:
            print("Has!")
        else:
            print("Warning: ResourceManager doesn't have resource - Tag : " + tag)

    def LoadAndReflushImage(self, loader):
        for path, filename in self.m_resourceMap.items():
            self.m_loadedResourceMap[path] = loader(path + filename[-4:])
                                        

    def GetLoadedResource(self, tag):
        if tag is None:
            return None
        
        if "Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag in self.m_loadedResourceMap:
            return self.m_loadedResourceMap["Resource/" + ProgramInformation.Get().GetDefalutPrefix() + "/" + tag]

        return None


# 맵 생성 함수
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
        
        mapData[0][i][0].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")
        mapData[0][i][y - 1].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")

    for i in range(y):
        mapData[0][0][i] = Wall()
        mapData[0][x - 1][i] = Wall()
        
        mapData[0][0][i].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")
        mapData[0][x - 1][i].SetProperty("ResourceID", "Image/BlockObject/Wall/BreakdisableWall")

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
