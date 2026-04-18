class Octopus:
    def __init__(self, name, arms=8):
        self.name = name
        self.arms = arms

    def ink(self):
        return f"{self.name} releases ink to escape!"

    def __str__(self):
        return f"{self.name} with {self.arms} arms"
