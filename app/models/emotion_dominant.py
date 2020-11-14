from pydantic import BaseModel
from typing import Optional


class EmotionDominant(BaseModel):
    text: str
    beta: Optional[float] = 0.03
