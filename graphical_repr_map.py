import sys
import pygame
import tkinter.messagebox

from time import sleep
from findit import Player, mappa, find_gen

# Definisci i colori
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Definisci le dimensioni del quadrato
SQUARE_SIZE = 20

def draw_grid(screen, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            color = RED if grid[i][j] == 1 else WHITE if grid[i][j] == 0 else GREEN if grid[i][j] == 9 else BLUE
            pygame.draw.rect(screen, color, (j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    from findit import mappa

    pygame.init()
    screen = pygame.display.set_mode((len(mappa[0]) * SQUARE_SIZE, len(mappa) * SQUARE_SIZE))
    pygame.display.set_caption("Rappresentazione della lista")

    clock = pygame.time.Clock()
    start = (0,1)
    p = Player(mappa, layer_index=start[0], index=start[1])
    target = 9
    directions = [ p.move_up, p.move_down, p.move_left, p.move_right ]
    moves : list[tuple[int,int]] = []
    searching = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        draw_grid(screen, mappa)
        pygame.display.flip()
        if searching:
            cross = [ x[1] for x in p.get_surroundings() ]
            if target in cross:
                direction = cross.index(target)
                directions[direction]()
                tkinter.messagebox.showinfo("EVVAI", "Ho trovato l'obiettivo")
                searching = False
            else:
                try:
                    direction = cross.index(0)
                except ValueError:
                    tkinter.messagebox.showinfo("AIUTO", "Mi sono cacato")
                    searching = False
                    continue
                move = directions[direction]
                coords = p.index, p.layer_index
                next_coords = p.calculate_coords(move)
                #if verbose: pprint(f"Coords:{coords} NextCoords:{next_coords} Cross:{cross} Moves:{moves}")
                if next_coords in moves:
                    try:
                        direction = cross.index(0, direction+1)
                    except ValueError:
                        tkinter.messagebox.showinfo("AIUTO", "Mi sono cacato")
                        searching = False
                        continue

            move = directions[direction]
            coords = p.index, p.layer_index
            moves.append(coords)
            move()



        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
