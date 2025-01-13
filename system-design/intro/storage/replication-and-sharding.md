# Replication and Sharding in Distributed Systems

## Replication

**Replication** involves creating copies of a database (replicas) to improve:

- **Availability**: Ensures uptime even if the primary database fails.
- **Scalability**: Distributes read requests across replicas.
- **Durability**: Keeps data safe and available during failures.

### Types of Replication

1. **Synchronous Replication**:

   - **Process**: Every write is immediately replicated to followers.
   - **Advantages**:
     - Guarantees data consistency across replicas.
     - Followers can take over seamlessly if the leader fails.
   - **Disadvantages**:
     - Higher latency as leader waits for replication acknowledgment.

2. **Asynchronous Replication**:

   - **Process**: The leader sends updates to followers without waiting for acknowledgment.
   - **Advantages**:
     - Lower latency and higher write throughput.
   - **Disadvantages**:
     - Followers may temporarily serve stale data.

3. **Master-Master (Multi-Master) Replication**:
   - **Process**: Multiple leaders handle writes and replicate data between each other.
   - **Advantages**:
     - Distributes traffic geographically for low latency.
   - **Disadvantages**:
     - Synchronization latency between leaders can cause inconsistencies.

> **Note:** A convention is that we only allow users to read/write from the leader. Users only have read access to the followers and no write access.

## Sharding

**Sharding** involves splitting a database into smaller, more manageable **shards**, each hosted on a different server. Each shard contains a subset of the data, improving performance and scalability.

### Shard Key

- A **shard key** determines how data is partitioned.
- Common strategies:
  1. **Range-Based Sharding**:
     - Splits data based on a range of values (e.g., rows 1–25 in Shard A, 26–50 in Shard B).
  2. **Hash-Based Sharding**:
     - Uses a hash function to distribute data uniformly across shards.
     - Example: Consistent hashing minimizes data movement during rebalancing.

### Replication vs. Sharding

| **Feature**     | **Replication**                              | **Sharding**                                 |
| --------------- | -------------------------------------------- | -------------------------------------------- |
| **Purpose**     | Data redundancy and availability             | Distributes data and load across servers     |
| **Data Copy**   | Full copy of the database on each replica    | Subset of data on each shard                 |
| **Scaling**     | Improves read scalability                    | Improves read and write scalability          |
| **Consistency** | High (especially in synchronous replication) | More complex (eventual consistency in NoSQL) |

### Challenges with Sharding

1. **Complexity**:

   - Ensuring related data resides in the same shard can be challenging.
   - Shard key selection is critical for even distribution and performance.

2. **Relational Database Constraints**:

   - Relational databases (SQL) are not designed for horizontal scaling.
   - Developers must implement custom sharding logic at the application level.

3. **ACID Compliance**:

   - Maintaining atomicity and consistency across shards is difficult.
   - NoSQL databases trade strict consistency for eventual consistency, simplifying sharding.

### Eventual Consistency

- Ensures that replicas converge to the same state over time.
- Benefits:
  - Higher availability and fault tolerance.
  - Faster write operations.
- Tradeoff:
  - Clients may see outdated data temporarily.

## Use Cases

1. **Replication**:

   - **Read-Heavy Workloads**: Distribute reads across replicas (e.g., search engines).
   - **High Availability**: Critical systems requiring 24/7 uptime (e.g., financial systems).

2. **Sharding**:
   - **Write-Heavy Workloads**: Handle massive datasets (e.g., social media platforms).
   - **Scalable Systems**: Distribute users and data geographically (e.g., global e-commerce).

## Key Takeaways

1. **Replication** improves availability and durability but is limited in write scalability.
2. **Sharding** enables horizontal scaling by distributing data but adds complexity.
3. **Consistent Hashing** can optimize shard allocation and rebalancing.
4. NoSQL databases are better suited for sharding due to their design for distributed systems and eventual consistency.
