# Knowledge Graph Construction System - Setup & Execution Guide

## Project Structure
```
infosys_project/
├── kg_backend/                 # Flask Backend
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── models/
│   │   └── user.py            # Database models
│   ├── routes/
│   │   ├── auth.py            # Authentication endpoints
│   │   ├── dataset.py         # Dataset management endpoints
│   │   ├── nlp.py             # NLP processing endpoints
│   │   └── graph.py           # Graph management endpoints
│   └── modules/
│       ├── nlp_processor.py    # NER & Relation extraction
│       └── graph_builder.py    # Graph construction
│
└── kg_frontend/                # Streamlit Frontend
    ├── app.py                 # Streamlit UI
    └── requirements.txt        # Frontend dependencies
```

## Setup Instructions

### 1. Install Python & Virtual Environment
```bash
# Navigate to project directory
cd c:\Users\Lenovo\Desktop\infosys_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

### 2. Install Backend Dependencies
```bash
cd kg_backend

# Install requirements
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### 3. Install Frontend Dependencies
```bash
cd ../kg_frontend

# Install requirements
pip install -r requirements.txt
```

## Running the Application

### Option 1: Run Backend & Frontend Separately

#### Terminal 1 - Run Backend (Flask API)
```bash
cd kg_backend
python app.py
```

Expected output:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

#### Terminal 2 - Run Frontend (Streamlit)
```bash
cd kg_frontend
streamlit run app.py
```

Expected output:
```
You can now view your Streamlit app in your browser.
URL: http://localhost:8501
```

### Option 2: Run Using Shell Scripts

#### create batch/shell file to run both:
For Windows (create `run_app.bat`):
```batch
@echo off
start cmd /k "cd kg_backend && python app.py"
start cmd /k "cd kg_frontend && streamlit run app.py"
```

For Linux/Mac (create `run_app.sh`):
```bash
#!/bin/bash
cd kg_backend
python app.py &
cd ../kg_frontend
streamlit run app.py
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get JWT token
- `GET /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update user profile
- `POST /api/auth/logout` - Logout (client-side token removal)

### Dataset Management
- `POST /api/dataset/upload` - Upload dataset file
- `GET /api/dataset/list` - List user's datasets
- `GET /api/dataset/<id>` - Get specific dataset
- `DELETE /api/dataset/<id>` - Delete dataset

### NLP Processing
- `POST /api/nlp/process` - Process raw text
- `POST /api/nlp/process-file/<dataset_id>` - Process uploaded file
- `GET /api/nlp/extractions/<dataset_id>` - Get extractions for dataset

### Knowledge Graph
- `POST /api/graph/create` - Create new graph
- `POST /api/graph/<id>/from-dataset/<dataset_id>` - Build graph from dataset
- `GET /api/graph/<id>` - Get graph data
- `POST /api/graph/<id>/add-triple` - Add triple to graph
- `GET /api/graph/<id>/search/<entity>` - Search entity in graph
- `GET /api/graph/<id>/statistics` - Get graph statistics
- `GET /api/graph/my-graphs` - List user's graphs

## Usage Workflow

### Step 1: Register/Login
- Go to "Authentication" tab in Streamlit UI
- Register new account or login with existing credentials

### Step 2: Upload Dataset
- Navigate to "Dataset Management"
- Upload a text file (supported: txt, csv, json, xml, pdf)
- Give your dataset a meaningful name

### Step 3: Process Dataset with NLP
- Go to "NLP Processing" tab
- Select your uploaded dataset
- Click "Process Dataset File"
- System extracts entities and relations

### Step 4: Create Knowledge Graph
- Navigate to "Graph Explorer"
- Create a new graph with a name
- Build graph from your processed dataset
- View statistics and entity relationships

### Step 5: Explore Graph
- Use "Visualize" tab to explore graph structure
- Search for specific entities and their connections
- Add manual triples to refine the graph

## Database

SQLite database (`kg_users.db`) is automatically created in the backend directory with the following tables:
- `users` - User accounts and profiles
- `datasets` - Uploaded datasets
- `extractions` - Extracted entities and relations
- `knowledge_graphs` - Knowledge graph definitions

## Troubleshooting

### Issue: spaCy model not found
```bash
python -m spacy download en_core_web_sm
```

### Issue: Port 5000 already in use
```bash
# Find and kill process using port 5000
lsof -i :5000
kill -9 <PID>
```

### Issue: Database locked
```bash
# Remove database file and restart
rm kg_users.db
python app.py
```

### Issue: ModuleNotFoundError
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

## Sample Test Data

### Text to Process:
```
Apple Inc. is an American technology company founded by Steve Jobs. 
Apple is located in Cupertino, California. 
Steve Jobs worked for Apple and created the Macintosh computer.
```

Expected entities: Apple, American, Steve Jobs, Cupertino, California, Macintosh
Expected relations: founded_by, located_in, works_for, created_by

## Next Steps (Future Milestones)

1. **Week 4-6**: Advanced Graph Visualization with PyVis/D3.js
2. **Week 7-9**: Semantic Search with Sentence Transformers
3. **Week 10-12**: Neo4j Integration for persistent graph storage
4. **Week 13**: Admin Dashboard with real-time monitoring
5. **Week 14-15**: Deployment to Hugging Face Spaces / Docker

## Milestone 1 Completion Checklist

✅ JWT Authentication system
✅ User registration and login
✅ Dataset upload and management
✅ NER with spaCy
✅ Relation extraction
✅ Triple storage
✅ Basic graph construction
✅ Graph statistics
✅ Streamlit frontend
✅ Full API endpoints

## Support & Documentation

For detailed API documentation, refer to the docstrings in each route file.
For frontend components, check Streamlit documentation: https://docs.streamlit.io

---
Knowledge Graph System v1.0 | Milestone 1 Complete
