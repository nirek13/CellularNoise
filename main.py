import pygame
import random
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH = 1000
HEIGHT = 1000
GRID_WIDTH = WIDTH
GRID_HEIGHT = HEIGHT
PIXEL_WIDTH = 1
PIXEL_HEIGHT = 1

# Reproduction rate is the number of neighbors a cell needs to reproduce. 
REPRODUCTION_RATE = 3
# Death rate is the number of neighbors a cell needs to die.
DEATH_RATE = 2
# The number of neighbors a cell needs to stay alive.
STAY_ALIVE = [2,3]
# The number of neighbors a cell needs to be born.
BIRTH_RATE = 3


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

class Environment:
    
    def __init__(self, GRID_WIDTH, GRID_HEIGHT):
        self.grid = []
        self.height = GRID_HEIGHT
        self.width = GRID_WIDTH
    
    def create_grid(self):
        self.grid = [[0 for x in range(self.width)] for y in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = Cell(i , j , random.randint(0, 5))
                self.grid[i][j].find_neighbors()

    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].state == 1:
                    pygame.draw.rect(WIN, (0, 0, 0), (j * PIXEL_WIDTH, i * PIXEL_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT))
  
                else:
                    pygame.draw.rect(WIN, (255, 255, 255), (j * PIXEL_WIDTH, i * PIXEL_HEIGHT, PIXEL_WIDTH, PIXEL_HEIGHT))
    
    def get_neighbors(self , x , y):
        
        self.grid[x][y].find_neighbors(9)
        print(self.grid[x][y].neighbors)

    def update_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].update(self.grid)
  




class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.neighbors = []
        self.alive_neighbors = []
        self.dead_neighbors = []
    
    def find_neighbors(self , distance = 1):
        neighbours = []
        for i in range(-distance, distance + 1):

            for j in range(-distance, distance + 1):
                if i == 0 and j == 0:
                    continue
                if self.x + i < 0 or self.y + j < 0 or self.x + i >= GRID_HEIGHT or self.y + j >= GRID_WIDTH:
                    continue
                neighbours.append((self.x + i, self.y + j))
        self.neighbors = neighbours
        
    def find_alive_neighbors(self , grid):
        alive = []
        
        for i in self.neighbors:
            if grid[i[0]][i[1]].state == 1:
                alive.append(grid[i[0]][i[1]])
                self.alive_neighbors.append(grid[i[0]][i[1]])

        return alive

    def find_dead_neighbours(self , grid):
        dead = []
        for i in self.neighbors:
            if grid[i[0]][i[1]].state == 0:
                dead.append(grid[i[0]][i[1]])
                self.dead_neighbors.append(grid[i[0]][i[1]])
        return dead
    
    def update(self , grid):
        self.find_alive_neighbors(grid)
        self.find_dead_neighbours(grid)
    
    
        if self.state == 1:
            if len(self.alive_neighbors) < STAY_ALIVE[0] or len(self.alive_neighbors) > STAY_ALIVE[-1] :
                self.state = 0
            elif len(self.alive_neighbors) in STAY_ALIVE:
                self.state = 1
            
      
        else:
            if len(self.alive_neighbors) >= REPRODUCTION_RATE:
                self.state = 1
            
 

           
   
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WIN.fill(WHITE)
pygame.display.update()
run = True
env = Environment(GRID_WIDTH, GRID_HEIGHT)
env.create_grid()

clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    
    env.create_grid()
    env.draw_grid()

    #env.update_grid()
    print(env.grid[0][0].state)

  
    pygame.display.update() 
    
    
       
