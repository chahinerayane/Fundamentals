# IPv4 – Internet Protocol Version 4

## Project Overview

A networking lab developed using Cisco Packet Tracer, focusing on IPv4 addressing and configuring IP addresses on Cisco router interfaces.

The project explores IPv4 address structure, subnet masks, CIDR notation, network identification, and interface configuration and verification.

## 1. What is IPv4?

IPv4 (Internet Protocol Version 4) is a network-layer protocol used to identify devices and enable communication across IP networks.

An IPv4 address consists of **32 bits**, divided into four 8-bit octets.

Example:

```text
192.168.2.254
```

Each octet represents a decimal value between 0 and 255.

## 2. Router Interface Configuration

The router was configured with three IPv4 addresses on separate GigabitEthernet interfaces.

** Running file **

```cisco
interface GigabitEthernet0/0
 description ## SW9 ##
 ip address 192.168.2.254 255.255.255.0

interface GigabitEthernet0/1
 description ## TO SW10 ##
 ip address 132.10.1.254 255.255.255.0

interface GigabitEthernet0/2
 description ## TO SW11 ##
 ip address 10.0.0.254 255.0.0.0
```

## 3. IP Addressing Table

| Interface | IP Address | Subnet Mask | CIDR |
|---|---|---|---|
| GigabitEthernet0/0 | 192.168.2.254 | 255.255.255.0 | /24 |
| GigabitEthernet0/1 | 132.10.1.254 | 255.255.255.0 | /24 |
| GigabitEthernet0/2 | 10.0.0.254 | 255.0.0.0 | /8 |

## 4. Understanding IPv4 Address Structure

An IPv4 address contains four octets, with each octet representing 8 bits.

Example:

```text
192.168.2.254
```

Binary representation:

```text
11000000.10101000.00000010.11111110
```

Each octet can have a value between 0 and 255.

## 5. Understanding Subnet Masks

A subnet mask determines which bits of an IPv4 address represent the network portion and which represent the host portion.

| CIDR | Subnet Mask | Network Bits | Host Bits |
|---|---|---:|---:|
| /8 | 255.0.0.0 | 8 | 24 |
| /24 | 255.255.255.0 | 24 | 8 |

### Example: 192.168.2.254/24

| Network Information | Value |
|---|---|
| Network Address | 192.168.2.0 |
| First Usable Address | 192.168.2.1 |
| Last Usable Address | 192.168.2.254 |
| Broadcast Address | 192.168.2.255 |
| Usable Hosts | 254 |

## 6. Interface Verification

The following Cisco IOS command displays the IP addresses and operational status of router interfaces.

```cisco
show ip interface brief
```

Example output:

```text
Interface              IP-Address      OK? Method Status                 Protocol
GigabitEthernet0/0     192.168.2.254   YES manual up                     up
GigabitEthernet0/1     132.10.1.254    YES manual up                     up
GigabitEthernet0/2     10.0.0.254      YES manual up                     up
Vlan1                  unassigned      YES unset   administratively down down
```

### Understanding Interface Status

- **Up/Up:** The physical interface and line protocol are operational.
- **Down/Down:** The physical connection or interface is not operational.
- **Administratively Down:** The interface has been manually disabled using the `shutdown` command.

## 7. Useful Cisco Commands

| Command | Purpose |
|---|---|
| `show ip interface brief` | Displays interface IP addresses and status |
| `show running-config` | Displays the current router configuration |
| `show ip interface` | Displays detailed IP interface information |
| `show interfaces` | Displays interface information and statistics |
| `show ip route` | Displays the routing table |
| `ping <destination-ip>` | Tests IP connectivity |

## 8. Technologies & Concepts

- IPv4 Addressing
- 32-bit IP Addresses
- Binary and Dotted-Decimal Notation
- Subnet Masks
- CIDR Notation
- Network and Broadcast Addresses
- Usable Host Addresses
- Cisco Router Interfaces
- GigabitEthernet
- Interface Configuration and Verification

## 9. Project Objective

Understand IPv4 addressing, configure IP addresses and subnet masks on Cisco router interfaces, identify network and host portions, and verify interface operational status using Cisco IOS commands.