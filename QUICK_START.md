# 🚀 QUICK START GUIDE - Knowledge Graph System

## 30-Second Setup

### Windows Users:
```bash
cd c:\Users\Lenovo\Desktop\infosys_project
run_app.bat
```

### Linux/Mac Users:
```bash
cd ~/infosys_project
bash run_app.sh
```

## Manual Setup (5 minutes)

### Step 1: Open Two Terminals

**Terminal 1 - Backend:**
```bash
cd kg_backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd kg_frontend
pip install -r requirements.txt
streamlit run app.py
```

## What You'll See

✅ **Backend Running:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

✅ **Frontend Running:**
```
You can now view your Streamlit app in your browser.
URL: http://localhost:8501
```

## First Steps in the App

1. **Register** (Authentication tab)
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `password123`

2. **Upload Sample Text** (Dataset Management tab)
   - Create file: `sample.txt`
   - Content:
     ```
     Apple Inc. is an American technology company.
     Steve Jobs founded Apple.
     Apple is located in Cupertino, California.
     ```
   - Upload it

3. **Process Text** (NLP Processing tab)
   - Select your dataset
   - Click "Process Dataset File"
   - Wait for extraction results

4. **Create Graph** (Graph Explorer tab)
   - Name: `My First Graph`
   - Click "Create Graph"
   - Build from your processed dataset

5. **Explore** (Graph Explorer tab)
   - View statistics
   - Visualize relationships

## API Testing (Optional)

Use curl or Postman:

```bash
# Register
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","email":"user1@test.com","password":"pass123"}'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"pass123"}'

# Copy the access_token from response, then:

# Get Profile
curl -X GET http://localhost:5000/api/auth/profile \
  -H "Authorization: Bearer <your_token>"
```

## Project Files Explained

```
kg_backend/
├── app.py               ← Start here (Flask app)
├── models/user.py       ← Database tables
├── routes/
│   ├── auth.py         ← Login/Register
│   ├── dataset.py      ← File upload
│   ├── nlp.py          ← Text processing
│   └── graph.py        ← Graph operations
└── modules/
    ├── nlp_processor.py ← Entity & relation extraction
    └── graph_builder.py ← Graph visualization

kg_frontend/
└── app.py               ← Streamlit UI
```

## Features Implemented (Milestone 1 ✓)

### Authentication ✓
- User registration & login with JWT tokens
- User profiles with metadata
- Secure password hashing

### Dataset Management ✓
- Upload multiple file formats (txt, csv, json, xml, pdf)
- Store file metadata
- File management (list, view, delete)

### NLP Processing ✓
- Named Entity Recognition (NER) with spaCy
- Relation Extraction with zero-shot classification
- Process raw text or files
- Extract entity-relation-entity triples

### Knowledge Graph ✓
- Create multiple graphs
- Build from extracted triples
- Graph statistics (nodes, edges, density)
- Entity search and subgraph queries
- Add manual triples

### Frontend ✓
- Streamlit UI with 6 tabs
- Real-time processing feedback
- Data visualization with pandas
- Interactive forms and buttons

## Troubleshooting

**Issue: "ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**Issue: "spaCy model not found"**
```bash
python -m spacy download en_core_web_sm
```

**Issue: "Port 5000 already in use"**
```bash
# Edit app.py, change: app.run(debug=True, port=5001)
```

**Issue: Connection refused**
- Make sure backend is running (should see "Running on..." message)
- Wait 3-5 seconds after starting backend before opening frontend

## Next Milestones (Future)

- [ ] PyVis interactive graph visualization
- [ ] Semantic search with Sentence Transformers
- [ ] Neo4j graph database integration
- [ ] Advanced admin dashboard
- [ ] Docker containerization
- [ ] Deployment to Hugging Face Spaces

---

**Ready to go?** Just run `run_app.bat` (Windows) or `bash run_app.sh` (Linux/Mac)! 🎉

Questions? Check [SETUP_AND_EXECUTION.md](SETUP_AND_EXECUTION.md) for detailed docs.
