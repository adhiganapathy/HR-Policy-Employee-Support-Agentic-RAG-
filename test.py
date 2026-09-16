from app.core.config import get_settings
from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents

"""
docs = load_file(Path("app/data/sample_kb/company_hr_handbook.md"))

print(chunk_documents(docs))

#
"""

settings = get_settings()

folder_path = Path(settings.sample_kb_dir)
files = [p for p in folder_path.iterdir() if p.is_file()]

all_docs = []

for path in files:
    all_docs.extend(load_file(path))
chunks = chunk_documents(all_docs)
ids = add_documents(chunks)
print(f"Adding {len(chunks)} chunks to vectorstore...")


