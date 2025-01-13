# Caching

- Caching involves creating **copies of data** to enable faster access.
- Common in single machines (e.g., CPU cache) and distributed systems.
- Tradeoff: **Speed vs. Capacity**:
  - Cache is faster but smaller than RAM or disk.
  - Thoughtful management is required to store frequently accessed or critical data.

## How Caching Works

1. **Client Perspective**:

   - **Steps to load a resource**:
     - Check **memory cache** (fast, non-persistent).
     - Check **disk cache** (slower but persistent).
     - Make a **network request** (slowest).
   - **Cache Hit**: Data is found in the cache.
   - **Cache Miss**: Data is not in the cache, requiring a network or disk request.
   - **Cache Hit Ratio**:
     $$
     \text{Cache Hit Ratio} = \frac{\text{Cache Hits}}{\text{Cache Hits + Cache Misses}} \times 100
     $$

2. **Server Perspective**:
   - Servers decide what to cache based on access frequency.
   - Example: Viral tweets are cached because they are frequently accessed.

## Caching Modes

1. **Write-Around Cache**:

   - New data is written to disk, not cache.
   - Cached only when accessed for the first time.
   - Saves cache space but may cause a delay for initial popular data access.

2. **Write-Through Cache**:

   - Writes to both cache and disk simultaneously.
   - Ensures data consistency but increases memory load.
   - Suitable for frequently accessed data.

3. **Write-Back Cache**:
   - Writes to cache first, defers writing to disk.
   - Disk is updated only when the cache is full or during idle periods.
   - Reduces write load but risks data loss if the cache fails.

## Eviction Policies

When the cache is full, the system must remove items to make space for new data. Common policies include:

1. **FIFO (First In, First Out)**:

   - Evicts the oldest cached item.
   - Simple but may not prioritize the most relevant data.

2. **LRU (Least Recently Used)**:

   - Removes the least recently accessed item.
   - Ideal for data with temporal relevance (e.g., popular tweets).

3. **LFU (Least Frequently Used)**
   - Removes the item with the lowest access frequency.
   - Tracks the number of times each item is accessed.
   - Items accessed infrequently are evicted first, regardless of when they were last accessed.

## Real-Life Example: Browser Caching

- Browsers cache static files (e.g., JavaScript, images) to improve page load times.
- Cached files are stored on disk, reducing the need for repetitive network requests.
- Example: A static JavaScript file from `neetcode.io` is cached to reduce load time from 123 ms (network) to 11 ms (disk).

## Importance of Caching

- Reduces **latency** and improves **user experience**.
- Enhances **system scalability** by minimizing repeated resource requests.
- Essential for high-traffic systems like **social media platforms** or **content delivery networks (CDNs)**.

## Key Takeaways

1. **Caching saves time and resources** by storing frequently accessed data closer to the user or process.
2. Proper **cache management and eviction policies** are crucial to balance speed and capacity.
3. Implementing caching efficiently improves **system performance** and **user experience**, especially in large-scale systems.
