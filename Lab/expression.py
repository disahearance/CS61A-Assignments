class Ratio:
    def __init__(self, n, d):
        self.number = n
        self.denom = d
    def __repr__(self):
        return "Ratio({0},{1})，哈哈哈".format(self.number, self.denom)
    def __str__(self):
        return "{0}/{1}".format(self.number, self.denom)
    
