class OceanHabitat:
    def __init__(self, depth, temperature):
        self.depth = depth
        self.temperature = temperature

    def describe(self):
        return f"Habitat at {self.depth}m depth, {self.temperature}°C"
