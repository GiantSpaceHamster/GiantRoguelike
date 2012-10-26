from core import *
from utils import *

from data import *

import sys
import pygame

# 파이 게임을 초기화 한다.
pygame.init()

window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Roguelike")
screen = pygame.display.get_surface()

# ResourceManager의 파일들을 갱신해 두자.
ResourceManager.Get().LoadAndReflushImage(pygame.image.load)
 
def KeyInput(events): 
   for event in events: 
      if event.type == pygame.QUIT: 
         sys.exit(0)
      else:
         #print(event)
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               """ 왼쪽으로 이동 """
               MoveCharacter(player, fieldMap, row, col, "LEFT")
               
            elif event.key == pygame.K_RIGHT:
               """ 오른쪽으로 이동 """
               MoveCharacter(player, fieldMap, row, col, "RIGHT")
               
            elif event.key == pygame.K_UP:
               """ 위로 이동 """
               MoveCharacter(player, fieldMap, row, col, "UP")
               
            elif event.key == pygame.K_DOWN:
               """ 아래로 이동 """
               MoveCharacter(player, fieldMap, row, col, "DOWN")
            
while True:
   # 가장 먼저 플레이어가 행동 하고,
   KeyInput(pygame.event.get())

   # 그 뒤에 Nonplayer 들이 행동을 한다.
   #

   # 모든 사이클이 끝났다면, 이제 장면을 렌더링.

   #
   screen.fill((0, 0, 0))

   # 장면 렌더링.
   for i in range(3):
      for x in range(row):
         for y in range(col):
            image = ResourceManager.Get().GetLoadedResource(fieldMap[i][x][y].GetProperty("ResourceID"))
            if image is not None:
               screen.blit(image, (x * 50, y * 50))

   #playerImg = ResourceManager.Get().GetLoadedResource(player.GetProperty("ResourceID"))
   #if playerImg is not None:
    #  screen.blit(playerImg, (player.GetX() * 50, player.GetY() * 50))

   pygame.display.flip()
