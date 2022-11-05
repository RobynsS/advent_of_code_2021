class Lanterfish:
    def __init__(self, timer=8):
        self.timer = timer
        self.new = False

    def step(self):
        self.new = False
        self.timer -= 1
        if self.timer < 0:
            self.new = True
            self.timer = 6

    def has_new(self):
        return self.new
