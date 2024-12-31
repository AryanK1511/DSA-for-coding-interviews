# Domain Name System (DNS)

- **Definition:** DNS functions as the internet's phone book, translating human-readable domain names into numerical IP addresses.
  - Example: _google.com → 142.251.211.238_
- **Purpose:** Enables computers to route requests to the correct internet servers.

## Key Concepts

1. **ICANN (Internet Corporation for Assigned Names and Numbers):**

   - Governs the coordination, security, and operation of DNS.
   - Does not directly sell domains but certifies domain registrars to handle domain registration.

2. **Domain Registrars:**

   - Act as intermediaries certified by ICANN to sell domain names (e.g., GoDaddy, Google Domains).
   - Maintain domain registration records.

3. **DNS Records:**

   - **A Record:** Maps a domain to an IPv4 address (e.g., _neetcode.io → 192.158.1.39_).
   - Cached IP addresses improve response time for subsequent requests if the server has a static IP.

4. **Server Configuration:**
   - Servers have public IPs, are configured with firewalls, and respond to client requests via DNS mappings.

## Anatomy of a URL (Uniform Resource Locator)

- A URL specifies the location of a resource and the protocol for accessing it.
  **Example URL: `https://domains.google.com/get-started`**

1. **Protocol (Scheme):**

   - _https://_ indicates the use of HTTPS for secure communication.
   - Other examples:
     - FTP: _ftp://ftp.example.com/pub/file.txt_
     - SSH: _ssh://username@example.com:22_

2. **Domain Name:**

   - Divided into:
     - **Subdomain:** _domains_ → Represents a distinct section within the primary domain.
     - **Primary Domain:** _google.com_ → The main identifier, owned via a registrar.
     - **Top-Level Domain (TLD):** _.com_ → Indicates the domain’s category (e.g., _.com_ for commercial sites, _.io_ for tech companies).

3. **Path:**

   - _get-started_ → Specifies a particular resource or section within the domain.

4. **Port:**
   - Default ports:
     - HTTP → Port 80
     - HTTPS → Port 443
   - Example of a custom port: _localhost:8080_.

## Closing Notes

- **DNS:** Vital for routing and server connectivity.
- **URL Anatomy:** A foundational aspect for understanding system design and resource navigation.
- Further exploration into DNS records, protocols, and URL components can deepen understanding for system design and web development contexts.
