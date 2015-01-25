class Neuron:
    def __init__(self, position=(0,0,0), amplitude=1):
        self.position = position
        self.amplitude = amplitude
        pass

    def set_position(self, x, y, z):
        self.position = (x, y, z)

    def region_position(self):
        return [self.position[0], self.position[1]]

    def input(self, value):
        self.amplitude = value

    def description(self):
        return "[({0}) {1},{2},{3}]".format(self.amplitude, self.position[0], self.position[1], self.position[2])