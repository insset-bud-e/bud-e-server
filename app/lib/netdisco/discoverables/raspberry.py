from . import MDNSDiscoverable

class Discoverable(MDNSDiscoverable):
    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_raspberry._tcp.local.')
