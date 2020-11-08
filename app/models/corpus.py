from pydantic import BaseModel


class Corpus(BaseModel):
    text: str
    anger: float
    disgust: float
    fear: float
    happiness: float
    sadness: float
    surprise: float