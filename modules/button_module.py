import pygame

class button_image:
    def __init__(self, image_path, pos, size=(-1, -1), action=None):
        original_image = pygame.image.load(image_path).convert_alpha()
        orig_w, orig_h = original_image.get_size()

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
            self.image = pygame.transform.scale(original_image, (new_w, new_h))
        else:
            self.image = original_image

        self.rect = self.image.get_rect(topleft=pos)
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                x = event.pos[0] - self.rect.x
                y = event.pos[1] - self.rect.y

                alpha = self.image.get_at((x, y)).a
                if alpha > 0:
                    if self.action:
                        self.action()
