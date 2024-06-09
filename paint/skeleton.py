import pygame
pygame.init()


class Constants:
    def __init__(self):
        self.SCREENWIDTH = 1080
        self.SCREENHEIGHT = 600
        self.GREY = (191, 191, 189)  

        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.WHITE=(255,255,255)

class GameConstants:
    

    def __init__(self):
        self.SCREEN=None
        self.BOARD = None
        self.SUBOARD = None
        self.FONT = None
        self.USER_FONT= None
        self.MENU = None
        self.IMG = pygame.image.load("colorwheel.png")
        self.IMG = pygame.transform.scale(self.IMG, (100, 100))

class Sprite:
    """the object for storing button data"""
    
    def __init__(self, text,font, x,y):

        self.font=pygame.font.Font(font, 18)
        self.user_font=pygame.font.Font(font, 10)
        self.text=  self.font.render(text, True, (0,0,255), (191,191,191))
        self.user_text=  self.user_font.render(text, True, (0,0,0), (191,191,191))

        self.rect= self.text.get_rect()#itt keszul el e rect ami kattinthato lesz
        self.rect.left=x
        self.rect.top= y
class Buttons:
    def __init__(self):
        self.SAVE=None
        self.THIN= None
        self.THICK=None
        self.NEW=None
        self.FILL=None
        self.BLACK_LINE=None
        self.LIGHT=None
        self.DARK=None


def UserInfo(SCREEN,drawcolor,thickness):
    """updates the infos used by the user"""
    
    info_drawcolor= Sprite(f'Current color: {drawcolor}', 'freesansbold.ttf',0, 400)
    info_thickness= Sprite(f'Current size: {thickness}', 'freesansbold.ttf',0, 430)

    SCREEN.blit(info_drawcolor.user_text, info_drawcolor.rect)
    SCREEN.blit(info_thickness.user_text, info_thickness.rect)

    pygame.display.update()

def BoardBlitter(a,b,c, drawcolor, thickness):
    """bits board whenever neccesary"""
     


    pygame.draw.rect(b.SCREEN, a.GREY, (0, 0, 200, a.SCREENHEIGHT))
    b.SCREEN.blit(c.SAVE.text, c.SAVE.rect)
    b.SCREEN.blit(c.THIN.text, c.THIN.rect)   
    b.SCREEN.blit(c.THICK.text, c.THICK.rect)
    b.SCREEN.blit(c.NEW.text, c.NEW.rect)
    b.SCREEN.blit(c.FILL.text, c.FILL.rect)
    b.SCREEN.blit(c.BLACK_LINE.text, c.BLACK_LINE.rect)
    b.SCREEN.blit(c.DARK.text, c.DARK.rect)
    b.SCREEN.blit(c.LIGHT.text, c.LIGHT.rect)
    b.SCREEN.blit(c.ERASER.text, c.ERASER.rect)
    b.SCREEN.blit(b.IMG,(0,0))
    UserInfo(b.SCREEN, drawcolor, thickness)

def BaseMaker(a,b):
    b.SCREEN=pygame.display.set_mode((a.SCREENWIDTH, a.SCREENHEIGHT))
    b.SCREEN.fill((a.WHITE))
    b.BOARD = pygame.draw.rect(b.SCREEN, a.WHITE, (200, 0, a.SCREENWIDTH, a.SCREENHEIGHT))
    b.SUBOARD = b.SCREEN.subsurface(b.BOARD)
    b.FONT = pygame.font.Font('freesansbold.ttf', 20)
    b.USER_FONT= pygame.font.Font('freesansbold.ttf', 10)
    b.MENU = pygame.draw.rect(b.SCREEN, a.GREY, (0, 0, 200, a.SCREENHEIGHT))

    return b.SCREEN, b.BOARD, b.SUBOARD,b.FONT, b.USER_FONT, b.MENU


def ButtonCreator(c):

    c.SAVE=Sprite('Save', 'freesansbold.ttf',10, 120)
    c.THIN= Sprite('Thinner line', 'freesansbold.ttf', 10, 150)
    c.THICK=Sprite('Thicker line', 'freesansbold.ttf', 10, 180)
    c.NEW=Sprite("New page", 'freesansbold.ttf', 10, 210)
    c.FILL=Sprite("Fill",'freesansbold.ttf', 10, 240 )
    c.BLACK_LINE= Sprite("Reset drawing color", 'freesansbold.ttf', 10, 270)
    c.DARK=Sprite("Darker line", 'freesansbold.ttf', 10, 300)
    c.LIGHT=Sprite("Lighter line", 'freesansbold.ttf', 10, 330)
    c.ERASER=Sprite("Eraser", 'freesansbold.ttf', 10, 360)
    
    return c.SAVE, c.THIN, c.THICK, c.NEW, c.FILL, c.BLACK_LINE, c.DARK, c.ERASER, c.LIGHT

