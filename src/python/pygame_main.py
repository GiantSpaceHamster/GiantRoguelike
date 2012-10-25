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
         print(event)

while True: 
   KeyInput(pygame.event.get())

   # 장면 렌더링.
   for i in range(3):
      for x in range(row):
         for y in range(col):
            image = ResourceManager.Get().GetLoadedResource(fieldMap[i][x][y].GetProperty("ResourceID"))
            if image is not None:
               screen.blit(image, (x * 50, y * 50))

   playerImg = ResourceManager.Get().GetLoadedResource(player.GetProperty("ResourceID"))
   if playerImg is not None:
      screen.blit(playerImg, (player.GetX() * 50, player.GetY() * 50))

   pygame.display.flip()
