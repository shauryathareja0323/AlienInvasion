import pygame

pygame.font.init()
# Fonts
MAIN_FONT = pygame.font.SysFont("comicsans", 50)
LOGIN_FONT = pygame.font.SysFont("comicsans", 60)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.txt_surface = MAIN_FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = WHITE if self.active else BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    username = self.text
                    self.text = ''
                    self.txt_surface = MAIN_FONT.render(self.text, True, self.color)
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = MAIN_FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, win):
        win.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(win, self.color, self.rect, 2)
