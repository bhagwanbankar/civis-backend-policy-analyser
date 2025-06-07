# routers/document_type_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from civis_backend_policy_analyser.views.document_type_view import DocumentTypeView
from civis_backend_policy_analyser.schemas.document_type_schema import (
    DocumentTypeSchema,
    DocumentTypeCreate,
    DocumentTypeUpdate,
)
from civis_backend_policy_analyser.core.db_connection import DBSessionDep

document_type_router = APIRouter(
    prefix="/api/document_types",
    tags=["document_types"],
    responses={404: {"description": "Document Type not found"}},
)

# 1. Get all
@document_type_router.get("/", response_model=List[DocumentTypeSchema])
async def get_all_document_types(db_session: DBSessionDep):
    document_service = DocumentTypeView(db_session)
    return await document_service.all()


# 2. Get by ID
@document_type_router.get("/{document_type_id}", response_model=DocumentTypeSchema)
async def get_document_type(document_type_id: int, db_session: DBSessionDep):
    document_service = DocumentTypeView(db_session)
    document = await document_service.get(document_type_id)
    if not document:
        raise HTTPException(status_code=404, detail="DocumentType not found")
    return document


# 3. Create
@document_type_router.post("/", response_model=DocumentTypeSchema)
async def create_document_type(payload: DocumentTypeCreate, db_session: DBSessionDep):
    document_service = DocumentTypeView(db_session)
    return await document_service.create(payload)


# 4. Update
@document_type_router.put("/{document_type_id}", response_model=DocumentTypeSchema)
async def update_document_type(
    document_type_id: int,
    payload: DocumentTypeUpdate,
    db_session: DBSessionDep,
):
    document_service = DocumentTypeView(db_session)
    updated_doc = await document_service.update(document_type_id, payload)
    if not updated_doc:
        raise HTTPException(status_code=404, detail="DocumentType not found")
    return updated_doc


# 5. Delete
@document_type_router.delete("/{document_type_id}")
async def delete_document_type(document_type_id: int, db_session: DBSessionDep):
    document_service = DocumentTypeView(db_session)
    deleted = await document_service.delete(document_type_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="DocumentType not found")
    return {"message": f"DocumentType {document_type_id} deleted successfully"}
