import circuit
from numberEncoder import *
import random

size = 10

net = circuit.Network()
net.create_network(region_count=1, region_size=size)

input_region = net.regions[0]

encode_int(22, input_region)

input_region.description()

print "Decoded int", decode_int(input_region)

#input_region.input([[x,y] for x in xrange(size) for y in xrange(size)])
#input_region.sparse(remaining_count=int(pow(size,2) * .2))