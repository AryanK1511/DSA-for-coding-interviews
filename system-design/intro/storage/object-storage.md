# Object Storage

- **Object Storage** treats data as independent objects, each with:
  1. **Data**: The file or content (e.g., image, video).
  2. **Metadata**: Describes the data (e.g., file size, type, or custom tags).
  3. **Unique Identifier**: A globally unique key to locate the object.
- Objects are stored in a **flat address space** (no hierarchical folder structure like file systems), making it highly **scalable**.

## Comparison: Databases vs. Object Storage

| Feature           | Databases                                   | Object Storage                                        |
| ----------------- | ------------------------------------------- | ----------------------------------------------------- |
| **Structure**     | Hierarchical (tables, rows, columns).       | Flat, address-based.                                  |
| **Optimization**  | Suited for transactional data and querying. | Handles large, unstructured data (e.g., media files). |
| **Scalability**   | Limited by schema complexity.               | Easily scalable.                                      |
| **Use Cases**     | Financial records, analytics.               | Images, videos, backups.                              |
| **Access Method** | SQL queries.                                | HTTP requests (e.g., REST APIs).                      |

## Why Use Object Storage?

1. **Optimized for Large Files**:
   - Efficiently stores unstructured data like images, videos, and backups.
   - Avoids performance issues common with relational databases handling large files.
2. **Scalability**:
   - Flat architecture allows easy scaling without the complexities of folder hierarchies.
3. **HTTP Access**:
   - Objects are accessed via HTTP requests directly to the storage system.
   - Example: Amazon S3, Google Cloud Storage.

## When to Use Object Storage

- **Ideal For**:

  - Storing media files, logs, or backups.
  - Applications with infrequent queries for stored data.
  - Systems requiring scalable and cost-effective storage.

- **Not Ideal For**:
  - Complex queries or relational data.
  - Real-time data analytics.

## Examples of Object Storage Systems

1. **Amazon S3** (Simple Storage Service):
   - Widely used in system design for storing and retrieving files.
2. **Google Cloud Storage**:
   - Similar functionality for large-scale, distributed object storage.
3. **Azure Blob Storage**:
   - Microsoft's solution for unstructured data storage.

## Closing Notes

Object storage complements databases by handling unstructured, large-scale files that are cumbersome for traditional RDBMS. In system design:

- Use **SQL/NoSQL databases** for structured, transactional data.
- Use **Object Storage** for media files, backups, and logs, leveraging its scalability and efficiency.
