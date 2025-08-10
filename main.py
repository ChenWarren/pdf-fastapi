from fastapi import FastAPI, UploadFile, File, HTTPException
from models import PDFMetadata, PDFUploadResponse
from services.pdf_service import extract_pdf_metadata

# Constants
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_CONTENT_TYPES = ["application/pdf"]

# FastAPI app
app = FastAPI(
    title="PDF Upload API",
    description="API for uploading PDF files and extracting metadata",
    version="1.0.0"
)


# Root endpoint
@app.get("/")
async def health_check():
    return {"message": "PDF Upload API is running", "status": "healthy"}

# Health check endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}


# PDF upload and process
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
  # Validate file type
  if file.content_type not in ALLOWED_CONTENT_TYPES:
      raise HTTPException(
          status_code=400,
          detail=f"Invalid file type. Allowed types: {', '.join(ALLOWED_CONTENT_TYPES)}"
      )

  # Validate file extension
  if not file.filename.lower().endswith('.pdf'):
      raise HTTPException(
          status_code=400,
          detail="File must have .pdf extension"
      )

  # Check file size (limit to 10MB)
  content = await file.read()
  file_size = len(content)

  if file_size > MAX_FILE_SIZE:
      raise HTTPException(
          status_code=400,
          detail=f"File size exceeds the limit of {MAX_FILE_SIZE / (1024 * 1024)} MB"
      )
  
  # Extract PDF metadata
  metadata = extract_pdf_metadata(content, file.filename)


  # Return info
  return PDFUploadResponse( 
      file_meta=PDFMetadata(**metadata),
      message="PDF processed successfully"
  )


