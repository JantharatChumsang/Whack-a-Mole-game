class TRUMP(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.current_frame2 = 0
        self.last_update2 = 0
        self.load_images()
        self.animate2()

        self.image = self.TRUMP_fingers_l[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH *3/4), (589)
        self.pos = vec((WIDTH/2), (HEIGHT/2))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

    def load_images(self):

        self.TRUMP_fingers_l = [self.game.spritesheet.get_image(503, 1, 248, 559)]
        for frame in self.TRUMP_fingers_l:
            frame.set_colorkey(BLACK)
        self.TRUMP_walk1_l = [self.game.spritesheet.get_image(643, 562, 249, 448)]
        self.TRUMP_walk2_l = [self.game.spritesheet.get_image(894, 474, 249, 448)]
        self.TRUMP_hailing = [self.game.spritesheet.get_image(1, 571, 248, 439)]
        self.TRUMP_throwing = [self.game.spritesheet.get_image(753, 1, 248, 471)]
        self.TRUMP_smug = [self.game.spritesheet.get_image(252, 1, 249, 562)]
        self.TRUMP_flexing_l = [self.game.spritesheet.get_image(1, 1, 249, 568)]

    def animate2(self):

       now = pg.time.get_ticks()
       if now - self.last_update2 > 200:
            self.last_update2 = now
            self.current_frame2 = self.TRUMP_hailing[0]
            self.image = self.TRUMP_hailing[0]