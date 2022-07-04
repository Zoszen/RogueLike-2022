from typing import Tuple
from xmlrpc.server import DocXMLRPCRequestHandler



class Entity:
    def __init__(self, x:int, y:int, char: str, colour:tuple[int,int,int]):
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
#Moves entity by x , y. dx = directionX