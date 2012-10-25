from core import *
from utils import *

from data import *

import sys
import pygame

# 파이 게임을 초기화 한다.
pygame.init()

window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Roguelike") 
 
def KeyInput(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      else: 
         print(event)
 
while True: 
   input(pygame.event.get()) 
