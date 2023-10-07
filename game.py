import pygame
import sys
from board import board, BOARD_COLS, SQUARE_SIZE

pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LINE_WIDTH = 15

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

def draw_grid():
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (SCREEN_WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

def draw_X(row, col):
    pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE),
                     (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE, row * SQUARE_SIZE),
                     (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE), LINE_WIDTH)

def draw_O(row, col):
    pygame.draw.circle(screen, LINE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                           row * SQUARE_SIZE + SQUARE_SIZE // 2),
                       SQUARE_SIZE // 2 - 5, LINE_WIDTH)

def play_game():
    player_turn = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = player_turn
                    if player_turn == 'X':
                        player_turn = 'O'
                    else:
                        player_turn = 'X'

                    if player_turn == 'O':
                        draw_O(clicked_row, clicked_col)
                    else:
                        draw_X(clicked_row, clicked_col)

        draw_grid()
        pygame.display.update()
