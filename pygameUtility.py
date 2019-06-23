import pygame

class PygameUtility:

    def __init__(self, fps, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()

        # Display parameters
        self.display_height = width
        self.display_width = height
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))
        self.fps = fps

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (200, 0, 0)
        self.bright_red = (255, 0, 0)
        self.green = (0, 200, 0)
        self.bright_green = (0, 255, 0)
        self.blue = (0, 0, 200)
        self.bright_blue = (0, 0, 255)

    def event_update(self):
        self.game_display.fill(self.white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def quit(self):
        pygame.quit()

    def sprite_update(self, sprite_group):
        sprite_group.draw(self.game_display)

    def display_update(self):
        pygame.display.flip()
        self.clock.tick(self.fps)

    def text_objects(self, text, font):
        text_surface = font.render(text, True, self.black)
        return text_surface, text_surface.get_rect()

    def fill_background(self, color):
        self.game_display.fill(color)

    def draw_line(self, start, end, width):
        pygame.draw.line(self.game_display, self.black, start, end, width)

    def draw_circle(self, position, radius, border):
        pygame.draw.circle(self.game_display, self.black, position, radius, border)

    def draw_button(self, msg, x, y, width, height, a_color, i_color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(self.game_display, a_color, (x, y, width, height))
            if click[0] == 1 and action is not None:
                action()

        else:
            pygame.draw.rect(self.game_display, i_color, (x, y, width, height))

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = self.text_objects(msg, small_text)
        text_rect.center = ((x + (width/2)), (y + (height/2)))
        self.game_display.blit(text_surf, text_rect)

    def update_point_counter(self, count):
        font = pygame.font.SysFont(None, 50)
        text = font.render("Points: " + str(count), True, self.green)
        pygame.draw.rect(self.game_display, self.white, (30, 30, 330, 30), 0)
        self.game_display.blit(text, (30, 30))