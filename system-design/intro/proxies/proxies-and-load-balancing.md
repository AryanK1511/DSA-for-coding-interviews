# Proxies & Load Balancers

## 1. Proxies

### Forward Proxy

- Acts as an intermediary between a client and the internet.
- **Key Features**:
  - **Privacy**: Masks the client's IP address by using the proxy’s address.
  - **Caching**: Stores frequently requested data for faster access.
  - **Access Control**: Filters requests, restricting access to certain websites.
- **Example**: A school proxy server blocking access to entertainment sites.

### Reverse Proxy

- Intercepts requests from the internet and forwards them to the appropriate server.
- **Key Features**:
  - **Server Anonymity**: Masks the destination server from the client.
  - **Load Balancing**: Distributes incoming traffic across multiple servers.
  - **DDoS Protection**: Shields origin servers from malicious traffic.
- **Example**: A CDN acting as a reverse proxy by serving cached content directly.

## 2. Load Balancers

A type of reverse proxy that distributes traffic across multiple servers to ensure optimal performance and resource utilization.

### Load Balancing Strategies

1. **Round Robin**:

   - Requests are distributed sequentially across servers.
   - Assumes equal workload capacity for all servers.
   - Simple and effective for homogeneous server environments.

2. **Weighted Round Robin (WRR)**:

   - Requests are distributed based on server capacity (e.g., CPU, RAM).
   - Ensures proportional resource utilization.
   - Example: Server A (50%) handles 2 requests, Server B (25%) handles 1, etc.

3. **Least Connections**:

   - Assigns requests to the server with the fewest active connections.
   - Useful for unpredictable workloads or varying request complexities.
   - Example: E-commerce during peak times, where checkout requests are heavier than browsing.

4. **User Location**:

   - Routes traffic to the server geographically closest to the user.
   - Reduces latency and improves response times.
   - Example: A user in Asia is routed to a server in Asia.

5. **Layer 4 vs. Layer 7 Load Balancing**:
   - **Layer 4 (Transport Layer)**:
     - Routes traffic based on IP address and TCP/UDP ports.
     - Fast but less granular.
   - **Layer 7 (Application Layer)**:
     - Routes traffic based on HTTP headers, methods, or body content.
     - Slower but offers sophisticated routing options.

## 3. Benefits of Load Balancers

- **Improved Performance**: Distributes traffic to avoid overloading servers.
- **High Availability**: Ensures redundancy; traffic is rerouted if a server fails.
- **Scalability**: Enables horizontal scaling by managing traffic across multiple servers.
- **Enhanced Security**: Protects servers from direct exposure to malicious traffic.

## Key Tools and Resources

- **Maglev**: Google’s internal software-based network load balancer.
- **Nginx**: Open-source load balancer supporting multiple strategies (e.g., WRR, least connections).
- **Cloud Providers**: AWS, GCP, and Azure offer managed load balancers for seamless scaling and traffic management.

### Closing Notes

Proxies and load balancers are essential for building scalable, secure, and performant systems. While proxies focus on privacy, caching, and traffic filtering, load balancers ensure efficient resource utilization and high availability.
