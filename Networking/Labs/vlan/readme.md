# VLAN Segmentation & Inter-VLAN Routing

## Overview

This project demonstrates VLAN configuration and inter-VLAN routing using Cisco Packet Tracer.

The network represents a company divided into three departments: Finance, HR, and Engineering.

Each department is assigned a separate VLAN and IPv4 subnet to provide logical network segmentation. A Cisco router with three physical interfaces enables communication between the departments.

## Network Topology

The network consists of:

- 1 Router
- 1 Layer 2 Switch
- 3 VLANs each 2 pcs
- 3 IPv4 subnets

## VLAN Configuration

| VLAN ID | Department | Network | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| 10 | Finance | 192.168.1.0/26 | 255.255.255.192 | 192.168.1.62 |
| 20 | HR | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.190 |
| 30 | Engineering | 192.168.1.64/26 | 255.255.255.192 | 192.168.1.126 |

## Switch Configuration

The switch uses access ports to assign end devices to their respective VLANs.

| Switch Ports | VLAN | Department |
|---|---|---|
| Fa0/1 – Fa0/3 | 10 | Finance |
| Fa0/4 – Fa0/6 | 20 | HR |
| Fa0/7 – Fa0/9 | 30 | Engineering |

### VLAN Creation

```cisco
vlan 10
 name FINANCE

vlan 20
 name HR

vlan 30
 name ENGINEERING
```

### Access Port Configuration

```cisco
interface range FastEthernet0/1-3
 switchport mode access
 switchport access vlan 10

interface range FastEthernet0/4-6
 switchport mode access
 switchport access vlan 20

interface range FastEthernet0/7-9
 switchport mode access
 switchport access vlan 30
```

## Router Configuration

The router uses three physical GigabitEthernet interfaces, each connected to a separate VLAN.

| Interface | IP Address | Connected VLAN |
|---|---|---|
| G0/0 | 192.168.1.62/26 | VLAN 10 |
| G0/1 | 192.168.1.126/26 | VLAN 30 |
| G0/2 | 192.168.1.190/26 | VLAN 20 |

This configuration enables inter-VLAN routing through the router.

## Key Networking Concepts

- **VLANs:** Logically separating devices into different broadcast domains.
- **Access Ports:** Assigning switch ports to specific VLANs.
- **Inter-VLAN Routing:** Allowing communication between different VLANs through a router.
- **IPv4 Subnetting:** Assigning separate subnets to different departments.
- **Default Gateway:** Providing a path for devices to reach other networks.

## Verification & Troubleshooting

Useful Cisco IOS commands:

```cisco
show vlan brief
show interfaces status
show ip interface brief
show ip route
show running-config
```

Connectivity can be tested using `ping` between devices belonging to different VLANs.

## Tools Used

- Cisco Packet Tracer
- Cisco IOS CLI
- IPv4
- VLAN Configuration
- Inter-VLAN Routing

## Learning Objectives

- Create and configure VLANs.
- Assign switch access ports to VLANs.
- Configure router interfaces for different subnets.
- Understand broadcast domain separation.
- Implement inter-VLAN routing.
- Verify and troubleshoot network connectivity.