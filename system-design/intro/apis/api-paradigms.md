# API Paradigms

- An **Application Programming Interface (API)** is a set of rules and protocols for building and interacting with software applications.
- APIs allow clients and servers to communicate over a network.

## Three Popular API Paradigms

### 1. REST (Representational State Transfer)

- **Overview**:

  - Architectural style that uses HTTP for communication.
  - Stateless: Each request contains all required information; the server doesn't remember past interactions.
  - Relies heavily on JSON for data exchange.

- **Advantages**:

  - Simple and widely supported.
  - Independent development of client and server.

- **Challenges**:

  - Over-fetching: Receiving unnecessary data (e.g., extra fields in user profiles).
  - Under-fetching: Requiring multiple requests to get all needed data.
  - Less efficient for complex or real-time scenarios.

- **Example**:

  - URL for paginated video requests:
    - `https://youtube.com/videos?offset=0&limit=10`

### 2. GraphQL

- **Overview**:

  - Solves over-fetching and under-fetching issues in REST.
  - Allows clients to request only the data they need in a single query.
  - Operates via a single endpoint, typically over HTTP POST.

- **Key Features**:

  - **Queries**: Retrieve data.
  - **Mutations**: Modify data.
  - Flexible and efficient data fetching.

- **Example**:

  - SpaceX API query:

  ```graphql
  {
    launchesPast(limit: 10) {
      mission_name
      launch_date_local
      links {
        article_link
      }
    }
  }
  ```

  - Response provides only requested fields in JSON format.

### 3. gRPC (Google Remote Procedure Call)

- **Overview**:

  - Framework for executing Remote Procedure Calls (RPCs).
  - Built on HTTP/2 for fast, bi-directional communication using **protocol buffers** (Protobuf).
  - Commonly used for **server-to-server communication**.

- **Advantages**:

  - Faster and more compact than JSON due to Protobuf.
  - Supports streaming data from client to server and vice versa.

- **Example**:

  - Define request and response schemas in `.proto` files:

    ```proto
    syntax = "proto3";

    service Greeter {
      rpc SayHello (HelloRequest) returns (HelloReply);
    }

    message HelloRequest {
      string name = 1;
    }

    message HelloReply {
      string message = 1;
    }
    ```

  - The `.proto` file generates language-specific classes for easy API interaction.

- **Limitations**:
  - Requires custom error handling (doesn't rely on HTTP status codes).

## Key Differences Between Paradigms

- **REST**: Simple and widely supported, but can be inefficient for complex queries.
- **GraphQL**: Optimized for flexible data fetching, ideal for client-driven applications.
- **gRPC**: High-performance, compact, and ideal for server-to-server or streaming communication.
