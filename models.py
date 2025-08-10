from pydantic import BaseModel

# Response models
class PDFMetadata(BaseModel):
  filename: str
  size: str
  page_count: int

class PDFUploadResponse(BaseModel):
  file_meta: PDFMetadata
  message: str

class ErrorResponse(BaseModel):
    detail: str