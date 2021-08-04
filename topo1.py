#!/usr/bin/python 

from mininet.net import Containernet 

from mininet.node import Controller, RemoteController 

from mininet.cli import CLI 

from mininet.link import TCLink 

from mininet.log import info, setLogLevel 

setLogLevel('info') 

   

net = Containernet(controller=None) 

info('*** Adding controller\n') 

net.addController(name='ryu' , controller=RemoteController , ip='192.168.75.169' , port=6633) 



info('*** Adding docker containers\n') 

d1 = net.addDocker('d1', ip='10.0.0.250', dimage="ubuntu:trusty") 

d2 = net.addDocker('d2', ip='10.0.0.251', dimage="ubuntu:trusty") 

d3 = net.addDocker('d3', ip='10.0.0.252', dimage="ubuntu:trusty") 

d4 = net.addDocker('d4', ip='10.0.0.253', dimage="ubuntu:trusty") 

d5 = net.addDocker('d5', ip='10.0.0.254', dimage="ubuntu:trusty") 

d6 = net.addDocker('d6', ip='10.0.0.255', dimage="ubuntu:trusty") 



info('*** Adding switches\n') 

s1 = net.addSwitch('s1') 

s2 = net.addSwitch('s2') 

s3 = net.addSwitch('s3') 



info('*** Creating links\n') 

net.addLink(d1, s1) 

net.addLink(d2, s1) 

net.addLink(s1, s2, cls=TCLink, delay='100ms', bw=1) 

net.addLink(s2, d3) 

net.addLink(s2, d4) 

net.addLink(s2, s3) 

net.addLink(s3, d5) 

net.addLink(s3, d6) 

 

info('*** Starting network\n') 

net.start() 



info('*** Testing connectivity\n') 

net.ping([d1, d3]) 



info('*** Running CLI\n') 

CLI(net) 

info('*** Stopping network') 

net.stop() 

 