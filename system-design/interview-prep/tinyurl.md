# Designing TinyURL

Create a system that converts long URLs into shorter, user-friendly URLs and allows users to be redirected to the original long URL when they use the short URL.

## Key Requirements

1. Short URLs should:
   - Be 8 characters long.
   - Be unique for each user, even if the original long URL is the same (to handle different expiration times).
   - Allow users to specify custom expiration times.
2. Provide high availability, fault tolerance, and minimal latency.
3. Scale to handle billions of URLs efficiently.
4. Expired URLs should be cleaned up periodically to free up space and allow reuse of keys.

## Non-Functional Requirements

1. **Scalability**: The system must handle:
   - ~400 writes/sec (URL generation requests).
   - ~30,000 reads/sec (redirection requests).
2. **Efficiency**: Minimize latency for both URL generation and redirection.
3. **Storage**: Efficiently store both short and long URLs, handling ~1 TB of data per month.
4. **Fault Tolerance**: Ensure system reliability even if parts of the system fail.
5. **Caching**: Implement caching to speed up frequent redirection queries.
6. **ACID Compliance**: Ensure unique short URLs using atomic transactions to avoid collisions.

## High-Level Design

### Components

1. **Client/User Interface**: Interface where users input the long URL and receive the short URL.
2. **URL Generator Service**: Responsible for generating unique short URLs.
3. **Database**: Stores mappings between short and long URLs, along with metadata (e.g., expiration time).
4. **Cache**: Speeds up redirection by storing frequently accessed short-to-long URL mappings.
5. **Cleanup Service**: Periodically deletes expired URLs and marks associated keys as reusable.
6. **Load Balancer**: Distributes incoming traffic across multiple servers.
7. **Web Server**: Handles URL generation and redirection requests.

### Flow

1. **URL Shortening**:

   - User provides a long URL (and optionally an expiration time).
   - Request hits the load balancer, which routes it to one of the web servers.
   - Web server interacts with the URL generator service to create a unique short URL.
   - The mapping (short URL → long URL + metadata) is stored in the database.
   - The short URL is returned to the user.

2. **URL Redirection**:

   - User clicks on a short URL.
   - Request is routed to the web server via the load balancer.
   - Web server checks the cache for the short URL.
     - If found, retrieves the long URL and redirects the user (301 or 302 status code).
     - If not found, queries the database, updates the cache, and redirects the user.

3. **Cleanup**:
   - Periodically identifies expired URLs in the database.
   - Marks their keys as reusable and deletes their entries from the database and cache.

## Core Components

### 1. URL Generator

- Generates 8-character unique short URLs.
- **Characters Used**: [a-zA-Z0-9] → 62 possible characters.
- **Keyspace**: \( 62^8 = 218,340,105,584,896 \) (218 trillion combinations).
- **Collision Handling**:
  - Use a SQL database for atomicity to ensure no duplicate keys.
  - If a collision occurs (rare but possible), retry with a different key.

### 2. Database

- **Type**: SQL database (ACID compliance ensures no duplicate short URLs).
- **Schema**:

  ```plaintext
  Table: URLs
  - id (Primary Key)
  - short_url (Unique, Indexed)
  - long_url
  - expiration_time (Timestamp)
  - created_at (Timestamp)
  ```

- **Query Examples**:
  - Write: `INSERT INTO URLs (short_url, long_url, expiration_time) VALUES (?, ?, ?)`.
  - Read: `SELECT long_url FROM URLs WHERE short_url = ?`.
  - Cleanup: `DELETE FROM URLs WHERE expiration_time < NOW()`.

### 3. Caching

- **Purpose**: Reduce latency for redirection requests by storing frequently accessed mappings.
- **Type**: In-memory cache (e.g., Redis, Memcached).
- **Cache Policy**:
  - Use **LRU (Least Recently Used)** eviction since:
    - Redirection patterns often favor recently created or popular URLs.
- **Capacity**: ~256 GB (enough to hold mappings for billions of URLs).
- **Key-Value Pair**:
  - **Key**: Short URL.
  - **Value**: Long URL.

### 4. Cleanup Service

- Runs periodically (e.g., every hour).
- Deletes expired URLs from the database.
- Marks keys of expired URLs as reusable.

### Scaling

#### 1. Horizontal Scaling

- **Load Balancer**: Distributes traffic across multiple servers.
- **Server Replication**: Deploy multiple web servers to handle high traffic.

#### 2. Database Scaling

- **Read-Heavy Workload**:
  - Add read replicas to handle increased read traffic.
  - Use consistent hashing to partition data across multiple database instances.
- **Sharding**:
  - Partition URLs based on hash of the short URL.

#### 3. Cache Scaling

- Use a distributed cache like Redis Cluster to spread load across nodes.
- Apply consistent hashing to ensure even key distribution.

## Detailed Considerations

### Expiration Handling

- URLs expire based on user-defined or default expiration times (e.g., 1 year).
- Cleanup service ensures expired URLs are removed:
  - Removes the entry from the database.
  - Marks the short URL key as reusable.
  - Deletes the entry from the cache.

### Redirection Status Codes

- **301 (Permanent Redirect)**:
  - Indicates the resource has permanently moved.
  - Allows browsers to cache the redirection.
- **302 (Temporary Redirect)**:
  - Indicates the redirection is temporary.
  - Ensures browsers always check with the TinyURL server for the latest redirection.

### Fault Tolerance

- **Database Failures**:
  - Use replication and failover mechanisms.
- **Cache Failures**:
  - Fallback to querying the database if the cache is unavailable.

## Trade-offs

### SQL vs. NoSQL

- SQL is chosen for its ACID properties, ensuring unique short URLs and handling concurrent writes.
- NoSQL (e.g., DynamoDB) can be considered if scalability becomes a bottleneck.

### Pre-generated vs. On-Demand Keys

- Pre-generating all keys reduces the need for runtime key generation but increases initial storage requirements.
- On-demand generation is more dynamic but risks collisions (mitigated with retries).
