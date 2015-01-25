import region
import neuron
import random

def make_sparse(region, remaining_count):
    active_neurons = region.active()
    while len(active_neurons) > remaining_count:
        active_neurons.remove(random.choice(active_neurons))