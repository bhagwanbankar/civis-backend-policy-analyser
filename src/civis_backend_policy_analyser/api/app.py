import logging
import sys
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from civis_backend_policy_analyser.core.db_connection import sessionmanager
from civis_backend_policy_analyser.api.document_type_router import document_type_router
from civis_backend_policy_analyser.api.evaluations_framework_router import router as evaluations_router

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, docs_url="/api/docs")


@app.get("/health-check")
async def root():
    return {"message": "Backend is running."}


app.include_router(document_type_router)
app.include_router(evaluations_router)


if __name__ == "__main__":
    uvicorn.run("civis_backend_policy_analyser.api.app:app", host="0.0.0.0", reload=True, port=8000)