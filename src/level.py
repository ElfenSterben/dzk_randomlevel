#coding:utf-8
import random
from cocos.sprite import Sprite


class Level(object):
    def __init__(self):
        super(Level, self).__init__()
        self.levels = 0
        self.number_of_blocks = 0
        self.blocks_pos = []
        self.h = 150
        self.w = 640
        self.hstart = 300
        self.wstart = 0
        self.next()

    def next(self):
        self.blocks_pos.clear()
        self.levels += 1
        block_width = 64
        block_height = 10
        i = random.randint(10, 150)
        self.number_of_blocks = i
        while i > 0:
            x = random.randrange(0, self.w, block_width)
            y = random.randrange(0, self.h, 10)
            bx = self.wstart + x + block_width / 2
            by = self.hstart + y + block_height / 2
            print(x, y)
            if (bx, by) not in self.blocks_pos:
                self.blocks_pos.append((bx, by))
                i -= 1


