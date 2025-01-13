# CAP Theorem and PACELC Extension

The **CAP theorem** states that in a distributed system, it is impossible to simultaneously guarantee all three of the following properties:

1. **Consistency**: Ensures all nodes have the same data at any given time. Every read reflects the most recent write.
2. **Availability**: Guarantees that every request receives a response, regardless of success or failure.
3. **Partition Tolerance**: The system continues to function despite communication breakdowns between nodes.

In practice, distributed systems must always tolerate partitions (P). Therefore, a system can only prioritize **Consistency (C)** or **Availability (A)** during a partition.

## 1. Partition Tolerance

- A system can handle node communication failures without crashing.
- Example: A network partition prevents a leader from updating a follower.

## 2. Consistency (in CAP)

- Guarantees data uniformity across all nodes.
- Example:
  - In a banking system, the account balance must be consistent across all nodes.
  - Writes to the leader are blocked if the follower cannot update.

## 3. Availability

- Ensures all valid requests receive a response, even during failures.
- Example:
  - A learning management system (LMS) must accept assignment submissions even if grades are delayed due to inconsistent replicas.

## Choosing Between Consistency and Availability

### Consistency > Availability (CP Systems)

- Prioritize data correctness over responsiveness.
- Use Case: Banking, healthcare, and critical systems requiring precise data.
- Tradeoff: Requests may fail or be delayed during partitions.

### Availability > Consistency (AP Systems)

- Prioritize system responsiveness over data consistency.
- Use Case: Social media platforms, content delivery, and systems tolerant of stale data.
- Tradeoff: Clients may read outdated data temporarily.

## PACELC Theorem

- An extension of CAP that considers system behavior **without partitions**.
- States:
  - **P** (Partition): Choose between **A** (Availability) or **C** (Consistency).
  - **ELC** (Else): Choose between **L** (Latency) or **C** (Consistency) when no partition exists.
- **Example**:
  - A CDN might prioritize low latency over consistency (ELC).
  - A database might prioritize consistency over latency for precise data (ELC).

## Comparison of Consistency in CAP vs. ACID

- **Consistency (CAP)**: Ensures all nodes have the same, most up-to-date data in a distributed system.
- **Consistency (ACID)**: Maintains the integrity of transactions within a database, ensuring no rules or constraints are violated.

## Trade-offs in System Design

1. **CP Systems**:
   - Prioritize correctness during partitions.
   - May sacrifice uptime (availability).
   - Example: Distributed databases in financial systems.
2. **AP Systems**:
   - Prioritize uptime during partitions.
   - May serve stale or inconsistent data.
   - Example: E-commerce during high traffic (serving cached inventory).

## Key Takeaways

- The **CAP theorem** emphasizes unavoidable trade-offs in distributed systems.
- The **PACELC theorem** extends this understanding by factoring latency in partition-free scenarios.
- Designing a system requires balancing these trade-offs based on application requirements:
  - **Consistency** for accuracy-critical systems.
  - **Availability** for responsiveness and fault tolerance.
