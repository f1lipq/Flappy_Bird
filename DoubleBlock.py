from Block import Block

class DoubleBlock:
    def __init__(self, x1, y1, width1, height1, x2, y2, width2, height2):
        self.top_block = Block(x1, y1, width1, height1)
        self.bottom_block = Block(x2, y2, width2, height2)

    def update(self):
        self.top_block.update()
        self.bottom_block.update()

    def draw(self, canvas):
        self.top_block.draw(canvas)
        self.bottom_block.draw(canvas)
    
    def collide_bird(self, bird):
        if bird.rect.colliderect(self.top_block.rect) or bird.rect.colliderect(self.bottom_block.rect):
            return True
        return False
    
    def comeback(self):
        self.top_block.comeback()
        self.bottom_block.comeback()