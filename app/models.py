from pydantic import BaseModel


class ModerationRequest(BaseModel):
    """
    Request payload for moderation API.
    """

    text: str