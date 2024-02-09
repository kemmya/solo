class ChallengeTracking:
    def __init__(self):
        self.learners = []

    def add_learner(self,name):
        self.learners = []
        self.learners.append(name)
        return self.learners
        
    
    def track_learners(self, name):
        if name not in self.learners:
            self.add_learner(name)
        else:
            return "Learner name already exists"
        return self.learners