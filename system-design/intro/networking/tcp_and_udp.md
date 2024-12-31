# TCP and UDP: Networking Notes

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two primary protocols used for data transmission over the internet. They have distinct features and use cases depending on reliability, speed, and application requirements.

## TCP (Transmission Control Protocol)

### Key Features of TCP

1. **Reliable Transmission**:
   - Ensures all packets are delivered to the recipient.
   - Lost packets are retransmitted until acknowledged by the receiver.
2. **Connection-Oriented**:
   - Establishes a two-way connection between devices (3-way handshake) before data transfer.
   - The handshake ensures both devices are ready to communicate.
3. **Order Guarantee**:
   - Packets are reassembled in the correct order, even if they arrive out of sequence.
4. **Acknowledgment**:
   - Each transmitted packet requires an acknowledgment.
   - If no acknowledgment is received, TCP retransmits the packet.

### Drawbacks of TCP

- **Overhead**: The need for connection setup and acknowledgment increases processing time.
- **Slower Transmission**: The reliability mechanisms make TCP slower than UDP.

### Use Cases for TCP

- Applications where data integrity and reliability are critical:
  - **File transfers** (e.g., FTP)
  - **Web browsing** (e.g., HTTP/HTTPS)
  - **Email** (e.g., SMTP)

### 3-Way Handshake

A **3-way handshake** is a process used in the **TCP (Transmission Control Protocol)** to establish a reliable connection between two devices (client and server) before data is transmitted. It ensures that both devices are ready to communicate and agree on initial sequence numbers for reliable data delivery.

#### Steps of the 3-Way Handshake

1. **SYN (Synchronize):**

   - The **client** sends a TCP segment with the **SYN** flag set to the **server**.
   - This indicates the client wants to establish a connection.
   - The client also includes an **initial sequence number (ISN)** to track data.

   **Example:**

   - Client → Server: "I want to connect (SYN), here’s my sequence number: 100."

2. **SYN-ACK (Synchronize + Acknowledge):**

   - The **server** responds with a TCP segment that has both the **SYN** and **ACK** flags set.
   - It acknowledges the client’s ISN by incrementing it (ISN + 1).
   - The server also includes its own ISN.

   **Example:**

   - Server → Client: "Acknowledged (ACK your 100 + 1), I also want to connect (SYN). Here’s my sequence number: 300."

3. **ACK (Acknowledge):**

   - The **client** responds with an **ACK** segment.
   - It acknowledges the server’s ISN by incrementing it (ISN + 1).
   - The connection is now established, and data transmission can begin.

   **Example:**

   - Client → Server: "Acknowledged (ACK your 300 + 1). Ready to send data!"

#### Summary of Flags

- **SYN:** Initiates a connection.
- **ACK:** Acknowledges receipt of a segment.
- **SYN-ACK:** A combination of SYN and ACK, used to acknowledge and synchronize.

#### Visual Representation

```txt
Client                  Server
  | SYN (SEQ=100) ----->|
  |<---- SYN-ACK (SEQ=300, ACK=101) |
  | ACK (SEQ=101, ACK=301) ----->|
Connection Established
```

#### Why is the 3-Way Handshake Important?

1. **Reliability:**

   - Ensures both devices are ready to communicate.
   - Synchronizes sequence numbers to manage data flow and prevent duplication.

2. **Security:**
   - Protects against connection-related errors (e.g., avoiding unexpected data transfer).
   - Basis for advanced features like SYN cookies (used to prevent SYN flood attacks).

## UDP (User Datagram Protocol)

### Key Features of UDP

1. **Fast Transmission**:
   - Lacks reliability mechanisms, making it faster than TCP.
2. **Connectionless**:
   - No need for a handshake or connection setup before data transfer.
3. **No Retransmission**:
   - Does not resend lost packets or ensure packets are received in order.

### Benefits of UDP

- Lower overhead.
- Suitable for time-sensitive applications where speed is more important than accuracy.

### Drawbacks of UDP

- No guarantee of packet delivery.
- Packets may arrive out of order or be dropped without notice.

### Use Cases for UDP

- Applications where speed and efficiency are prioritized over reliability:
  - **Online gaming**: Skipping a frame is better than introducing delays.
  - **Video streaming**: Ensures smooth playback even with occasional data loss.
  - **Voice over IP (VoIP)**: Maintains real-time communication without latency.

## Closing Notes

- **TCP** is ideal for scenarios requiring data integrity and reliability.
- **UDP** excels in situations demanding speed and low latency.
- As developers, understanding these protocols helps in choosing the right one for a specific application.
- For most software engineering tasks, focus remains on **application-layer protocols** like HTTP.
