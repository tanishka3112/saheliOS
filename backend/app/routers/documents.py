from fastapi import APIRouter, HTTPException, status, UploadFile, File
from app.models import Document,CreateDocument
import os

router = APIRouter()

upload_folder = "app/uploads"

documents=[]

@router.post("/documents")
def post_Documents(doc: CreateDocument):
    next_id = 1 if not documents else documents[-1].id + 1
    new_doc = Document(
        id = next_id,
        title = doc.title,
        description = doc.description
    )
    documents.append(new_doc)
    return {"message":"Successfully accepted a new document"}

@router.get("/documents")
def get_All_Documents():
    return documents

@router.get("/documents/{id}")
def get_Document_by_ID(id: int):
    for document in documents:
        if (document.id == id):
            return document

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Document Not Found !!"
    )

@router.delete("/documents/{id}")
def delete_Document_by_ID(id: int):
    for index, document in enumerate(documents):
        if (document.id == id):
            deleted_document = documents.pop(index)
            return{"message":"Deleted Successfully!!!"}

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Document Not Found !!!"
    )

@router.post("/documents/upload")
def upload_document(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Only pdf files allowed."
        )

    filename = file.filename
    destination_path = os.path.join(upload_folder,filename)

    counter = 1
    base_name,extension = os.path.splitext(filename)

    while os.path.exists(destination_path):
        filename = f"{base_name}_{counter}{extension}"
        destination_path = os.path.join(upload_folder,filename)
        counter += 1

    with open(destination_path, "wb") as buffer:
        content = file.read()
        buffer.write(content)

    return {
        "message": "File uploaded successfully",
        "filename": filename,
        "content_type": file.content_type
    }