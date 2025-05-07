class Rectangel:
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def permiter(self):
        return 2*(self.w + self.h)