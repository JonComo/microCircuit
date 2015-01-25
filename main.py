import circuit

size = 10

net = circuit.Network()
net.create_network(region_count=10, region_size=size)

input_region = net.regions[0]

input_region.input([[x,y] for x in xrange(size) for y in xrange(size)])

input_region.sparse(remaining_count=int(pow(size,2)*.1))

input_region.description()
print "Active", len(input_region.active())