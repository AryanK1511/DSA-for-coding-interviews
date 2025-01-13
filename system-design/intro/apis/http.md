# HTTP (Hypertext Transfer Protocol)

- HTTP is a foundational protocol for web communication, built on top of IP and TCP.
- It is a request/response protocol, defining how data is formatted and transmitted between clients (e.g., browsers) and servers.

## Client-Server Model

- The client initiates requests, while the server responds with resources or services.
- Roles can interchange; e.g., Google acts as a client when requesting third-party data.
- Peer-to-peer networks blur the client-server distinction, as machines act as both.

## Remote Procedure Calls (RPC)

- RPC allows programs to execute functions on remote servers as if they were local.
- For example, searching "NeetCode" on YouTube calls a server-side function to retrieve video data.

## HTTP Anatomy

- **Request Components:**
  - **Method**: Actions like GET, POST, PUT, DELETE.
  - **URL/URI**: Specifies resource location and parameters.
  - **Headers**: Provide metadata (e.g., accepted content types, cookies).
  - **Body**: Data payload (for POST/PUT). DELETE does not have a payload since the best practice suggests sending the ID in the URL as a part of the route.
- **Response Components:**
  - Status codes (e.g., 200 OK, 404 Not Found) indicate request outcomes.
  - Headers define response details (e.g., content type, caching).

## HTTP Methods

1. **GET**: Retrieve resources (idempotent).
2. **POST**: Create new resources (not idempotent).
3. **PUT**: Update resources (idempotent).
4. **DELETE**: Remove resources (idempotent).

> **Note:** Idempotence means that making multiple identical requests to an endpoint results in the same effect on the server and the same response as making the request only once

## HTTP Status Codes

- **100-199**: Informational (e.g., 100 Continue).
- **200-299**: Success (e.g., 200 OK, 201 Created).
- **300-399**: Redirection (e.g., 301 Moved Permanently).
- **400-499**: Client errors (e.g., 400 Bad Request, 401 Unauthorized).
- **500-599**: Server errors (e.g., 500 Internal Server Error).

## Secure Communication (SSL/TLS)

- SSL: Secure Sockets Layer is an older protocol that has some security flaws.
- TLS: Transport Layer Security is a more modern and secure version of SSL that fixes some of its vulnerabilities.
- HTTPS combines HTTP with TLS for secure communication, protecting against man-in-the-middle attacks.
- TLS encrypts data to ensure confidentiality and integrity.
- Although "SSL" is often mentioned, it is an outdated predecessor of TLS.

## Key Takeaways

- HTTP is a core protocol for web communication.
- HTTPS (HTTP + TLS) is the standard for secure interactions, essential for modern system design. This essentially just encrypts the data that the client sends to the server and vice versa.
