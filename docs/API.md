# API Documentation for Carmula Backend

## Overview
Carmula is a backend service designed to manage and facilitate interactions with the Carmula system. This API provides a range of functionalities for developers.

## Authentication
- **Endpoint:** `/api/auth/login`
- **Method:** `POST`
- **Description:** Authenticates a user and returns a token for further requests.

### Request Body
```json
{
  "username": "user",
  "password": "pass"
}
```

### Response
- **200 OK**
```json
{
  "token": "your_jwt_token"
}
```

## Endpoints
### 1. Get User Information
- **Endpoint:** `/api/user`
- **Method:** `GET`
- **Description:** Retrieves the current user's information.

### Request Header
- `Authorization: Bearer your_jwt_token`

### Response
- **200 OK**
```json
{
  "id": "1",
  "username": "user",
  "email": "user@example.com"
}
```

### 2. Update User Profile
- **Endpoint:** `/api/user/update`
- **Method:** `PUT`
- **Description:** Updates the user's profile information.

### Request Body
```json
{
  "email": "new_email@example.com"
}
```

### Response
- **200 OK**
```json
{
  "message": "Profile updated successfully"
}
```

## Error Handling
All error responses will include a standard error structure:
```json
{
  "error": "Error message"
}
```

## Conclusion
This document serves as a basic guide for utilizing the Carmula backend API. For further inquiries or detailed explanations, please refer to the source code or contact the developer team.
