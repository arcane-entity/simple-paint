import sys
import pygame
import pygame as pygame
from pygame.locals import *
from skeleton import BoardBlitter, Constants, GameConstants, Buttons, BaseMaker, ButtonCreator
from gameloop import EventHandler





pygame.init()

def main():
    
    """ddefines constants"""
    constant=Constants()
    game_const=GameConstants()
    button=Buttons()
    """starting values"""
    drawcolor=(0,0,0,255)
    thickness=1
    """inits board"""
    BaseMaker(constant,game_const)
    ButtonCreator(button)
    BoardBlitter(constant,game_const,button, drawcolor, thickness)
    """gameloop"""
    EventHandler(constant,game_const,button, thickness, drawcolor)


    pygame.display.update()

    
main()

  


