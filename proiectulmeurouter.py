from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost


class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    # pylint: disable=arguments-differ
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

    # pylint: disable=arguments-differ
    def build( self, **_opts ):

        defaultIP = '192.168.1.1/24'  # IP address for r0-eth1
        router = self.addNode( 'r0', cls=LinuxRouter, ip=defaultIP )

        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
 

        self.addLink( s6, router, intfName2='r0-eth1',
                      params2={ 'ip' : defaultIP } )  # for clarity
        self.addLink( s7, router, intfName2='r0-eth2',
                      params2={ 'ip' : '172.16.0.1/12' } )
        self.addLink(s6, s1)
        self.addLink(s6, s2)
        self.addLink(s7, s3)
        self.addLink(s7, s4)
        self.addLink(s7, s5)
        

        h1 = self.addHost( 'h1', ip='192.168.1.10/24',
                           defaultRoute='via 192.168.1.1' )
        h2 = self.addHost( 'h2', ip='192.168.1.20/24',
                           defaultRoute='via 192.168.1.1' )
        h3 = self.addHost( 'h3', ip='192.168.1.30/24',
                           defaultRoute='via 192.168.1.1' )
        h4 = self.addHost( 'h4', ip='192.168.1.40/24',
                           defaultRoute='via 192.168.1.1' )
        h5 = self.addHost( 'h5', ip='172.16.0.10/12',
                           defaultRoute='via 172.16.0.1' )
        h6 = self.addHost( 'h6', ip='172.16.0.20/12',
                           defaultRoute='via 172.16.0.1' )
        h7 = self.addHost( 'h5', ip='172.16.0.30/12',
                           defaultRoute='via 172.16.0.1' )
        h8 = self.addHost( 'h5', ip='172.16.0.40/12',
                           defaultRoute='via 172.16.0.1' )
        h9 = self.addHost( 'h5', ip='172.16.0.50/12',
                           defaultRoute='via 172.16.0.1' )
        h10 = self.addHost( 'h10', ip='172.16.0.60/12',
                           defaultRoute='via 172.16.0.1' )
                           
                           
        self.addLink(s1, h1,bw=10)
        self.addLink(s1, h2,bw=10)
        self.addLink(s2, h3,delay='15ms')
        self.addLink(s2, h4)
        self.addLink(s3, h5)
        self.addLink(s3, h6)
        self.addLink(s4, h7)
        self.addLink(s4, h8)
        self.addLink(s5, h9)
        self.addLink(s5, h10)
        
        
       
        
        
        
        
        
        
        
        
        
def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo,
                   waitConnected=True )  # controller is used by s1-s7
    net.start()
    # Aici afisam tabela Routerului 
    info( '*** Routing Table on Router:\n' )
    info( net[ 'r0' ].cmd( 'route' ) )
    
     #Aici vedem daca comunica hosturile intre ele
        
    net.pingAll()
    
    # Aici afisam viteza de transfer de date intre doua hosturi
    
    info( "Dumping host connections\n" )
    dumpNodeConnections(net.hosts)
    info( "Testing bandwidth between h1 and h4\n" )
    h1, h10 = net.getNodeByName('h1', 'h10')
    
    
    net.iperf( ( h1, h10 ), l4Type='UDP' )
    
    
    
    
    
    CLI( net )
    net.stop()
  
if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
                    
                         

        


