# Designing a Rate Limiter

A **rate limiter** is a mechanism to control the number of requests a user or client can make to a system within a specified timeframe. It prevents abuse of resources by enforcing usage limits and protects the backend services from overload. If the rate limit is exceeded, the system returns an HTTP status code `429 Too Many Requests` along with an error message explaining the issue.

## Why Not Client-Side Enforcement?

Rate limiting cannot be reliably implemented on the client side because:

1. **Bypassing is trivial:** A user can use tools like `curl` or a custom script to make direct requests to the server, bypassing client-side checks.
2. **Inconsistent enforcement:** Different client platforms may not enforce the rules uniformly.

Instead, the rate limiter must operate server-side, ideally as a **reverse proxy** that sits in front of the API servers, handling request validation before forwarding them.

## Key Design Requirements

### Functional Requirements

1. Limit the number of API requests a user can make within a specific timeframe.
2. Enforce rules based on:
   - User identity (e.g., User ID, API Key).
   - IP address if the user is unauthenticated.
3. Return a `429 Too Many Requests` status code and a descriptive error message when the limit is exceeded.
4. Support different rate-limiting rules for different endpoints (e.g., stricter limits for expensive operations).
5. Ensure high availability and fault tolerance of the rate limiter.

### Non-Functional Requirements

1. **Low Latency:** The rate limiter should introduce minimal overhead to request processing.
2. **High Throughput:** It must handle large volumes of traffic efficiently.
3. **Scalability:** The system should scale horizontally to handle increases in users and traffic.
4. **Fail-Open Behavior:** If the rate limiter fails, it should allow requests to pass through instead of blocking them. This ensures that critical services are not disrupted. You can either Fail open or Fail close. Fail Close would mean that everything stops working when the rate limiter goes down vs Fail Open where everything except fro your rate limited would still work.

## High-Level Design

1. A client makes a request to the API.
2. The request first hits the **Rate Limiter**, acting as a **reverse proxy**.
3. The Rate Limiter:
   - Checks if the user is within the allowed rate limits.
   - Forwards the request to the appropriate API server if the limit is not exceeded.
   - Returns a `429 Too Many Requests` error if the limit is exceeded.

### Components

1. **Rate Limiter Service:**
   - Acts as the entry point for all incoming requests.
   - Tracks request counts and enforces rate-limiting rules.
2. **In-Memory Store:**
   - Stores request counts for users (e.g., Redis, Memcached).
   - Allows fast reads/writes for tracking request rates.
3. **Rules Database:**
   - Stores rate-limiting rules for different APIs.
   - Defines limits like requests per time unit, operation type, and endpoint.
4. **Cache Layer:**
   - Speeds up rule lookups by caching rules from the database.
5. **API Gateway:**
   - Handles actual API requests and communicates with backend servers.

### Rate Limiting Algorithms

#### 1. Fixed Window Counter

- Simplest approach.
- **How it works:**
  - Track the number of requests made by a user in the current time window (e.g., 1 minute).
  - Allow or reject requests based on this count.
- **Pros:**
  - Easy to implement and understand.
  - Efficient storage using a key-value store with an expiration (e.g., Redis `EXPIRE`).
- **Cons:**
  - Burst traffic near the boundary of two time windows can exceed the limit (e.g., 100 requests at the end of one minute + 100 at the start of the next).

#### 2. Sliding Window Log

- Tracks all requests with timestamps.
- **How it works:**
  - Store timestamps of each request in a sorted data structure (e.g., Redis Sorted Sets).
  - Continuously calculate the number of requests in the last `N` seconds by removing expired timestamps.
- **Pros:**
  - Handles burst traffic more effectively than Fixed Window.
- **Cons:**
  - Higher storage overhead since all request timestamps are stored.
  - Slightly more complex implementation.

#### 3. Token Bucket

- Allows bursts of traffic while enforcing an average rate over time.
- **How it works:**
  - Tokens are added to a bucket at a constant rate.
  - A request consumes one token. If the bucket is empty, the request is denied.
- **Pros:**
  - Flexible and efficient for rate limiting.
  - Can handle temporary bursts without exceeding limits over time.
- **Cons:**
  - Requires periodic token replenishment logic.

### Data Storage Design

#### In-Memory Key-Value Store

1. **Schema for Tracking Requests:**
   - **Key:** Combination of user identifier (User ID, IP Address) and API endpoint.
   - **Value:** Request count (integer) or timestamps (list for sliding window).
2. **Rule Storage:**
   - **Key:** Rule ID.
   - **Value:** JSON-like structure containing:
     - API endpoint.
     - Request limit (e.g., 100 requests).
     - Time unit (e.g., 1 minute).

#### Scaling the KV Store

- Use **sharding** to distribute keys across multiple nodes.
- Apply **consistent hashing** to ensure keys are evenly distributed, even as nodes are added or removed.

## Scaling the System

1. **Horizontal Scaling:**

   - Deploy multiple instances of the rate limiter behind a load balancer.
   - Ensure shared state across instances using a distributed store (e.g., Redis Cluster).

2. **Database Optimization:**

   - Cache rules in memory to reduce database reads.
   - Use workers to asynchronously update the cache when rules are added/modified.

3. **Latency Minimization:**
   - Co-locate the rate limiter with backend services to reduce network latency.
   - Use connection pooling and efficient data structures (e.g., hashes, sorted sets).

## Trade-offs

1. **Accuracy vs. Performance:**

   - Sliding Window Log provides better accuracy but requires more storage and computation.
   - Fixed Window is simpler but less precise during bursts.

2. **Fail-Open vs. Fail-Closed:**
   - Fail-Open ensures service availability but risks abuse.
   - Fail-Closed prioritizes security but risks service unavailability.
