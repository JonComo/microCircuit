import region

class Network:
    def __init__(self):
        self.regions = []
        print "New network created"

    def create_network(self, region_count=1, region_size=10):
        self.regions = [region.Region(size=region_size, level=l) for l in xrange(region_count)]

    def description(self):
        for r in self.regions:
            print r.description()