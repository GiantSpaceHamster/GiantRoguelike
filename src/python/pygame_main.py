from core import *
from utils import *

from data import *

import sys
import pygame

# 명령 리스트
orderList = []

def KeyInput(events):
   DoOrder = False
   
   for event in events: 
      if event.type == pygame.QUIT: 
         sys.exit(0)
      else:
         #print(event)
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               """ 왼쪽으로 이동 """
               MoveCharacter(player, fieldMap, row, col, "LEFT")
               DoOrder = True
               
            elif event.key == pygame.K_RIGHT:
               """ 오른쪽으로 이동 """
               MoveCharacter(player, fieldMap, row, col, "RIGHT")
               DoOrder = True
               
            elif event.key == pygame.K_UP:
               """ 위로 이동 """
               MoveCharacter(player, fieldMap, row, col, "UP")
               DoOrder = True
               
            elif event.key == pygame.K_DOWN:
               """ 아래로 이동 """
               MoveCharacter(player, fieldMap, row, col, "DOWN")
               DoOrder = True

            elif event.key == pygame.K_SPACE:
               """ 랜덤으로 이동 """
               global orderList
               orderList = PathFindAndMove(player, fieldMap, 4, 4)
               DoOrder = True

      return DoOrder

def main():
   # 파이 게임을 초기화 한다.
   pygame.init()

   window = pygame.display.set_mode((800, 600)) 
   pygame.display.set_caption("Roguelike")
   screen = pygame.display.get_surface()

   # ResourceManager의 파일들을 갱신해 두자.
   ResourceManager.Get().LoadAndReflushImage(pygame.image.load)

   global orderList

   while True:
      # 가장 먼저 플레이어가 행동 하고,
      if KeyInput(pygame.event.get()) == True:
            # 그 뒤에 Nonplayer 들이 행동을 한다.
            print("Find Path for enemy...")
            enemyOrder = PathFindAndMove(enemy, fieldMap, player.GetX(), player.GetY())
            print(enemyOrder)
            eorder = enemyOrder[1]

            EnemyPos = enemy.GetY() * 10 + enemy.GetX()
            if EnemyPos > eorder:
                  # playerPos 가 order 보다 크다.
                  if EnemyPos - 10 == eorder:
                     MoveCharacter(enemy, fieldMap, row, col, "UP")
                  elif EnemyPos - 1 == eorder:
                     MoveCharacter(enemy, fieldMap, row, col, "LEFT")
            else:
                  # playerPos 가 order 보다 작다.
                  if EnemyPos + 10 == eorder:
                     MoveCharacter(enemy, fieldMap, row, col, "DOWN")
                  elif EnemyPos + 1 == eorder:
                     MoveCharacter(enemy, fieldMap, row, col, "RIGHT")


      # 플레이어 명령 수행
      if len(orderList) > 0:
         #print("Order Size : ", len(orderList))
         order = orderList[0]
         orderList.remove(order)
         playerPos = player.GetY() * 10 + player.GetX()

         if playerPos > order:
            # playerPos 가 order 보다 크다.
            if playerPos - 10 == order:
               MoveCharacter(player, fieldMap, row, col, "UP")
            elif playerPos - 1 == order:
               MoveCharacter(player, fieldMap, row, col, "LEFT")
         else:
            # playerPos 가 order 보다 작다.
            if playerPos + 10 == order:
               MoveCharacter(player, fieldMap, row, col, "DOWN")
            elif playerPos + 1 == order:
               MoveCharacter(player, fieldMap, row, col, "RIGHT")

         # 그 뒤에 Nonplayer 들이 행동을 한다.
         print("Find Path for enemy...")
         enemyOrder = PathFindAndMove(enemy, fieldMap, player.GetX(), player.GetY())
         print(enemyOrder)
         eorder = enemyOrder[1]

         EnemyPos = enemy.GetY() * 10 + enemy.GetX()
         if EnemyPos > eorder:
               # playerPos 가 order 보다 크다.
               if EnemyPos - 10 == eorder:
                  MoveCharacter(enemy, fieldMap, row, col, "UP")
               elif EnemyPos - 1 == eorder:
                  MoveCharacter(enemy, fieldMap, row, col, "LEFT")
         else:
               # playerPos 가 order 보다 작다.
               if EnemyPos + 10 == eorder:
                  MoveCharacter(enemy, fieldMap, row, col, "DOWN")
               elif EnemyPos + 1 == eorder:
                  MoveCharacter(enemy, fieldMap, row, col, "RIGHT")

      # 모든 사이클이 끝났다면, 이제 장면을 렌더링.

      #
      screen.fill((0, 0, 0))

      # 장면 렌더링.
      for i in range(3):
         for x in range(row):
            for y in range(col):
               image = ResourceManager.Get().GetLoadedResource(fieldMap[i][x][y].GetProperty("ResourceID"))
               if image is not None:
                  screen.blit(image, (x * 48, y * 48))

      #playerImg = ResourceManager.Get().GetLoadedResource(player.GetProperty("ResourceID"))
      #if playerImg is not None:
       #  screen.blit(playerImg, (player.GetX() * 48, player.GetY() * 48))

      pygame.display.flip()

if __name__ == "__main__":
    main()
