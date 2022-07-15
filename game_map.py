import numpy as np
import scipy.signal
from tcod.console import Console
import random
import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.thick_tree, order="F")
        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the player has seen before
        for x in range(width):
            for y in range(height):
                if random.random() < 0.5:
                    self.tiles[x][y] = tile_types.floor


        for x in range(width):
            for y in range(height):
                if random.random() < 0.011:
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
                   self.tiles[1:85, 22] = tile_types.thick_tree
                
    def in_bounds(self,x:int, y:int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
         """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """
         console.tiles_rgb[0:self.width, 0:self.height] = np.select(
             condlist=[self.visible, self.explored],
             choicelist=[self.tiles["light"], self.tiles["dark"]],
             default=tile_types.SHROUD
         )