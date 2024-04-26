import sys
import pygame
import tkinter.messagebox

from time import sleep
from player import Player
from mappa import mappa_big as mappa

mappaReversed :list[list] = mappa[::]
mappaReversed.reverse()
mappaReversed[-1][0]=0
for index, layer in enumerate(mappaReversed):
    if 9 in mappa[index]:
        mappa[index][mappa[index].index(9)] = 0
    mappa[index] += layer

for layer in mappa:
    layer.append(1)

mappa[0][-2] = 9

# Definisci i colori
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Definisci le dimensioni del quadrato
SQUARE_SIZE = 5

def draw_grid(screen, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            color = RED if grid[i][j] == 1 else WHITE if grid[i][j] == 0 else GREEN if grid[i][j] == 9 else BLUE
            pygame.draw.rect(screen, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((len(mappa[0]) * SQUARE_SIZE, len(mappa) * SQUARE_SIZE))
    pygame.display.set_caption("Rappresentazione della lista")
    clock = pygame.time.Clock()

    player = Player(mappa=mappa, coords=(0,0), target=9, when_target_found_place_at_start=True)
    running = True
    moves = []
    mc = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(screen, mappa)
        pygame.display.flip()
        nm = player.nextMove()

        if not(nm is None) and not(player.target_found):
            nm()

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
