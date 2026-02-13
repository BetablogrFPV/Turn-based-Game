"""
---------- init ----------

b1 = image_button(idle_image: pygame.Surface, pressed_image: pygame.Surface, pos: tuple (x,y), size: tuple (width,height), action: assigned function, timing: string)

b1 = image_button(idle_image_1, pressed_image_1, (100,100), (20,30), test, "on_press")
--> button image gets sized to 20x30px

b1 = image_button(idle_image_1, pressed_image_1, (100,100), (-1,30), test, "on_press")
b1 = image_button(idle_image_1, pressed_image_1, (100,100), (20,-1), test, "on_press")
--> the undefined dimension (width or height) ist automaticly scaled

b1 = image_button(idle_image_1, pressed_image_1, (100,100), (-1,-1), test, "on_press")
--> original size is used

"on_press" --> action is called directly
"on_release" --> action is called on release
"delayed" --> action is called 400ms delayed

---------- usage ----------

update the button in the loop:

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play_button.handle_event(event)

---------- display ----------

draw the button in the loop:

b1.draw(screen)

"""

import pygame

class image_button:
    next_event_id = pygame.USEREVENT + 1
    def __init__(self, idle_image: pygame.Surface, pressed_image: pygame.Surface, pos, size=(-1, -1), action=None, timing="on_press"):

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
        self.timing = timing
        self.pressed = False

        if timing == "delayed":
            self.trigger_event = image_button.next_event_id
            image_button.next_event_id += 1

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

                    if self.action and self.timing == "on_press":
                        self.action()
                    

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.image = self.idle_image
                self.pressed = False
                
                if self.action and self.timing == "on_release":
                    self.action()

                if self.action and self.timing == "delayed":
                    pygame.time.set_timer(self.trigger_event, 400, loops=1)


        elif self.timing == "delayed" and event.type == self.trigger_event:
            self.action()
