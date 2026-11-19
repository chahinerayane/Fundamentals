# Spanning Tree Protocol (STP)

## Overview

This lab focuses on understanding and analyzing the Spanning Tree Protocol (STP) in a switched network containing four interconnected switches.

The objective is to understand how STP prevents Layer 2 loops by electing a Root Bridge, selecting the best paths, assigning port roles, and blocking redundant links.

## Topology

The topology consists of four switches connected with multiple redundant links.

- Switch0
- Switch1
- Switch2
- Switch3

## Root Bridge Election

All switches have the same Bridge Priority:

`32769`

The Bridge Priority consists of:

- Default Bridge Priority: `32768`
- VLAN ID: `1`

**Bridge Priority = 32768 + 1 = 32769**

Since all switches have the same priority, STP uses the lowest MAC address as the tie-breaker.

| Switch | Bridge Priority | MAC Address | Status |
|---|---:|---|---|
| Switch0 | 32769 | 00D0.BC67.48A1 | Non-Root |
| Switch1 | 32769 | 0040.0B43.532C | Non-Root |
| Switch2 | 32769 | 0050.0F52.5086 | Non-Root |
| Switch3 | 32769 | 0001.9798.39A5 | **Root Bridge** |

**Result:** Switch3 becomes the Root Bridge because it has the lowest MAC address among the four switches.

## STP Port Roles

After the Root Bridge election, STP determines the role of each port.

| Switch | Port Role | Description |
|---|---|---|
| Switch3 | Designated Ports | All active ports on the Root Bridge are Designated |
| Switch1 | Root Port | Best path toward the Root Bridge |
| Switch1 | Designated Ports | Ports toward Switch0 and Switch2 |
| Switch2 | Root Port | Best path toward Switch3 |
| Switch2 | Designated Ports | Ports toward Switch0 |
| Switch2 | Blocked Port | Redundant path toward Switch1 |
| Switch0 | Root Port | Best path toward Switch1 |
| Switch0 | Blocked Ports | Redundant links toward Switch2 |

### Port Role Identification

- **Root Port (R):** The port providing the best path toward the Root Bridge.
- **Designated Port (D):** The port responsible for forwarding traffic on a network segment.
- **Blocked Port (B):** A port that does not forward normal traffic, preventing Layer 2 loops.

## STP Path Cost

STP uses path cost to determine the best path toward the Root Bridge.

The path cost depends on the link bandwidth.

| Link Speed | STP Path Cost |
|---|---:|
| 10 Mbps | 100 |
| 100 Mbps | 19 |
| 1 Gbps | 4 |
| 10 Gbps | 2 |

Lower path cost means a better path toward the Root Bridge.

## What I Practiced

- Understanding STP and Layer 2 loop prevention.
- Root Bridge election using Bridge ID.
- Understanding Bridge Priority and MAC address.
- Identifying Root Ports, Designated Ports, and Blocked Ports.
- Understanding STP path costs.
- Analyzing redundant links between switches.
- Understanding how STP maintains a loop-free Layer 2 topology.

## Conclusion

STP allows switches to have redundant physical connections while maintaining a loop-free logical topology.

By electing a Root Bridge and blocking redundant paths, STP prevents switching loops while keeping alternative paths available in case of a network failure.