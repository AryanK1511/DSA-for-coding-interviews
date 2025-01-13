# API Design

API design focuses on creating a clear and reliable interface (or "contract") for developers to interact with a service. A well-designed API ensures ease of use, backward compatibility, and maintainability.

APIs typically provide **CRUD operations** (Create, Read, Update, Delete), performed on resources (e.g., tweets, users) using HTTP methods like **GET**, **POST**, **PUT**, and **DELETE**.

## Key Principles of Good API Design

### 1. Backward Compatibility

- Changes to APIs should not break existing applications.
- Example: Adding a `parentId` parameter for replies in the `createTweet(userId, content)` method should make it **optional** to maintain compatibility with older applications.

### 2. API Versioning

- Significant changes (e.g., new parameters, methods, or structural overhauls) warrant a new API version.
- Example: Updating from `/v1.0/tweet` to `/v2.0/tweet`.
- Old versions are often deprecated, prompting developers to migrate to the newer version.

### 3. Pagination

- Essential for endpoints returning large datasets.
- Implemented using `limit` and `offset` parameters to fetch results in smaller chunks.
- Example:
  - `https://api.twitter.com/v1.0/users/:id/tweets?limit=10&offset=0` (fetches the first 10 tweets).

### 4. HTTP Best Practices

- **GET requests**: Should be read-only and idempotent (e.g., no side effects like writing to a database).
- **POST requests**: Used for creating resources and may include optional payloads.

### Example: Twitter REST API

#### Creating a Tweet

- **Endpoint**: `https://api.twitter.com/v1.0/tweet`
- **Payload** (example request):

  ```json
  {
    "userId": "12345",
    "content": "Hello, Twitter!"
  }
  ```

- **Response** (example):

  ```json
  {
    "tweetId": "abc123",
    "userId": "12345",
    "content": "Hello, Twitter!",
    "createdAt": "2025-01-13T10:00:00Z",
    "likes": 0
  }
  ```

#### Fetching Tweets

- **Endpoint**: `https://api.twitter.com/v1.0/users/:id/tweets?limit=10&offset=0`
- Parameters:
  - `id` (required): User ID.
  - `limit` (optional): Number of tweets per page.
  - `offset` (optional): Starting point for the results.

### Security

- **API Keys**:
  - Used to authenticate and authorize API requests.
  - New API keys may be issued with new versions to address security vulnerabilities.

### Best Practices

1. Avoid conflicting or ambiguous endpoints.
2. Maintain backward compatibility to prevent breaking dependent applications.
3. Implement pagination for scalability and efficiency.
4. Follow HTTP standards (e.g., GET should not modify server state).
5. Version APIs clearly and deprecate older versions thoughtfully.
