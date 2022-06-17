from mininet.net import Mininet
from mininet.topo import Linear Topo


Linear=LinearTopo(k=4)
net=Mininet(topo=Linear)

net.start()
net.pingAll()
net.stop()
