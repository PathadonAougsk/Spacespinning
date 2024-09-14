import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

Cposition = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

c = 0
m = 0
o = 0

class Circle:
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius
    
    def drawCircle(self):
        pygame.draw.circle(screen, self.color, self.position, self.radius) 

    def circularmotion(self, scale, name, disk):
        self.position = pygame.Vector2(name.position.x - 100 * scale * math.cos(disk), name.position.y - 100 * scale * math.sin(disk))
  

sun = Circle(pygame.Color("#D2E0FB"), Cposition, 50)
earth = Circle("blue", pygame.Vector2(Cposition.x + 100, Cposition.y + 100), 20)
k1 = Circle(pygame.Color("#FF885B"), Cposition, 15)
e3 = Circle(pygame.Color("#C7253E"), Cposition, 25)
mar = Circle("red", pygame.Vector2(Cposition.x + 100, Cposition.y + 100), 10)
moon = Circle("white", pygame.Vector2(earth.position.x + 10, earth.position.y + 10), 5)

while running:
    # Respawn 

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #Circular Motion
    earth.circularmotion(2, sun, c)
    mar.circularmotion(1, sun, o)
    k1.circularmotion(1.4, sun, c + (o * 4))
    e3.circularmotion(2.8, sun, c + (o * 2))
    moon.circularmotion(0.4, earth, m)

    c -= 0.01
    o -= 0.002
    m += 0.07

    # RENDER YOUR GAME HERE
    sun.drawCircle()
    earth.drawCircle()
    k1.drawCircle()
    e3.drawCircle()
    mar.drawCircle()
    moon.drawCircle()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
