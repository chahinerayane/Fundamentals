# MAC Address Table & ICMP – Cisco Packet Tracer

## Project Overview

A networking lab developed using Cisco Packet Tracer to understand how switches learn and maintain MAC address tables and how devices communicate using ICMP (Internet Control Message Protocol).

The project demonstrates dynamic MAC address learning, Ethernet frame forwarding, communication between devices across multiple switches, and basic network connectivity testing.

## 1. Network Topology

The network consists of two interconnected switches connecting six PCs within the same Local Area Network (LAN).

**Network Address:** `192.168.1.0/24`

**Subnet Mask:** `255.255.255.0`

| Device | IP Address |
|---|---|
| PC0 | 192.168.1.1 |
| PC1 | 192.168.1.2 |
| PC5 | 192.168.1.3 |
| PC2 | 192.168.1.4 |
| PC6 | 192.168.1.5 |
| PC7 | 192.168.1.6 |

All devices belong to the same subnet and can communicate without requiring a router.

## 2. MAC Address Table

A MAC Address Table is maintained by a switch to associate MAC addresses with the interfaces where those devices are reachable.

Switches use this table to forward Ethernet frames to the correct destination port.

### Dynamic MAC Address Learning

Switches automatically learn MAC addresses by examining the source MAC address of incoming Ethernet frames.

The learning process works as follows:

1. A switch receives an Ethernet frame.
2. It reads the source MAC address.
3. It associates that MAC address with the incoming switch port and VLAN.
4. It stores this information in its MAC address table.
5. When another frame arrives, the switch checks the destination MAC address to determine where to forward it.

### Displaying the MAC Address Table

The following Cisco IOS command displays the switch's MAC address table:

```cisco
show mac address-table
```

Example output:

```text
Vlan    Mac Address       Type       Ports
----    -----------       --------   -----
1       0001.c938.8501    DYNAMIC    Fa0/3
1       0002.16e7.5c21    DYNAMIC    Fa0/3
1       000c.cf87.1dd3    DYNAMIC    Fa0/3
```

**Understanding the output:**

| Field | Description |
|---|---|
| VLAN | VLAN associated with the MAC address |
| MAC Address | Hardware address of the device |
| Type | How the address was learned (DYNAMIC or STATIC) |
| Ports | Switch interface associated with the MAC address |

### Dynamic vs. Static MAC Addresses

- **Dynamic:** Automatically learned by the switch from incoming frames. These entries are removed after their aging timer expires if they are not refreshed.
- **Static:** Manually configured MAC address entries that remain in the table until removed or changed.

## 3. ICMP – Internet Control Message Protocol

ICMP is a network-layer protocol used by devices to send control, diagnostic, and error-reporting messages.

It is commonly used to troubleshoot network connectivity and identify communication problems.

### ICMP and Ping

The `ping` command uses ICMP to test whether another IP device is reachable.

It works using two main message types:

- **ICMP Echo Request:** Sent by the source device to test connectivity.
- **ICMP Echo Reply:** Returned by the destination device if it receives and responds to the request.

### Testing Network Connectivity

Example:

```bash
ping 192.168.1.4
```

If the destination responds, the source receives ICMP Echo Reply messages.

A successful ping indicates that ICMP communication is working between the devices at that moment.

### Important ICMP Message Types

| ICMP Type | Message | Purpose |
|---|---|---|
| 0 | Echo Reply | Responds to an Echo Request |
| 3 | Destination Unreachable | Indicates that a destination cannot be reached |
| 5 | Redirect | Informs a host of a potentially better route |
| 8 | Echo Request | Tests connectivity using ping |
| 11 | Time Exceeded | Indicates that a packet's TTL expired |

## 4. How MAC Address Learning and ICMP Work Together

When one PC pings another PC in the same LAN, several networking processes take place.

1. The source PC checks whether the destination IP belongs to its local subnet.
2. If the destination MAC address is unknown, the PC uses ARP (Address Resolution Protocol) to discover it.
3. The source PC sends an Ethernet frame containing an ICMP Echo Request inside an IP packet.
4. Switches examine the frame's destination MAC address and forward it using their MAC address tables.
5. The destination PC receives the ICMP Echo Request.
6. It responds with an ICMP Echo Reply.
7. The switches forward the response back to the source PC.

**Important:** ARP resolves IPv4 addresses into MAC addresses on the local network. ICMP handles the connectivity test, while switches use MAC addresses to forward Ethernet frames.

## 5. Useful Cisco Commands

| Command | Purpose |
|---|---|
| `show mac address-table` | Displays learned MAC addresses |
| `show mac address-table dynamic` | Displays dynamically learned MAC addresses |
| `show interfaces status` | Displays switch interface status |
| `show vlan brief` | Displays VLAN information |
| `ping <destination-ip>` | Tests IP connectivity |

## 6. Technologies & Concepts

- Cisco Packet Tracer
- Local Area Networks (LAN)
- Ethernet Frames
- MAC Addresses
- MAC Address Tables (CAM Tables)
- Dynamic MAC Address Learning
- Ethernet Frame Forwarding
- ICMP (Internet Control Message Protocol)
- ICMP Echo Request and Echo Reply
- ARP (Address Resolution Protocol)
- IPv4 Addressing and Subnetting
- Network Troubleshooting

## 7. Project Objective

Understand how switches dynamically learn MAC addresses, maintain forwarding tables, and deliver Ethernet frames between devices.

Additionally, explore ICMP communication, understand how ping works, and practice basic network connectivity troubleshooting across interconnected switches.