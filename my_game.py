import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Rushabh Game 2.0")
clock = pygame.time.Clock()

#character moving images
walkRight = [pygame.image.load(r"Game\R1.png"), pygame.image.load(r"Game\R2.png"), pygame.image.load(r"Game\R3.png"),
            pygame.image.load(r"Game\R4.png"), pygame.image.load(r"Game\R5.png"), pygame.image.load(r"Game\R6.png"),
            pygame.image.load(r"Game\R7.png"), pygame.image.load(r"Game\R8.png"), pygame.image.load(r"Game\R9.png")]

walkLeft = [pygame.image.load(r"Game\L1.png"), pygame.image.load(r"Game\L2.png"), pygame.image.load(r"Game\L3.png"),
            pygame.image.load(r"Game\L4.png"), pygame.image.load(r"Game\L5.png"), pygame.image.load(r"Game\L6.png"),
            pygame.image.load(r"Game\L7.png"), pygame.image.load(r"Game\L8.png"), pygame.image.load(r"Game\L9.png")]

#background image
bg = pygame.image.load(r"C:\Users\rushi\.spyder-py3\PyGame_Images\Game\bg.jpg")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x=300, y=410, width=64, height=64):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.jumpCount = 10
        self.hitbox = (self.x+17, self.y+11, 29, 52)
        
    def draw(self, win):
        if self.walkCount >= 26:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
            
    def hit(self, win):
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("+1", 1, (255, 255, 255))
        win.blit(text, (200, 200))
        pygame.time.delay(50)
        print("Coin")
        pygame.display.update()


class Coin(object):
    def __init__(self, x=200, y=280, radius=10, color=(255, 255, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        
def redrawWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    coin.draw(win)
    pygame.display.update()
    
    
man = Player()
run = True
coin = Coin()

while(run):
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    if coin.y - coin.radius < man.hitbox[1] + man.hitbox[3] and coin.y + coin.radius > man.hitbox[1]:
        if coin.x + coin.radius > man.hitbox[0] and coin.x - coin.radius < man.hitbox[0] + man.hitbox[2]:
            man.hit()
            
    
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x - man.vel > 0:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    
    elif keys[pygame.K_RIGHT] and man.x + man.vel + man.width < 500:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    
    else:
        man.standing = True
        man.walkCount = 0
        
    if man.isJump == False:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    
    else:   
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount))*0.5
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
            man.isJump = False

    
        
        
    redrawWindow()
    
    
pygame.quit()
        
