#import the necessary modules
import random
import time

#define the board size
board_width = 10
board_height = 10

#initialize the board
board = [[0 for x in range(board_width)] for y in range(board_height)]

#define the paddles
paddle_left = [3,3]
paddle_right = [board_width-3,3]

#define the ball
ball_x = int(board_width/2)
ball_y = int(board_height/2)

#define the ball velocity
vel_x = -1
vel_y = -1

#define the score
score_left = 0
score_right = 0

#define the game loop
while True:
	#clear the board
	for y in range(board_height):
		for x in range(board_width):
			board[y][x] = 0

	#draw the paddles
	board[paddle_left[1]][paddle_left[0]] = 1
	board[paddle_right[1]][paddle_right[0]] = 1

	#draw the ball
	board[ball_y][ball_x] = 2

	#print the board
	for y in range(board_height):
		for x in range(board_width):
			if board[y][x] == 0:
				print(" ", end="")
			elif board[y][x] == 1:
				print("|", end="")
			else:
				print("o", end="")
		print("")

	#update the ball position
	ball_x += vel_x
	ball_y += vel_y

	#check for collision with paddles
	if ball_x == paddle_left[0] and ball_y in range(paddle_left[1]-2, paddle_left[1]+2):
		vel_x = -vel_x
		vel_y = random.randint(-1,1)
	elif ball_x == paddle_right[0] and ball_y in range(paddle_right[1]-2, paddle_right[1]+2):
		vel_x = -vel_x
		vel_y = random.randint(-1,1)

	#check for collision with walls
	if ball_y == 0 or ball_y == board_height-1:
		vel_y = -vel_y
	elif ball_x == 0:
		score_right += 1
		ball_x = board_width/2
		ball_y = board_height/2
		vel_x = -vel_x
		vel_y = -vel_y
	elif ball_x == board_width-1:
		score_left += 1
		ball_x = board_width/2
		ball_y = board_height/2
		vel_x = -vel_x
		vel_y = -vel_y

	#print the score
	print("Score: Left %d | Right %d" % (score_left, score_right))

	#wait for a bit
	time.sleep(0.1)