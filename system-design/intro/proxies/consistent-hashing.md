# Consistent Hashing

- **Consistent Hashing** is a technique used in load balancing to map requests to servers (nodes) in a predictable and efficient way.
- It ensures that the same user (or request) is always routed to the same server unless that server becomes unavailable, which minimizes cache misses and redistributions.

## How Does Regular Hashing Work?

1. A hash function calculates the hash of a unique identifier (e.g., IP address).
2. The hash is then modded by the number of available servers to determine the server handling the request.
3. Example with 3 servers:
   - IP `6 % 3 = 0`, routed to Server 0.
   - IP `7 % 3 = 1`, routed to Server 1.
   - IP `8 % 3 = 2`, routed to Server 2.

### Issue with Regular Hashing

- When a server goes down, the hash distribution changes, reassigning many users to new servers, leading to:
  - **Cache Misses**: Previously cached data is no longer available.
  - **Overhead**: Servers must recompute and redistribute load.

### How Consistent Hashing Solves the Problem

1. **Ring-Based Structure**:
   - A ring represents the space of all possible hash values.
   - Servers (nodes) and requests are mapped to positions on this ring using a hash function.
2. **Assignment**:

   - A request is assigned to the first server that is equal to or follows its hash value (clockwise direction).
   - Example:
     - Node 0 at 0°, Node 1 at 120°, Node 2 at 240°.
     - Request at 130° goes to Node 2.

3. **Handling Node Failures**:
   - If a node (e.g., Node 2) goes down, its requests are reassigned to the next available node (Node 0).
   - Other nodes and their assignments remain unaffected, reducing the impact of the failure.

### Mathematical Foundation

1. **Hash Function**:

   - Converts unique identifiers (e.g., IP addresses) into hash values.
   - Ensures uniform distribution of requests across the ring.

2. **Modulo Operation**:
   - Ensures hash values fit within the ring's range (0 to \(M-1\)).
   - Prevents overflow and keeps requests distributed.

## Benefits of Consistent Hashing

- **Minimizes Redistribution**: Only the keys affected by the removed node are reassigned.
- **Efficient Scaling**: Adding or removing nodes impacts minimal requests.
- **Cache Consistency**: Maintains user-to-server mappings, reducing cache misses.
- **Reliability**: Ensures uniform load distribution even with node failures.

## Use Cases

1. **Content Delivery Networks (CDNs)**:
   - Routes users to the same cache server in their region for faster content delivery.
2. **Distributed Databases**:
   - Assigns users to specific servers holding their data, ensuring consistent access.

## Comparison with Other Load Balancing Techniques

- **Round Robin**:
  - Simple and effective when caching is not required.
  - Does not maintain user-to-server consistency.
- **Consistent Hashing**:
  - Preferred when caching or data locality is critical.
  - Provides a stable mapping of requests to servers.

## Key Takeaways

- Consistent hashing ensures efficient and predictable routing, especially in systems with dynamic server availability.
- It complements other load-balancing strategies like round robin, depending on the system’s caching and scalability needs.
