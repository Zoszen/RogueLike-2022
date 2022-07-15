import numpy as np
import scipy.signal
from tcod.console import Console
import random
import tile_types

map_width = 80
map_height = 45
class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.thick_tree, order="F")
        for x in range(width):
            for y in range(height):
                if random.random() < 0.5:
                    self.tiles[x][y] = tile_types.floor


        for x in range(width):
            for y in range(height):
             N = [
                 [1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1],
             ]

             neighboring_walls = scipy.signal.convolve2d(self.tiles != tile_types.floor, N, mode='same')
             

             
             walls_to_floors = (self.tiles != tile_types.floor) & (neighboring_walls <= 3)
             floors_to_walls = (self.tiles == tile_types.floor) & (neighboring_walls >= 5)
             
             self.tiles[walls_to_floors] = tile_types.floor
             self.tiles[floors_to_walls] = tile_types.thick_tree
           
             
               








 
 #attempt 1   def __init__(self, width: int, height: int):
 #       tree_count = 0
  #      self.width = width
  #      self.height = height
  #      for x in range(width):
  #          for y in range(height):
  #             neighbours = [self.width-1, self.width, self.width+1, self.height-1, self.height, self.height+1,]
  #             for thick_tree in neighbours:
  #              tree_count + 1
  #              if tree_count > 5:
  #                  self.tiles[x][y] = tile_types.thick_tree
  #              else:
  #                  self.tiles[x][y] = tile_types.floor



                
                
    def in_bounds(self,x:int, y:int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]        