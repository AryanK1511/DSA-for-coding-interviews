# Networking Basics

Networking is essential for enabling communication between devices. This guide offers a developer-friendly introduction to networking concepts using a client-server architecture. We'll use Alice and Bob as examples to illustrate the principles.

## Networks

### What is a Network?

A network connects devices, enabling them to send and receive data using unique **IP addresses** as identifiers.

### Example: Alice and Bob Communication

- **Alice** creates an invitation (data) and sends it to **Bob** (another device) over the network.
- Alice's and Bob's IP addresses ensure data is routed correctly.

## IP Address

### Overview

An IP address uniquely identifies devices on a network. Two main types:

1. **IPv4**: 32-bit, limited to ~4.3 billion addresses (e.g., `192.168.1.1`).
2. **IPv6**: 128-bit, with a vast address space (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

### Comparison

| **Feature**    | **IPv4**                          | **IPv6**                                  |
| -------------- | --------------------------------- | ----------------------------------------- |
| Address Length | 32-bit                            | 128-bit                                   |
| Format         | Decimal (e.g., `255.255.255.255`) | Hexadecimal (e.g., `xxxx:xxxx:xxxx:xxxx`) |
| Address Space  | Limited                           | Virtually unlimited                       |

## Data Transmission Protocols

### Sending Data Over a Network

Data transmission follows specific rules called **protocols**. Key protocols:

1. **IP (Internet Protocol)**: Routes packets to the correct destination.
2. **TCP (Transmission Control Protocol)**: Ensures reliable delivery.

### Data Packets

- Data is split into **packets** containing:
  - **Header**: Includes source/destination IPs (like the envelope for Alice’s letter). There is a TCP header and an IP header. The IP header just has the source and destination and the TCP header is responsible for reassembling the data in order.
  - **Payload**: Actual data (Alice's invitation). This is mainly what we worry about as software engineers. This is where the HTTP data lives for example.
  - **Trailer**: Additional metadata.

## TCP (Transmission Control Protocol)

### Reliable Data Delivery

TCP ensures:

1. **Order**: Packets are reassembled in the correct order.
2. **Accuracy**: All packets are received intact.

**Example**: Alice sends a multi-page letter to Bob, numbering the pages for correct assembly.

## Application Data

- As developers, focus on the **application data** within packets.
- Examples:
  - **HTTP POST request**: Data is in the payload.
  - **HTTP GET request**: Data represents the response.

## Network Layers

Networking protocols are organized into layers:

1. **Application Layer**: Handles client-server interactions (e.g., HTTP).
2. **Transport Layer**: Ensures data reliability (e.g., TCP).
3. **Network Layer**: Routes data (e.g., IP).

## Public vs Private Networks

Not every machine has a public IP address. Here’s how it works:

1. **Public IP Address:**

   - Assigned to devices directly accessible over the internet.
   - Typically assigned to your **router** by your Internet Service Provider (ISP).
   - Example: Your router has a public IP address visible to the internet.

2. **Private IP Address:**
   - Used within your local network (e.g., your home network).
   - Assigned to devices (e.g., your computer, phone) by your router using a protocol like DHCP (Dynamic Host Configuration Protocol).
   - Private IPs cannot communicate directly with the internet; they rely on the router's public IP.

### NAT (Network Address Translation)

When your device connects to the router:

- It gets a **private IP** (e.g., `192.168.0.101`).
- The router acts as an intermediary and translates your private IP to the router's **public IP** when sending data to the internet.
- This process is called **NAT (Network Address Translation)**.

### Does My Machine Get the Same Public IP?

Yes and no:

1. **Yes:**
   - When your device connects to the internet through your router, it uses the same public IP address as the router. This is because the router "hides" your private IP behind its public IP using NAT.
2. **No:**
   - Your device itself does not get assigned a public IP; it always retains its private IP within the local network.

### Key Points

- The router's **public IP** represents the entire network to the internet.
- Multiple devices in your local network (laptop, phone, etc.) share the router's public IP when accessing the internet.
- For direct internet accessibility (e.g., hosting a server), you would need to configure port forwarding or assign a device a public IP (rare for home networks).

## Static vs Dynamic IP Addresses

| **Type**    | **Description**                                 | **Use Case**               |
| ----------- | ----------------------------------------------- | -------------------------- |
| **Static**  | Fixed, manually configured IP address.          | Servers, critical systems. |
| **Dynamic** | Temporary, assigned automatically (can change). | Home networks, clients.    |

## Ports

Ports identify specific applications/services on a device. There are about 65000 ports for a machine. Examples:

- **Port 80**: HTTP.
- **Port 4200**: Default for Angular applications.

**Key Point**: Two applications cannot use the same port simultaneously.

## Summary

Networking relies on layers, protocols, and unique identifiers (IP addresses and ports) to enable communication between devices. Understanding these basics is foundational for developers.
