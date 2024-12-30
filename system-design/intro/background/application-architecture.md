# Application Architecture Notes

This high-level overview explores the architecture of a production-grade application, laying the foundation for more detailed discussions on its components later.

## Components of Application Architecture

### Developer's Perspective

- **Code Deployment**:
  - Developers write code that is deployed to a **server**.
  - A server handles requests from other computers and often requires persistent storage for application data.
  - **External Storage**: Servers may connect to external systems like databases or cloud storage via a network.

### User's Perspective

- **Client Requests**:
  - Users interact with the server through web browsers (clients).
  - The server responds with front-end assets (JavaScript, HTML, CSS) to display user-requested features.

## Scaling Servers

### Vertical Scaling

- Upgrading components within a single server, such as:
  - Increasing RAM.
  - Using a faster CPU.
- **Limitations**:
  - Physical constraints on the upgrades a single server can handle.

### Horizontal Scaling

- Adding multiple servers to distribute user requests:
  - **Benefits**:
    - Improves performance by avoiding bottlenecks in RAM or CPU.
    - Enhances fault tolerance; traffic can be redirected if one server fails.
  - **Challenges**:
    - Requires ensuring server communication and even distribution of requests.
- **Load Balancers**:
  - Distributes incoming requests evenly among multiple servers.

### Choosing Scaling Options

- **Simple Applications**:
  - Vertical scaling may suffice.
- **Complex Applications**:
  - Horizontal scaling with commodity hardware is preferred, despite higher engineering effort.

## Interacting with External Servers

- Servers often interact with third-party services via APIs.
  - Example: A website using Stripe for payments.

## Logging and Metrics

### Logging Services

- Logs capture server activity, errors, and events before crashes.
- **Recommendation**:
  - Store logs on external servers for better reliability.

### Metrics Services

- Collects data like CPU usage and network traffic to identify bottlenecks.
- Complements logs by offering insights into server behavior.

## Alerts

- Developers set **alerts** for unexpected metrics behavior:
  - Example: If successful request rates drop below 95%.
- Notifications are sent to developers, avoiding the need for constant manual monitoring.
