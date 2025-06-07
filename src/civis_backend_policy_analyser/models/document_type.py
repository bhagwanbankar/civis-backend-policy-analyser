from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from civis_backend_policy_analyser.models.base import Base
from typing import List, Optional
from datetime import datetime

class DocumentType(Base):
    __tablename__ = "document_type"

    doc_type_id: Mapped[int] = mapped_column(primary_key=True)
    doc_type_name: Mapped[str]
    description: Mapped[str]
    created_by: Mapped[Optional[str]] = mapped_column(nullable=True)
    created_on: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    updated_on: Mapped[datetime] = mapped_column(nullable=True, server_default=func.now(), onupdate=func.now())
    updated_by: Mapped[Optional[str]] = mapped_column(nullable=True)

    evaluations: Mapped[List["EvaluationsFramework"]] = relationship("EvaluationsFramework", back_populates="document_type") # type: ignore

    assessment_criteria: Mapped[List["AssessmentCriteria"]] = relationship( # type: ignore
        "AssessmentCriteria",
        secondary="evaluations_framework",
        primaryjoin="DocumentType.doc_type_id == EvaluationsFramework.doc_type_id",
        secondaryjoin="AssessmentCriteria.assessment_id == EvaluationsFramework.assessment_id",
        back_populates="document_types",
        viewonly=True
    )