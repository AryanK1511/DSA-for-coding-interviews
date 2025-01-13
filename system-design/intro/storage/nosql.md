# NoSQL Databases

- **NoSQL** (Not Only SQL) databases differ from SQL databases in structure, flexibility, and scalability.
- **Key Features**:
  - Do not use tables; data is stored in various flexible formats.
  - Designed for **horizontal scaling**, handling large-scale, high-speed workloads.
  - Suitable for distributed architectures across multiple nodes.

## Types of NoSQL Databases

### 1. Key-Value Databases

- **Structure**: Data is stored as key-value pairs, similar to hashmaps.
- **Example**:

  ```plaintext
  Key: 'user:123'
  Value: {name=John Doe, age=30, email=johndoe@example.com}
  ```

- **Use Cases**:
  - Caching.
  - Session storage.
- **Example Database**: **Redis** (in-memory storage for fast access).

### 2. Document Databases

- **Structure**: Data stored as documents (e.g., JSON-like objects).
- **Example**:

  ```json
  {
    "id": 1,
    "name": "John Doe",
    "contacts": [{ "type": "email", "value": "john@example.com" }]
  }
  ```

- **Use Cases**:
  - Applications requiring schema flexibility.
  - Content management systems.
- **Example Database**: **MongoDB**.

### 3. Wide-Column Databases

- **Structure**: Data stored in columns instead of rows, optimized for large-scale data and time-series workloads.
- **Example**:

  ```plaintext
  Row Key: location1
  Columns:
    Timestamp1: Temperature1
    Timestamp2: Temperature2
  ```

- **Use Cases**:
  - Analytical workloads.
  - Large-scale, time-series applications.
- **Example Databases**: **Cassandra**, **Bigtable**.

### 4. Graph Databases

- **Structure**: Data stored as nodes (entities) connected by edges (relationships).
- **Example**: Social networks (e.g., Facebook).
  - **Nodes**: Users, posts.
  - **Edges**: Likes, comments, friendships.
- **Use Cases**:
  - Applications requiring complex relationship modeling.
  - Fraud detection, recommendation systems.
- **Example Database**: **Neo4j**.

## Why NoSQL?

### 1. Scalability

- **Horizontal Scaling**: Data is distributed across multiple nodes, improving performance for large datasets.
- Unlike SQL databases, NoSQL databases can store data on servers in different locations without cross-referencing.

### 2. Schema Flexibility

- No predefined schema; supports dynamic and complex data structures.

### 3. Distributed Architecture

- Built to handle large-scale workloads across multiple nodes with fault tolerance and high availability.

## BASE vs. ACID

### ACID (SQL)

- Ensures strict **Consistency** and reliability in transactions.

### BASE (NoSQL)

- **Basically Available**: System is highly available.
- **Soft State**: Data state can change over time.
- **Eventual Consistency**: Data across nodes eventually becomes consistent. The opposite of this where data is instantly available on all nodes is called strong consistency.

## Eventual Consistency

- Updates occur on a **leader node** (primary) and are eventually propagated to **follower nodes**.
- Benefits:
  - High availability.
  - Scalability for large distributed systems.
- Tradeoff:
  - Users may encounter stale data temporarily (e.g., delayed follower counts in social media).
- **Strict Consistency**:
  - Ensures all nodes have updated data at all times, sacrificing speed for accuracy.

## Use Cases for NoSQL

1. **Social Media**: Real-time, highly scalable systems.
2. **E-commerce**: Product catalogs, dynamic pricing.
3. **IoT**: Storing time-series data from sensors.
4. **Content Delivery**: Serving dynamic and schema-less content.

## Key Takeaways

- NoSQL databases offer **flexibility**, **scalability**, and are well-suited for distributed systems.
- Types of NoSQL databases (Key-Value, Document, Wide-Column, Graph) cater to specific use cases.
- **BASE** and **eventual consistency** prioritize high availability over strict transaction guarantees, making NoSQL databases ideal for modern, large-scale applications.
