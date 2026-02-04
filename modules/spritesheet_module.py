import pygame

def get_tile(image_path, pos_x, pos_y, size_x, size_y):
    """
    Schneidet ein Rechteck (Tile) aus einem PNG aus und passt die Größe
    an die minimalen nicht-transparenten Pixel an.

    :param image_path: Pfad zur PNG-Datei
    :param pos_x: X-Koordinate oben links im Originalbild
    :param pos_y: Y-Koordinate oben links im Originalbild
    :param size_x: Breite des Tiles
    :param size_y: Höhe des Tiles
    :return: Surface des Tiles, nur die nicht-transparenten Pixel
    """
    # --- Bild laden ---
    image = pygame.image.load(image_path).convert_alpha()
    orig_w, orig_h = image.get_size()

    # --- Sicherheitscheck ---
    if pos_x < 0 or pos_y < 0:
        raise ValueError("pos_x und pos_y müssen >= 0 sein")
    if pos_x >= orig_w or pos_y >= orig_h:
        raise ValueError("pos_x oder pos_y liegen außerhalb des Bildes")

    size_x = min(size_x, orig_w - pos_x)
    size_y = min(size_y, orig_h - pos_y)

    # --- Rechteck ausschneiden ---
    rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
    tile_surf = image.subsurface(rect).copy()

    # --- Maske erstellen für nicht-transparente Pixel ---
    mask = pygame.mask.from_surface(tile_surf)
    if mask.count() == 0:
        # komplett transparent
        return tile_surf

    # Bounding Rect der nicht-transparenten Pixel
    bounding_rect = mask.get_bounding_rects()[0]  # gibt Liste, wir nehmen den ersten
    final_surf = tile_surf.subsurface(bounding_rect).copy()

    return final_surf
