from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from services.embeddings import upload_embeddings

app = FastAPI()

@app.post("/upload-embeddings")
async def upload_root_embeddings():
    await upload_embeddings()
    return {"Uploaded!"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )