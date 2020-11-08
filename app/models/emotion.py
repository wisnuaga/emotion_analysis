from pydantic import BaseModel


class Emotion(BaseModel):
    text: str
