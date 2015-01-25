import sys
import neuron
import random

class Region:
    def __init__(self, level=0, size=10):
        self.level = level
        self.size = size
        self.neurons = [[neuron.Neuron(amplitude=0, position=(x,y,level)) for y in xrange(size)] for x in xrange(size)]
        self.output_regions = []

    """Receive input in the form of array indices to active [0, 1] [100, 20] etc."""
    def input(self, indices):
        for index in indices:
            x = index[0]
            y = index[1]
            self.neurons[x][y].input(1)

    def output(self):
        return [n.region_position() for n in self.active()]

    def active(self):
        return [n for column in self.neurons for n in column if n.amplitude == 1]

    def sparse(self, remaining_count):
        active_neurons = self.active()
        random.shuffle(active_neurons)
        for n in active_neurons[0:len(active_neurons) - remaining_count]:
            n.amplitude = 0

    def description(self):
        print "Region: Level", self.level, "Neurons", len(self.neurons)
        for column in self.neurons:
            for n in column:
                sys.stdout.write("%s"%n.amplitude)
            sys.stdout.write('\n')