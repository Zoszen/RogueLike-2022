import numpy as np
from tcod.console import Console
from random import randrange, random
import tile_types

map_width = 80
map_height = 45
class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.thick_tree, order="F")
        for x in range(width):
            for y in range(height):
                if random.random() < 0.4:
                    self.tiles[x][y] = tile_types.floor

    def do_step():
        tile
        for tile in GameMap:
            if not tile_types.floor:
                neighbours = GameMap.get_neighbours(GameMap)
                if len(neighbours) > 0:
                   prey = neighbours[randrange(len(neighbours))]
                
   
   
    def get_tile(x,y):
        for tile in GameMap:
            if tile.x == x and tile.y == y:
                return tile             

    def get_neighbours(tile,x:int,y:int):
    
        
        neighbours = []
        for y in range(-1,1):
            for x in range(-1,1):
                if tile.x + x < 0 or tile.x + x > map_width-1 or tile.y + y < 0 or tile.y + y > map_height-1:
                    pass
                else:
                    neighbour_tile = GameMap.get_tile(tile.x+x, tile.y+y)
                    if neighbour_tile == tile_types.floor:
                        neighbours.append(neighbour_tile)

                return neighbours
                
        if len(neighbours) > 2:
            tile.tiles[x][y] = tile_types.floor
                

                








 
 #   def __init__(self, width: int, height: int):
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