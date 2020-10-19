"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )


        # Add links
        self.addLink( s1, s2, cls=TCLink, bw=1000, delay='1ms' )
        self.addLink( s1, s4, cls=TCLink, bw=1000, delay='1ms' )
        self.addLink( s1, h1, cls=TCLink, bw=100, delay='10ms' )

        self.addLink( s2, s4, cls=TCLink, bw=100, delay='5ms' )
        self.addLink( s2, s3, cls=TCLink, bw=1000, delay='1ms' )
        self.addLink( s2, h2, cls=TCLink, bw=100, delay='10ms' )

        self.addLink( s3, s4, cls=TCLink, bw=1000, delay='1ms' )
        self.addLink( s3, h3, cls=TCLink, bw=100, delay='10ms' )
        
        self.addLink( s4, h4, cls=TCLink, bw=100, delay='10ms' )
        


topos = { 'mytopo': ( lambda: MyTopo() ) }