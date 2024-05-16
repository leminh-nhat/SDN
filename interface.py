#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    cA=net.addController(name='cA',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    cB=net.addController(name='cB',
                      controller=Controller,
                      protocol='tcp',
                      port=6634)

    info( '*** Add switches\n')
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s21 = net.addSwitch('s21', cls=OVSKernelSwitch)
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    AAh1 = net.addHost('AAh1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    AAh2 = net.addHost('AAh2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    ABh1 = net.addHost('ABh1', cls=Host, ip='10.0.0.3', defaultRoute=None)
    ABh2 = net.addHost('ABh2', cls=Host, ip='10.0.0.4', defaultRoute=None)
    BAh1 = net.addHost('BAh1', cls=Host, ip='10.0.0.5', defaultRoute=None)
    BAh2 = net.addHost('BAh2', cls=Host, ip='10.0.0.6', defaultRoute=None)
    BBh1 = net.addHost('BBh1', cls=Host, ip='10.0.0.7', defaultRoute=None)
    BBh2 = net.addHost('BBh2', cls=Host, ip='10.0.0.8', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s11, AAh1)
    net.addLink(s11, AAh2)
    net.addLink(s12, ABh1)
    net.addLink(s12, ABh2)
    net.addLink(s12, s1)
    net.addLink(s11, s1)
    net.addLink(s2, s1)
    net.addLink(s21, BAh1)
    net.addLink(s21, BAh2)
    net.addLink(s22, BBh1)
    net.addLink(s22, BBh2)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s11').start([cA])
    net.get('s12').start([cA])
    net.get('s21').start([cB])
    net.get('s22').start([cB])
    net.get('s1').start([cA])
    net.get('s2').start([cB])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
