from mininet.topo import Topo

class MyTopo( Topo ):

	def build( self ):
	
	
		#Add Hosts and switches
		
		Host1 = self.addHost( 'h1' )
		Host2 = self.addHost( 'h2' )
		Switch1= self.addSwitch( 's1' )
		Switch2= self.addSwitch( 's2' )
		Host3 = self.addHost( 'h3' )
		Host4 = self.addHost( 'h4' )
		Host5 = self.addHost( 'h5' )
		Host6 = self.addHost( 'h6' )
		Switch3= self.addSwitch( 's3' )
		Host7 = self.addHost( 'h7' )
		Host8 = self.addHost( 'h8' )
		Host9 = self.addHost( 'h9' )
		
		
		
		#Add links
		
		self.addLink( Host1, Switch1 )
		self.addLink( Switch1, Switch2 )
		self.addLink( Switch2, Host2)
		self.addLink( Host3, Switch1 )
		self.addLink( Host4, Switch1 )
		self.addLink( Switch2, Host5 )
		self.addLink( Switch2, Host6 ) 
		self.addLink( Host7, Switch3 )
		self.addLink( Host8, Switch3 )
		self.addLink( Host9, Switch3 )
		self.addLink( Switch1, Switch3 )
		self.addLink( Switch1, Switch2 )
		
		
		
		
		
topos = { 'mytopo' : ( lambda: MyTopo() ) }

