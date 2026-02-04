import pygame

import pygame

class button_image:
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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                x = event.pos[0] - self.rect.x
                y = event.pos[1] - self.rect.y
                alpha = self.image.get_at((x, y)).a
                if alpha > 0:
                    self.image = self.pressed_image
                    self.pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                x, y = pygame.mouse.get_pos()
                if self.rect.collidepoint((x, y)):
                    rel_x = x - self.rect.x
                    rel_y = y - self.rect.y
                    alpha = self.image.get_at((rel_x, rel_y)).a
                    if alpha > 0 and self.action:
                        self.action()
                self.image = self.idle_image
                self.pressed = False
