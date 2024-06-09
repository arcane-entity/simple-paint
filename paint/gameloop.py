import pygame
import sys
from pygame.locals import *
from skeleton import BoardBlitter


def EventHandler(a,b,c, thickness, drawcolor):
    
    fillcolor= a.WHITE
    colors_used=[(0,0,0,255)] 
    bg_colors_used=[(255,255,255,255)]
    sizes_used=[1]
    drawn_lines=0 
    active_drawing = False
    pos = None
    

    pygame.display.update()

    while True:
        pygame.init()

        
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get(): 
            if event.type == QUIT:

                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN: 
                if pygame.mouse.get_pressed():

                    if pygame.Rect.collidepoint(c.SAVE.rect, x, y): 
                    
                        pygame.image.save(b.SUBOARD, "paint_image.jpg")
                        f= open("log.txt", "w") 
                        f.write("Colors used:" + "\n")
                        for i in range(len(colors_used)):
                            f.write(str(colors_used[i]))
                            f.write("\n")
                        f.write("Line sizes used:" + "\n") 
                        for i in range(len(sizes_used)):
                            f.write(str(sizes_used[i]))
                            f.write("\n")
                        f.write("Background colors used:" + "\n")
                        for i in range(len(bg_colors_used)):
                            f.write(str(bg_colors_used[i]))
                            f.write("\n")
                        f.write(f"Number of lines drawn: {drawn_lines}")
                        f.close


                    if pygame.Rect.collidepoint(c.THIN.rect, x, y): 
                        if thickness>0:
                            thickness = thickness - 1
                            BoardBlitter(a,b,c, drawcolor, thickness)
                        if thickness not in sizes_used:
                            sizes_used.append(thickness)

                    if pygame.Rect.collidepoint(c.THICK.rect, x, y):
                        if thickness<500: 
                            thickness = thickness + 1
                            BoardBlitter(a,b,c, drawcolor, thickness)
                        if thickness not in sizes_used:
                            sizes_used.append(thickness)

                    if pygame.Rect.collidepoint(c.NEW.rect, x, y): 
                        b.SCREEN.fill(a.WHITE) 
                        drawcolor= (0,0,0,255)
                        thickness=1
                        BoardBlitter(a,b,c, drawcolor, thickness)
                        
                        pygame.display.update()


                    if pygame.Rect.collidepoint(c.FILL.rect, x, y): 
                        b.SCREEN.fill(drawcolor) 
                        fillcolor= drawcolor
                        if fillcolor not in bg_colors_used:
                            bg_colors_used.append(fillcolor)

                        BoardBlitter(a,b,c, drawcolor, thickness)
                    if pygame.Rect.collidepoint(c.BLACK_LINE.rect, x, y):
                        drawcolor = (0,0,0,255)


                    if pygame.Rect.collidepoint(c.DARK.rect, x, y): 
                        tempcolor = [drawcolor[0], drawcolor[1], drawcolor[2],255]
                        for i in range(3):

                            if tempcolor[i] > 5: 
                                tempcolor[i] = tempcolor[i] - 5
                            
                        BoardBlitter(a,b,c, drawcolor, thickness)
                        if drawcolor not in colors_used:
                            colors_used.append(drawcolor)

                        drawcolor = (tempcolor[0], tempcolor[1], tempcolor[2],255)
                    if pygame.Rect.collidepoint(c.LIGHT.rect, x, y): 
                        tempcolor = [drawcolor[0], drawcolor[1], drawcolor[2],255]
                        for i in range(3):

                            if tempcolor[i] < 251: 
                                tempcolor[i] = tempcolor[i] + 5

                        drawcolor = (tempcolor[0], tempcolor[1], tempcolor[2],255)
                        if drawcolor not in colors_used:
                            colors_used.append(drawcolor)
                    BoardBlitter(a,b,c, drawcolor, thickness)
                
                    if pygame.Rect.collidepoint(c.ERASER.rect, x, y):
                        drawcolor = fillcolor


                    if b.IMG.get_rect().collidepoint(x, y):
                        drawcolor = b.IMG.get_at((x, y)) 
                        BoardBlitter(a,b,c,drawcolor, thickness)
                        if drawcolor not in colors_used:
                            colors_used.append(drawcolor) 

          
            if event.type == MOUSEMOTION: 
           
                if active_drawing==True:
                    mouse_position = pygame.mouse.get_pos()
                    if pos !=None:
                        pygame.draw.line(b.SCREEN, drawcolor, pos, mouse_position, thickness)
                        
                        BoardBlitter(a,b,c, drawcolor, thickness)
                    pos = mouse_position
            if event.type == MOUSEBUTTONUP:
      
                mouse_position = None
                active_drawing = False
                pos = None
                drawn_lines=drawn_lines+1
            if event.type == MOUSEBUTTONDOWN:
                active_drawing = True
