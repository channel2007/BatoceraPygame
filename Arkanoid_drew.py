class Box(object):
    def __init__( self, pygame, canvas, name, rect, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.rect = rect
        self.color = color

        self.visivle = True
        
    def update(self):
        if(self.visivle):
            self.pygame.draw.rect( self.canvas, self.color, self.rect)

class Circle(object):
    def __init__( self, pygame, canvas, name, pos, radius, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.pos = pos
        self.radius = radius
        self.color = color
        
        self.visivle = True

    def update(self):
        if(self.visivle):
            self.pygame.draw.circle( self.canvas, self.color, self.pos , self.radius)
