from datetime import datetime
from pydantic import BaseModel


class DocumentTypeBase(BaseModel):
    doc_type_name: str
    description: str
    created_by: str
    updated_by: str


class DocumentTypeCreate(DocumentTypeBase):
    pass


class DocumentTypeUpdate(BaseModel):
    doc_type_name: str | None = None
    description: str | None = None
    updated_by: str | None = None


class DocumentTypeSchema(DocumentTypeBase):
    doc_type_id: int
    created_on: datetime
    updated_on: datetime

    model_config = {
        "from_attributes": True
    }
