#coding:utf-8
# 볼 그리기
# 볼 그리고 움직이기
# 볼 그리고 튕기기
# 패들 그리기
import pygame, sys 
from pygame.locals import *

BLACK 	= (	0, 	0,	0)
WHITE 	= (255,255,255)
RED	   	= (255, 0,	0)
GREEN 	= (	0,255,	0)
BLUE	= (	0, 	0,255)

width = 640
height = 480
radius = 10
bx = width / 2
by = height / 2
dx = 2
dy = 2

px = 0
py = 440
p_width = 80
p_height = 10


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('벽돌깨기')

def drawball(x, y, r):
	pygame.draw.circle(screen, BLUE, (x, y), r, 0)

def drawpaddle(x, y):
	pygame.draw.rect(screen, RED, (px, py, p_width, p_height))

while True:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	bx += dx
	by += dy 
	if bx > width or bx < 0:
		dx = dx * (-1)
	if by > height or by < 0:
		dy = dy * (-1)

	drawball(bx, by, radius)
	drawpaddle(px, py)
	pygame.display.update()


