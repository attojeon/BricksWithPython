#coding:utf-8
# 볼 그리기
# 볼 그리고 움직이기
# 볼 그리고 튕기기
# 패들 그리기
# 패들 튕기기, 패들 키패드에 반응하기 => keydown에서 문제가 생김*** 어떻게 해결할까?결
# 키패드 반응 문제 해결
# updateObject() 함수로 정의

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

# 키보드의 누름상태를 저장하는 리스트
keys = [False, False]

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('벽돌깨기')

def drawball(x, y, r):
	pygame.draw.circle(screen, BLUE, (x, y), r, 0)

def drawpaddle(x, y):
	pygame.draw.rect(screen, RED, (px, py, p_width, p_height))

def updateObject():
	global bx, by, dx, dy, px, py, p_width, p_height 
	bx += dx
	by += dy 
	if bx > width or bx < 0:
		dx = dx * (-1)
	if by > height or by < 0:
		dy = dy * (-1)

	if keys[0] == True:
		px -= 5

	if keys[1] == True:
		px += 5

	if px < 0:
		px = 0
	if px + p_width > 640:
		px = width - p_width

while True:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				keys[0] = True
			elif event.key == K_RIGHT:
				keys[1] = True
				

		if event.type == pygame.KEYUP:
			if event.key == K_LEFT:
				keys[0] = False
			elif event.key == K_RIGHT:
				keys[1] = False
	
	updateObject()
	drawball(bx, by, radius)
	drawpaddle(px, py)
	pygame.display.update()


