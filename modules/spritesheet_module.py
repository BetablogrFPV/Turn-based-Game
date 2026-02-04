import pygame

def get_tile(image_path, pos_x, pos_y, size_x, size_y):
    """
    Schneidet ein Rechteck (Tile) aus einem PNG aus und gibt das Surface zurück.

    :param image_path: Pfad zur PNG-Datei
    :param pos_x: X-Koordinate oben links im Originalbild
    :param pos_y: Y-Koordinate oben links im Originalbild
    :param size_x: Breite des Tiles
    :param size_y: Höhe des Tiles
    :return: Surface des Tiles
    """
    pos_x *= 16
    pos_y *= 16
    size_x *= 16
    size_y *= 16

    image = pygame.image.load(image_path).convert_alpha()
    orig_w, orig_h = image.get_size()

    if pos_x < 0 or pos_y < 0:
        raise ValueError("pos_x und pos_y müssen >= 0 sein")
    if pos_x >= orig_w or pos_y >= orig_h:
        raise ValueError("pos_x oder pos_y liegen außerhalb des Bildes")

    size_x = min(size_x, orig_w - pos_x)
    size_y = min(size_y, orig_h - pos_y)

    rect = pygame.Rect(pos_x, pos_y, size_x, size_y)

    tile_surf = image.subsurface(rect).copy()

    return tile_surf
