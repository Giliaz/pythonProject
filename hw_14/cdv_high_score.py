# https://www.codewars.com/kata/5962bbea6878a381ed000036/train/python
class HighScoreTable:

    def __init__(self, a):
        self.lenth = a
        self.scores = []

    def update(self, n):
        self.scores.append(n)
        if len(self.scores) > self.lenth:
            self.scores.pop(self.scores.index(min(self.scores)))
        self.scores = sorted(self.scores, reverse=True)
        return self.scores

    def reset(self):
        self.scores = []
        return self.scores

