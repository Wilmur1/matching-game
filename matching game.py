import pygame
import sys
screen = pygame.display.set_mode((1520,780))
pygame.display.set_caption("matching")

candy = pygame.image.load("matching game/images/candy.jpg")
ludo = pygame.image.load("matching game/images/ludo.png")
subwaysurfers = pygame.image.load("matching game/images/ssurfers.png")
temple = pygame.image.load("matching game/images/temple.png")

candy_rect = pygame.Rect(50,10,90,90)
ludo_rect = pygame.Rect(50,10,90,90)
subwaysurfers_rect = pygame.Rect(50,10,90,90)
temple_run_rect = pygame.Rect(50,10,90,90)

pygame.font.init()
font = pygame.font.SysFont("Arial",50)
text1 = font.render("subwaysurfers",True, "white")
text2 = font.render("templerun",True, "white")
text3 = font.render("ludo",True, "white")
text4 = font.render("candycrush",True, "white")



def draw():
     pygame.draw.rect(screen,"white",candy_rect)
     screen.blit(candy,(50,10))
     screen.blit(ludo,(50,210))
     screen.blit(subwaysurfers,(50,410))
     screen.blit(temple,(50,610))
     screen.blit(text1,(1150,10))
     screen.blit(text2,(1150,210))
     screen.blit(text3,(1150,410))
     screen.blit(text4,(1150,610))





while True:
     draw()
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
               start = pygame.mouse.get_pos()
               pygame.draw.circle(screen,"white",start,5)
          if event.type == pygame.MOUSEBUTTONUP:
               end = pygame.mouse.get_pos()
               pygame.draw.circle(screen,"white",end,5)
               pygame.draw.line(screen,"white",start,end,3)
     pygame.display.update()