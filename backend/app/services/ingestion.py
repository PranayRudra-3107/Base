import io
import csv
import uuid
from datetime import datetime
from typing import List, Tuple, Dict, Any
import pypdf
from app.core.config import get_settings

settings = get_settings()


def chunk_text(text: str, chunk_size: int = None, overlap: int = None) -> List[str]:
    chunk_size = chunk_size or settings.chunk_size
    overlap = overlap or settings.chunk_overlap

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = pypdf.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"
    return text


def extract_text_from_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore")


def extract_text_from_csv(file_bytes: bytes) -> str:
    text = extract_text_from_txt(file_bytes)
    rows = csv.reader(io.StringIO(text))
    return "\n".join(" | ".join(cell.strip() for cell in row) for row in rows)


def extract_text(filename: str, file_bytes: bytes) -> str:
    ext = filename.lower().split(".")[-1]

    if ext == "pdf":
        return extract_text_from_pdf(file_bytes)
    elif ext in ["txt", "md"]:
        return extract_text_from_txt(file_bytes)
    elif ext == "csv":
        return extract_text_from_csv(file_bytes)
    else:
        raise ValueError(f"Unsupported file type: .{ext}. Supported: pdf, txt, md, csv")


def process_file_details(filename: str, file_bytes: bytes) -> Dict[str, Any]:
    """Extract text from file and return chunks, metadata, and document details."""
    text = extract_text(filename, file_bytes)
    if not text.strip():
        raise ValueError("Could not extract text from file.")

    document_id = str(uuid.uuid4())
    chunks = chunk_text(text)
    uploaded_at = datetime.utcnow().isoformat()

    metadatas = [
        {
            "document_id": document_id,
            "filename": filename,
            "chunk_index": i,
            "total_chunks": len(chunks),
            "uploaded_at": uploaded_at,
        }
        for i in range(len(chunks))
    ]

    return {
        "document_id": document_id,
        "filename": filename,
        "text": text,
        "chunks": chunks,
        "metadatas": metadatas,
        "uploaded_at": uploaded_at,
    }


def process_file(filename: str, file_bytes: bytes) -> Tuple[List[str], List[dict]]:
    """Extract text from file and return (chunks, metadatas)."""
    details = process_file_details(filename, file_bytes)
    return details["chunks"], details["metadatas"]
