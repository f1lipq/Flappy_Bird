import pygame

class BestScore:
    def __init__(self):
        try:
            f = open("bestScore.csv", "r")
            self.bestScore = int(str(f.read(1)))
            f.close()
        except Exception as ex:
            print(f'{ex}')
            self.bestScore = 0
        self.score = 0
    
    def check(self):
        if self.score > self.bestScore:
            f = open("bestScore.csv", "w")
            self.bestScore = self.score
            f.write(f'{self.bestScore}')
            f.close()

        return self.bestScore