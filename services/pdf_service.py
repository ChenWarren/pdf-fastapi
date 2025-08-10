import io
from pypdf import PdfReader
from fastapi import HTTPException

def extract_pdf_metadata(file_content: bytes, filename: str):
  """Extract metadata from PDF file content"""
  try:
    pdf_stream = io.BytesIO(file_content)
    pdf_reader = PdfReader(pdf_stream)
    page_count = len(pdf_reader.pages)
    file_size = len(file_content)
    file_size_mb = round(file_size / (1024 * 1024), 2)

    return {
        "filename": filename,
        "size": f"{file_size_mb} MB",
        "page_count": page_count,
    }

  except Exception as e:
    # Handle PDF parsing errors
    raise HTTPException(
        status_code=400,
        detail=f"Error processing PDF: {str(e)}"
    )