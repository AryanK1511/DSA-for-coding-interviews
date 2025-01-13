# SQL (Structured Query Language) Databases

- **SQL Databases**, or **Relational Database Management Systems (RDBMS)**, store data in tables with well-defined fields, enabling efficient data storage and retrieval.
- Data is organized in rows (records) and columns (fields), each uniquely identified by a **primary key**.

## 1. Data Storage and B+ Trees

- SQL databases use **B+ Trees** for efficient querying and indexing.
  - **Multi-way tree**: Nodes can have more than two children.
  - **Leaf nodes**: Contain all data and are linked in sorted order for quick range queries.
- **Indexing**:
  - Improves query speed by creating a structure to quickly locate data.
  - Example: An index on the "Name" column allows faster retrieval of phone numbers in a "People" table.

## 2. SQL Tables

- Tables define the structure for storing data, specifying data types and constraints.
- Example:

  ```sql
  CREATE TABLE People (
      PhoneNumber INT PRIMARY KEY,
      Name VARCHAR(100)
  );
  CREATE TABLE Homes (
      PhoneNumber INT,
      Address VARCHAR(255),
      FOREIGN KEY (PhoneNumber) REFERENCES People(PhoneNumber)
  );
  ```

- **Primary Key**: Uniquely identifies rows.
- **Foreign Key**: Ensures referential integrity by linking rows between tables.

## 3. JOINS

- Joins combine data from multiple tables based on a related column.
- Example: Retrieve names and addresses using a join on `PhoneNumber`:

  ```sql
  SELECT People.Name, Homes.Address
  FROM People
  JOIN Homes ON People.PhoneNumber = Homes.PhoneNumber;
  ```

## ACID Properties

SQL databases ensure reliable and predictable transactions through **ACID**:

### Atomicity

- Transactions are all-or-nothing.
- Example: Transferring $500 from Alice to Bob:
  - Deduct $500 from Alice.
  - Add $500 to Bob.
  - If any step fails, the transaction is rolled back.

### Consistency

- Transactions maintain data integrity and follow defined rules.
- Example: A rule ensuring account balances cannot be negative.

### Isolation

- Concurrent transactions do not interfere with each other.
- Prevents **dirty reads** (reading uncommitted changes).
- Transactions appear serialized, maintaining data accuracy.

### Durability

- Once a transaction commits, changes persist even during system failures.
- Example: A power outage won’t erase a completed bank transfer.

## Trade-offs of RDBMS

1. **Advantages**:

   - Structured schema ensures data consistency.
   - Joins and indexing allow complex queries.
   - ACID properties ensure reliability and predictability.

2. **Challenges**:

   - Performance can degrade with large-scale data and high concurrency.
   - Indexing requires additional storage and write overhead.
   - They are very hard to scale.

## Use Cases

SQL databases excel in applications requiring:

1. **Structured Data**: Banking systems, employee records.
2. **Complex Queries**: Reporting and data analytics.
3. **Strict Consistency**: Financial transactions.
