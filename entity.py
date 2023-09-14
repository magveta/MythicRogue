from typing import Tuple

class Entity: 
    # A generic object used to represent players, enemies, items, etc...

    def __init__(self, x:int, y:int, char:str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color


    def move(self, dx:int, dy:int): 
        # Moves the entity to a coordinate

        self.x += dx
        self.y += dy