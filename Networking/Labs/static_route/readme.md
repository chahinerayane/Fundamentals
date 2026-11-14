# Redundant Network Topology – Static Routing

## Overview

This project demonstrates a network topology built using **Cisco Packet Tracer**, consisting of four routers, two switches, and four end devices.

The network uses **static routing** to establish communication between two separate LANs through two alternative paths.

The main objective is to understand static routing, network segmentation, IP addressing, and redundant network paths.

## Network Topology

The topology contains four routers connected in a square configuration, providing two paths between the source and destination networks.

- **Upper path:** R1 → R3 → R4
- **Lower path:** R1 → R2 → R4

Each LAN is connected to its respective edge router through a switch.

## IP Addressing Scheme

| Network | Description |
|---|---|
| 192.168.1.0/24 | LAN 1 |
| 192.168.12.0/24 | R1 – R3 |
| 192.168.13.0/24 | R1 – R2 |
| 192.168.20.0/24 | R3 – R4 |
| 192.168.30.0/24 | R2 – R4 |
| 192.168.4.0/24 | LAN 2 |

### Router Interfaces

| Router | Interface | IP Address |
|---|---|---|
| R1 | G0/0 | 192.168.1.254 |
| R1 | G0/1 | 192.168.13.1 |
| R1 | G0/2 | 192.168.12.1 |
| R2 | G0/0 | 192.168.13.2 |
| R2 | G0/1 | 192.168.30.2 |
| R3 | G0/0 | 192.168.12.3 |
| R3 | G0/1 | 192.168.20.3 |
| R4 | G0/0 | 192.168.30.4 |
| R4 | G0/1 | 192.168.20.4 |
| R4 | G0/2 | 192.168.4.254 |

### End Devices

| Device | IP Address | Default Gateway |
|---|---|---|
| PC0 | 192.168.1.1 | 192.168.1.254 |
| PC2 | 192.168.1.2 | 192.168.1.254 |
| PC1 | 192.168.4.1 | 192.168.4.254 |
| PC3 | 192.168.4.2 | 192.168.4.254 |

## Routing Configuration

The network uses **static routes** to reach remote networks.

Each router is configured with routes pointing to the appropriate next-hop IP address.

### R1

```cisco
ip route 192.168.4.0 255.255.255.0 192.168.12.3
ip route 192.168.4.0 255.255.255.0 192.168.13.2
```

### R2

```cisco
ip route 192.168.1.0 255.255.255.0 192.168.13.1
ip route 192.168.4.0 255.255.255.0 192.168.30.4
```

### R3

```cisco
ip route 192.168.1.0 255.255.255.0 192.168.12.1
ip route 192.168.4.0 255.255.255.0 192.168.20.4
```

### R4

```cisco
ip route 192.168.1.0 255.255.255.0 192.168.20.3
ip route 192.168.1.0 255.255.255.0 192.168.30.2
```

## Key Networking Concepts

- **Static Routing:** Manually configuring routes to reach remote networks.
- **Equal-Cost Multi-Path (ECMP):** Using multiple routes with equal routing preference to reach the same destination.
- **Redundant Paths:** Providing alternative paths between networks.
- **IP Addressing:** Assigning IPv4 addresses and subnet masks to network interfaces.
- **Default Gateway:** Allowing end devices to communicate with remote networks.

## Verification & Troubleshooting

The following Cisco IOS commands are useful for verifying the network configuration:

```cisco
show ip interface brief
show ip route
show running-config
traceroute 192.168.4.1
```

Connectivity can be tested using `ping` between devices located in different LANs.

## Learning Objectives

- Configure router interfaces and IPv4 addresses.
- Establish communication between separate LANs.
- Configure static routes on multiple routers.
- Understand equal-cost routing.
- Explore redundant network paths.
- Troubleshoot connectivity using Cisco IOS commands.