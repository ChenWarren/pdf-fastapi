# PDF Upload API

A FastAPI-based web service code example for uploading PDF files and extracting metadata (filename, size, page count).

## Features

- **PDF Upload**: Accept PDF file uploads via REST API
- **Metadata Extraction**: Extract filename, file size, and page count
- **File Validation**: Only accepts PDF files with size limits (max 10MB)
- **Interactive Docs**: Built-in Swagger UI for easy testing

## Project Structure

```
pdf-api/
├── main.py              # FastAPI application and routes
├── models.py            # Pydantic response models
├── services/
│   └── pdf_service.py   # PDF processing logic
├── requirements.txt     # Python dependencies
├── test_pdfs/           # Sample PDFs for testing
└── README.md           # This file
```

## Setup Instructions

### 1. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Server
```bash
uvicorn main:app --reload
```

You should see output like:
```
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process
```

## Testing the API

### Option 1: Interactive Documentation (Recommended)
1. Open your browser
2. Go to: `http://127.0.0.1:8000/docs`
3. Try the endpoints:
   - **GET** `/` - Health check
   - **GET** `/health` - Alternative health check  
   - **POST** `/upload` - Upload PDF file

### Option 2: Command Line Testing
```bash
# Test health check
curl http://127.0.0.1:8000/

# Upload PDF file
curl -X POST "http://127.0.0.1:8000/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your-pdf-file.pdf"
```

## API Endpoints

### `GET /`
Health check endpoint
**Response:**
```json
{
  "message": "PDF Upload API is running",
  "status": "healthy"
}
```

### `GET /health`  
Alternative health check
**Response:**
```json
{
  "status": "ok"
}
```

### `POST /upload`
Upload PDF file and extract metadata

**Request:** Multipart form data with `file` field containing PDF

**Success Response (200):**
```json
{
  "file_meta": {
    "filename": "document.pdf",
    "size": "2.5 MB",
    "page_count": 10
  },
  "message": "PDF processed successfully"
}
```

**Error Responses:**
- `400`: Invalid file type, size too large, or PDF parsing error
- `422`: Missing or invalid request format

## File Validation Rules

- **File Type**: Only PDF files accepted (`.pdf` extension + `application/pdf` MIME type)
- **File Size**: Maximum 10MB
- **Content**: Must be a valid, readable PDF file

## Development

### Adding Test PDFs
Place sample PDF files in the `test_pdfs/` directory for testing.

### Running in Development Mode
The `--reload` flag automatically restarts the server when code changes:
```bash
uvicorn main:app --reload
```

## Troubleshooting

**"Failed to fetch" in browser docs:**
- Make sure the server is running on `http://127.0.0.1:8000`
- Try refreshing the `/docs` page
- Use direct curl commands as alternative

**Import errors:**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**PDF parsing errors:**
- Ensure uploaded file is a valid PDF
- Check file is not corrupted or password-protected

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- pypdf
- python-multipart

See `requirements.txt` for complete dependency list.