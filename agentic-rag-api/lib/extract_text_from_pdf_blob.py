import fitz
import io

def extract_text_from_pdf_blob(file_blob):
    file_bytes = io.BytesIO(file_blob)
    doc = fitz.open(file_bytes)
    text = ""
    for page in doc:
        text += page.get_text()
    return text