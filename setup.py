#!/usr/bin/python
#sudo mn --custom setup.py  --topo mytopo --test pingall

#host --- switch --- host

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

## host1 ----- switch -----/ 10% loss /----- host2
class SimpleTopology( Topo ):
  "Simple topology example."
  def build(self,inloss=10):
    # Add hosts and switches
    lHost = self.addHost( 'h1' )
    rHost = self.addHost( 'h2' )
    switch = self.addSwitch( 's1' )
    # Add links
    self.addLink( lHost, switch )
    self.addLink( rHost, switch, loss=inloss)

def simpleTest():
  "Create and test a simple network"
  topo = SimpleTopology(inloss=10)
  net = Mininet(topo=topo, 
                host=CPULimitedHost, link=TCLink)
  net.start()
  print "Dumping host connections"
  dumpNodeConnections(net.hosts)
  print "Testing network connectivity"
  net.pingAll()
  net.stop()

if __name__ == '__main__':
  # Tell mininet to print useful information
  setLogLevel('info')
  simpleTest()
