class Score:
    def __init__(self,num):
        # instance variable
        self.count = 0
        self.alive = True
        self.highCount = num


    def getScore(self):
        return str(self.count)

    def scoreUp(self):
        self.count+=1
        if self.count > self.highCount:
            self.highCount+=1

    def getHighScore(self):
        return str(self.highCount)

    def lose(self):
        self.alive = False

    def reset(self):
        self.count = 0

    def getStatus(self):
        return self.alive