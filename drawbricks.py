#coding:utf-8
# 벽돌 생성하기
# 벽돌 그리기 

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
p_vel = 10
p_width = 80
p_height = 10

bricks_cols = 3
bricks_rows = 7
brickWidth = 75
brickHeight = 20
brickPadding = 10
brickOffsetTop = 30
brickOffsetLeft = 30

# 키보드의 누름상태를 저장하는 리스트
keys = [False, False]

# 벽돌 리스트
bricks = []

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('벽돌깨기')

hit = pygame.mixer.Sound('res/took.wav')
hit.set_volume(0.1)

def bricksInit():
	global bricks_cols, bricks_rows, brickWidth, brickHeight, brickPadding, brickOffsetTop, brickOffsetLeft

	for r in range(bricks_rows):
		for c in range(bricks_cols):
			state = 1
			x = brickOffsetLeft + r*(brickPadding + brickWidth)
			y = brickOffsetTop + c*(brickPadding + brickHeight)
			oneBrick = [x, y, state]
			bricks.append(oneBrick)

	print(bricks)

def drawBricks():
	global bricks_cols, bricks_rows, brickWidth, brickHeight, brickPadding, brickOffsetTop, brickOffsetLeft
	for b in bricks:
		pygame.draw.rect(screen, GREEN, (b[0], b[1],brickWidth, brickHeight))

bricksInit()

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
	
	#updateObject()
	#collideCheck()
	drawBricks()
	#drawBall(bx, by, radius)
	#drawPaddle(px, py)
	pygame.display.update()


