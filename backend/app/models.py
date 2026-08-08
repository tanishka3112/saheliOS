from pydantic import BaseModel

class Document(BaseModel):
    id: int
    title: str
    description: str

class CreateDocument(BaseModel):
    title: str
    description: str
