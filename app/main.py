from fastapi import FastAPI
from app.models import ModerationRequest
from app.service import ModerationService


# FastAPI application initialization
app = FastAPI(title="Aikyam Profanity Service")

# Service initialization
service = ModerationService()


@app.get("/health")
def health():
    """
    Health check endpoint.
    Used for monitoring and deployment validation.
    """

    return {"status": "ok"}


@app.post("/moderate")
def moderate(req: ModerationRequest):
    """
    Main moderation endpoint.
    """

    return service.moderate(req.text)


# Internal testing endpoint
@app.post("/admin/test")
def test(req: ModerationRequest):
    return service.moderate(req.text)