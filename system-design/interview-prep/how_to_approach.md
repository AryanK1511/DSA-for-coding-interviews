# How to Approach System Design Interviews

In system design interviews, you're typically given an open-ended problem where you're asked to design a part of a larger system. The goal is to evaluate your ability to think through complex system architectures, consider various trade-offs, and build a robust solution.

## 1. Clarify the Problem

- **Understand the scope**: Confirm what exactly the interviewer wants you to design. It's common to be asked to design only a small part of a much larger system.
- **Ask clarifying questions**: Inquire about any assumptions or constraints to ensure you are aligned with the interviewer's expectations. This could involve understanding the scale of the system or specific requirements that need to be prioritized.

## 2. Functional Requirements

These are the **core features** that the system must have:

- What does the system need to **do**?
- What are the main use cases and user interactions?
- Think in terms of **CRUD** operations (Create, Read, Update, Delete).

## 3. Non-Functional Requirements

These describe the **qualities** of the system that are not related to its core functionality:

- **Scalability**: How will the system handle growth (e.g., scaling to 100M users)?
- **Throughput**: What is the expected rate of requests/operations per second?
- **Storage Capacity**: How much data should the system be able to store?
- **Performance**: How fast should the system be? E.g., latency, request processing speed.
  - **Latency**: How long should the system take to respond to requests?
  - Example: You may optimize for fast reads but allow slower writes.
- **Availability**: How reliable is the system? What is the expected uptime?
  - This typically involves understanding how to handle **failures** gracefully (e.g., non-error responses, handling downtime).

## 4. Design Trade-Offs

- **Avoid overengineering**: Aim for a simple yet scalable solution.
- **Make intelligent trade-offs**: You may need to decide between different approaches (e.g., between using a NoSQL vs. SQL database based on scalability vs. data consistency).

  Example:

  - **Twitter**: With 100M active users, the platform might have:
    - 100 tweets per user per day
    - 10 million writes per day
    - 10 billion reads per day
    - **Throughput**: 10 billion reads / 86,400 seconds per day = 115,740 reads per second.

## 5. Back-of-the-Envelope Calculations

- Perform rough calculations to validate your approach. For instance:
  - Estimate the amount of traffic your system will handle.
  - How many requests per second does your architecture need to support?
  - Calculate the required storage capacity based on the volume of data.

## 6. Tools and Resources

- Be aware of latency benchmarks and industry best practices:
  - **Latency numbers**: Review latency research like this [Interactive Latency page](https://colin-scott.github.io/personal_website/research/interactive_latency.html) to understand practical expectations for response times in large-scale systems.
