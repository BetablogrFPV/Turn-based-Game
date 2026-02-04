"""
b1 = image_button(idle_image: pygame.Surface, pressed_image: pygame.Surface, pos: tuple (x|y), size: tuple (width|height), action: assigned function)

b1 = image_button(idle_image_1, pressed_image_1, (100|100), (20|30), test)
--> button image gets sized to 20x30px

b1 = image_button(idle_image_1, pressed_image_1, (100|100), (-1|30), test)
b1 = image_button(idle_image_1, pressed_image_1, (100|100), (20|-1), test)
--> the undefined dimension (width or height) ist automaticly scaled

b1 = image_button(idle_image_1, pressed_image_1, (100|100), (-1|-1), test)
--> original size is used

"""

import pygame

class image_button:
    def __init__(self, idle_image: pygame.Surface, pressed_image: pygame.Surface, pos, size=(-1, -1), action=None):

        orig_w, orig_h = idle_image.get_size()
        target_w, target_h = size

        if target_w == -1 and target_h == -1:
            new_w, new_h = orig_w, orig_h
        elif target_w == -1:
            scale = target_h / orig_h
            new_w = int(orig_w * scale)
            new_h = target_h
        elif target_h == -1:
            scale = target_w / orig_w
            new_w = target_w
            new_h = int(orig_h * scale)
        else:
            new_w, new_h = target_w, target_h

        if (new_w, new_h) != (orig_w, orig_h):
            self.idle_image = pygame.transform.scale(idle_image, (new_w, new_h))
            self.pressed_image = pygame.transform.scale(pressed_image, (new_w, new_h))
        else:
            self.idle_image = idle_image
            self.pressed_image = pressed_image

        self.image = self.idle_image
        self.rect = self.image.get_rect(topleft=pos)
        self.action = action
        self.pressed = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        # Maus gedrückt
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                x = event.pos[0] - self.rect.x
                y = event.pos[1] - self.rect.y
                alpha = self.image.get_at((x, y)).a
                if alpha > 0:
                    self.image = self.pressed_image
                    self.pressed = True
                    # --- Aktion sofort ausführen ---
                    if self.action:
                        self.action()

        # Maus losgelassen
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.image = self.idle_image
                self.pressed = False