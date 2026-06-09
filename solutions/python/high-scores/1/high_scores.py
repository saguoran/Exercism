class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        top_list = [score for score in sorted(self.scores, reverse=True)[:3] if score]
        return top_list

    def report(self):
        if(self.latest() == self.personal_best()):
            return f"Your latest score was {self.latest()}. That's your personal best!"
        else:
            return f"Your latest score was {self.latest()}. That's {self.personal_best()-self.latest()} short of your personal best!"
