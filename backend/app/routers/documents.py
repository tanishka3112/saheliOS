from fastapi import APIRouter, HTTPException, status
from app.models import Document,CreateDocument

router = APIRouter()

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
