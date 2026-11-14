# VLSM Subnetting – Multi-LAN Network

## Overview

This project demonstrates **Variable Length Subnet Masking (VLSM)** using Cisco Packet Tracer.

The network is designed using the `192.168.1.0/24` address space, divided into five subnets with different sizes according to the number of required hosts.

Two routers connect four separate LANs, allowing communication between different network segments.

## Network Topology

The topology consists of:

- 2 Routers
- 4 Switches
- 4 End Devices
- 4 LANs
- 1 Router-to-Router connection

## VLSM Addressing Plan

The original network is:

- Network: `192.168.1.0/24`
- Subnet Mask: `255.255.255.0`

The address space is divided according to host requirements, starting with the largest network.

| Network | Required Hosts | Network Address | CIDR | Subnet Mask |
|---|---:|---|---|---|
| LAN A | 110 | 192.168.1.0 | /25 | 255.255.255.128 |
| LAN D | 47 | 192.168.1.128 | /26 | 255.255.255.192 |
| LAN C | 30 | 192.168.1.192 | /27 | 255.255.255.224 |
| LAN B | 10 | 192.168.1.224 | /28 | 255.255.255.240 |
| Router Link | 2 | 192.168.1.240 | /30 | 255.255.255.252 |

## Subnet Details

| Network | Usable IP Range | Broadcast Address |
|---|---|---|
| LAN A | 192.168.1.1 – 192.168.1.126 | 192.168.1.127 |
| LAN D | 192.168.1.129 – 192.168.1.190 | 192.168.1.191 |
| LAN C | 192.168.1.193 – 192.168.1.222 | 192.168.1.223 |
| LAN B | 192.168.1.225 – 192.168.1.238 | 192.168.1.239 |
| Router Link | 192.168.1.241 – 192.168.1.242 | 192.168.1.243 |

## Router Interface Addressing

### Router 1 (Left)

| Interface | IP Address | Connected Network |
|---|---|---|
| G0/0 | 192.168.1.126 | LAN A |
| G0/1 | 192.168.1.238 | LAN B |
| Router Link | 192.168.1.241 | Router-to-Router |

### Router 2 (Right)

| Interface | IP Address | Connected Network |
|---|---|---|
| G0/0 | 192.168.1.222 | LAN C |
| G0/1 | 192.168.1.190 | LAN D |
| Router Link | 192.168.1.242 | Router-to-Router |

## Key Networking Concepts

- **VLSM:** Dividing a network into subnets with different subnet masks according to host requirements.
- **Subnetting:** Separating a larger network into smaller logical networks.
- **CIDR Notation:** Representing subnet masks using prefix lengths such as /25, /26, /27 and /28.
- **Default Gateway:** Allowing devices to communicate with networks outside their local subnet.
- **Point-to-Point Connection:** Connecting two routers using a /30 subnet.

## Verification & Troubleshooting

Useful commands for checking connectivity and network configuration:

```cisco
show ip interface brief
show ip route
show running-config
ping <destination-ip>
```

Connectivity should be tested between devices in different LANs.

## Tools Used

- Cisco Packet Tracer
- Cisco IOS CLI
- IPv4 Addressing
- VLSM Subnetting

## Learning Objectives

- Calculate subnet masks according to host requirements.
- Allocate IPv4 addresses efficiently using VLSM.
- Identify network, broadcast, and usable host addresses.
- Configure router interfaces with appropriate IP addresses.
- Connect multiple LANs through routers.
- Understand point-to-point addressing and default gateways.