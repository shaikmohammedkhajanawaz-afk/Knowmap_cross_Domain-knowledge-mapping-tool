# API Testing Guide - Knowledge Graph System

## Quick Reference

Base URL: `http://localhost:5000/api`

All endpoints (except register/login) require JWT token in header:
```
Authorization: Bearer <your_jwt_token>
```

## Complete API Examples

### 1. AUTHENTICATION ENDPOINTS

#### Register New User
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password_123"
  }'
```

**Response:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "created_at": "2024-02-15T10:30:00"
  }
}
```

#### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password_123"
  }'
```

**Response:**
```json
{
  "message": "Login successful",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "created_at": "2024-02-15T10:30:00"
  }
}
```

#### Get User Profile
```bash
curl -X GET http://localhost:5000/api/auth/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "created_at": "2024-02-15T10:30:00"
  },
  "datasets_count": 2,
  "graphs_count": 1
}
```

#### Update Profile
```bash
curl -X PUT http://localhost:5000/api/auth/profile \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "new_password_456"
  }'
```

---

### 2. DATASET MANAGEMENT ENDPOINTS

#### Upload Dataset
```bash
curl -X POST http://localhost:5000/api/dataset/upload \
  -H "Authorization: Bearer <token>" \
  -F "file=@/path/to/document.txt" \
  -F "name=My Important Document"
```

**Response:**
```json
{
  "message": "Dataset uploaded successfully",
  "dataset": {
    "id": 1,
    "name": "My Important Document",
    "filename": "1708018200_document.txt",
    "uploaded_at": "2024-02-15T10:30:00",
    "file_type": "txt",
    "size": 2048
  }
}
```

#### List User's Datasets
```bash
curl -X GET http://localhost:5000/api/dataset/list \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "datasets": [
    {
      "id": 1,
      "name": "My Important Document",
      "filename": "1708018200_document.txt",
      "uploaded_at": "2024-02-15T10:30:00",
      "file_type": "txt",
      "size": 2048
    }
  ]
}
```

#### Get Specific Dataset
```bash
curl -X GET http://localhost:5000/api/dataset/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "dataset": {
    "id": 1,
    "name": "My Important Document",
    "filename": "1708018200_document.txt",
    "uploaded_at": "2024-02-15T10:30:00",
    "file_type": "txt",
    "size": 2048
  }
}
```

#### Delete Dataset
```bash
curl -X DELETE http://localhost:5000/api/dataset/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "message": "Dataset deleted successfully"
}
```

---

### 3. NLP PROCESSING ENDPOINTS

#### Process Raw Text
```bash
curl -X POST http://localhost:5000/api/nlp/process \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Apple Inc. was founded by Steve Jobs in Cupertino, California."
  }'
```

**Response:**
```json
{
  "result": {
    "entities": [
      {
        "text": "Apple Inc.",
        "label": "ORG",
        "start": 0,
        "end": 10
      },
      {
        "text": "Steve Jobs",
        "label": "PERSON",
        "start": 26,
        "end": 36
      },
      {
        "text": "Cupertino",
        "label": "GPE",
        "start": 40,
        "end": 49
      }
    ],
    "relations": [
      {
        "entity_1": "Apple Inc.",
        "relation": "founded_by",
        "entity_2": "Steve Jobs",
        "confidence": 0.85
      },
      {
        "entity_1": "Apple Inc.",
        "relation": "located_in",
        "entity_2": "Cupertino",
        "confidence": 0.92
      }
    ],
    "entity_count": 3,
    "relation_count": 2
  }
}
```

#### Process Uploaded File
```bash
curl -X POST http://localhost:5000/api/nlp/process-file/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "message": "File processed successfully",
  "entities_found": 25,
  "relations_found": 18,
  "extractions_stored": 18,
  "result": {
    "entities": [...],
    "relations": [...],
    "entity_count": 25,
    "relation_count": 18
  }
}
```

#### Get Extractions for Dataset
```bash
curl -X GET http://localhost:5000/api/nlp/extractions/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "extractions": [
    {
      "id": 1,
      "entity_1": "Apple Inc.",
      "relation": "founded_by",
      "entity_2": "Steve Jobs",
      "confidence": 0.85
    },
    {
      "id": 2,
      "entity_1": "Apple Inc.",
      "relation": "located_in",
      "entity_2": "Cupertino",
      "confidence": 0.92
    }
  ],
  "count": 2
}
```

---

### 4. KNOWLEDGE GRAPH ENDPOINTS

#### Create New Graph
```bash
curl -X POST http://localhost:5000/api/graph/create \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tech Companies Knowledge Graph"
  }'
```

**Response:**
```json
{
  "message": "Knowledge graph created",
  "graph": {
    "id": 1,
    "name": "Tech Companies Knowledge Graph",
    "created_at": "2024-02-15T10:30:00",
    "updated_at": "2024-02-15T10:30:00"
  }
}
```

#### Build Graph from Dataset
```bash
curl -X POST http://localhost:5000/api/graph/1/from-dataset/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "message": "Graph built successfully",
  "graph": {
    "id": 1,
    "name": "Tech Companies Knowledge Graph",
    "created_at": "2024-02-15T10:30:00",
    "updated_at": "2024-02-15T10:35:00"
  },
  "statistics": {
    "nodes": 25,
    "edges": 18,
    "density": 0.031,
    "is_directed": true
  }
}
```

#### Get Graph Data
```bash
curl -X GET http://localhost:5000/api/graph/1 \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "graph": {
    "id": 1,
    "name": "Tech Companies Knowledge Graph",
    "created_at": "2024-02-15T10:30:00",
    "updated_at": "2024-02-15T10:35:00"
  },
  "data": {
    "nodes": [
      {"id": "Apple Inc.", "label": "Apple Inc.", "type": "entity"},
      {"id": "Steve Jobs", "label": "Steve Jobs", "type": "entity"}
    ],
    "edges": [
      {
        "source": "Apple Inc.",
        "target": "Steve Jobs",
        "label": "founded_by",
        "confidence": 0.85
      }
    ],
    "node_count": 25,
    "edge_count": 18
  }
}
```

#### Add Triple to Graph
```bash
curl -X POST http://localhost:5000/api/graph/1/add-triple \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "entity_1": "Microsoft",
    "relation": "founded_by",
    "entity_2": "Bill Gates",
    "confidence": 0.95
  }'
```

**Response:**
```json
{
  "message": "Triple added successfully",
  "graph": {
    "id": 1,
    "name": "Tech Companies Knowledge Graph",
    "created_at": "2024-02-15T10:30:00",
    "updated_at": "2024-02-15T10:40:00"
  }
}
```

#### Search Entity in Graph
```bash
curl -X GET "http://localhost:5000/api/graph/1/search/Apple%20Inc." \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "entity": "Apple Inc.",
  "subgraph": {
    "nodes": [
      {"id": "Apple Inc.", "label": "Apple Inc."},
      {"id": "Steve Jobs", "label": "Steve Jobs"},
      {"id": "Cupertino", "label": "Cupertino"}
    ],
    "edges": [
      {
        "source": "Apple Inc.",
        "target": "Steve Jobs",
        "label": "founded_by"
      },
      {
        "source": "Apple Inc.",
        "target": "Cupertino",
        "label": "located_in"
      }
    ]
  }
}
```

#### Get Graph Statistics
```bash
curl -X GET http://localhost:5000/api/graph/1/statistics \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "graph": {
    "id": 1,
    "name": "Tech Companies Knowledge Graph",
    "created_at": "2024-02-15T10:30:00",
    "updated_at": "2024-02-15T10:40:00"
  },
  "statistics": {
    "nodes": 26,
    "edges": 19,
    "density": 0.029,
    "is_directed": true
  }
}
```

#### List User's Graphs
```bash
curl -X GET http://localhost:5000/api/graph/my-graphs \
  -H "Authorization: Bearer <token>"
```

**Response:**
```json
{
  "graphs": [
    {
      "id": 1,
      "name": "Tech Companies Knowledge Graph",
      "created_at": "2024-02-15T10:30:00",
      "updated_at": "2024-02-15T10:40:00"
    },
    {
      "id": 2,
      "name": "Financial Network",
      "created_at": "2024-02-15T11:00:00",
      "updated_at": "2024-02-15T11:05:00"
    }
  ]
}
```

---

## Testing Workflow

### Step 1: Register & Login
```bash
# Register
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
  }'

# Login and save token
TOKEN=$(curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }' | jq -r '.access_token')

echo "Token: $TOKEN"
```

### Step 2: Upload & Process Dataset
```bash
# Create test file
echo "Apple Inc. was founded by Steve Jobs." > test.txt

# Upload
curl -X POST http://localhost:5000/api/dataset/upload \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@test.txt" \
  -F "name=Test Document"

# Process (assume dataset_id=1)
curl -X POST http://localhost:5000/api/nlp/process-file/1 \
  -H "Authorization: Bearer $TOKEN"
```

### Step 3: Create & Build Graph
```bash
# Create graph
curl -X POST http://localhost:5000/api/graph/create \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Graph"}'

# Build from dataset (assume graph_id=1)
curl -X POST http://localhost:5000/api/graph/1/from-dataset/1 \
  -H "Authorization: Bearer $TOKEN"

# View statistics
curl -X GET http://localhost:5000/api/graph/1/statistics \
  -H "Authorization: Bearer $TOKEN"
```

---

## Error Responses

### 401 Unauthorized
```json
{
  "msg": "Missing Authorization Header"
}
```

### 404 Not Found
```json
{
  "message": "Dataset not found"
}
```

### 400 Bad Request
```json
{
  "message": "Missing required fields"
}
```

### 500 Server Error
```json
{
  "message": "Error processing file: [error details]"
}
```

---

## Tools for Testing

### Option 1: curl (command line)
```bash
curl -X GET http://localhost:5000/api/...
```

### Option 2: Postman (GUI)
- Import collection: API endpoints listed above
- Set Authorization header with Bearer token
- Test each endpoint

### Option 3: Python requests
```python
import requests

token = "your_jwt_token"
headers = {"Authorization": f"Bearer {token}"}

# Get profile
response = requests.get(
    "http://localhost:5000/api/auth/profile",
    headers=headers
)
print(response.json())
```

### Option 4: Streamlit Frontend
- Use the built-in UI at http://localhost:8501
- All API calls handled automatically

---

**API Version:** 1.0
**Last Updated:** February 2024
