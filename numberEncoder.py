import math

def encode_int(value, region):
    for i in xrange(value):
        region.neurons[int(math.floor(i / region.size))][int(i%10)].input(1)

def decode_int(region):
    i = 0
    while region.neurons[int(math.floor(i / region.size))][int(i%10)].amplitude == 1:
        i += 1

    return i