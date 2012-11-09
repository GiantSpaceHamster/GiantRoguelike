from RoomGenerator import *

import sys
import pygame

# 명령 리스트
orderList = []

def KeyInput(events):
   
   for event in events: 
      if event.type == pygame.QUIT: 
         sys.exit(0)

def main():
   # 파이 게임을 초기화 한다.
   pygame.init()
   
   mapData = MapData()
   generatedRoomList = MapGenerator(5)
   
   curRow = 0
   curCol = 0
   for data in generatedRoomList:
        mapData.m_mapData[curRow][curCol] = 1
        
        direction = 0
        for pos in data.m_directionData:
            if pos is not None:
                
                break
                
            direction = direction + 1
   
   # 생성된 룸 리스트로 이미지를 만들자. 각각 MostLeftRoom / MostRightRoom / MostTopRoom / MostDownRoom

   window = pygame.display.set_mode((800, 600)) 
   pygame.display.set_caption("graphical test")
   screen = pygame.display.get_surface()

   while True:
      # 가장 먼저 플레이어가 행동 하고,
      KeyInput(pygame.event.get())

      pygame.display.flip()

if __name__ == "__main__":
    main()
