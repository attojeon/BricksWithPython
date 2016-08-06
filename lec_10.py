#coding:utf-8
# 볼 그리기
# 볼 그리고 움직이기
# 볼 그리고 튕기기
# 패들 그리기
# 패들 튕기기, 패들 키패드에 반응하기 => keydown에서 문제가 생김*** 어떻게 해결할까?결
# 키패드 반응 문제 해결
# updateObject() 함수로 정의
# 사운드 추가 
# 볼과 패들의 충돌 체크
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


def drawBall(x, y, r):
	pygame.draw.circle(screen, BLUE, (x, y), r, 0)

def drawPaddle(x, y):
	pygame.draw.rect(screen, RED, (px, py, p_width, p_height))

def updateObject():
	global bx, by, dx, dy, px, py, p_width, p_height, p_vel

	bx += dx
	by += dy 
	if bx > width or bx < 0:
		dx = dx * (-1)
		hit.play()
	if by > height or by < 0:
		dy = dy * (-1)
		hit.play()

	if keys[0] == True:
		px -= p_vel

	if keys[1] == True:
		px += p_vel

	if px < 0:
		px = 0
	if px + p_width > 640:
		px = width - p_width


def collideCheck():
	global bx, by, dx, dy, px, py, p_width, p_height, p_vel
	# 충돌 체크 - ball & paddle
	if bx > px and bx < px + p_width and by > py:
		#dx *= -1
		dy *= -1 
		hit.play()


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
	
	updateObject()
	collideCheck()
	drawBricks()
	drawBall(bx, by, radius)
	drawPaddle(px, py)
	pygame.display.update()


