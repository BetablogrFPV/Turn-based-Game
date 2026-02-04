"""
image1 = get_tile(image_path, pos: tuple (x,y), size: tuple (width,height))

--> 1 unit is 16px in the spritesheet
--> the top-left corner is (0|0)

image_1 = get_tile("images/spritesheet.png",(2,1), (1,2))
--> tile with the size 32x16px at the position 16x48px dimensioned at the top-left corner

    [tile arked with X in the following explanation-graphic]
    O O O O O O
    O O X O O O
    O O X O O O
    O O O O O O
    
"""


import pygame

def get_tile(image_path, pos, size):

    pos_x, pos_y = pos
    size_x, size_y = size
    
    pos_x *= 16
    pos_y *= 16
    size_x *= 16
    size_y *= 16

    image = pygame.image.load(image_path).convert_alpha()
    orig_w, orig_h = image.get_size()

    if pos_x < 0 or pos_y < 0:
        raise ValueError("input error")
    if pos_x >= orig_w or pos_y >= orig_h:
        raise ValueError("range error")

    size_x = min(size_x, orig_w - pos_x)
    size_y = min(size_y, orig_h - pos_y)

    rect = pygame.Rect(pos_x, pos_y, size_x, size_y)

    tile_surf = image.subsurface(rect).copy()

    return tile_surf
