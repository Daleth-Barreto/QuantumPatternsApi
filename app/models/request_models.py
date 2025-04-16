from pydantic import BaseModel

class PatternRequest(BaseModel):
    width: int = 100
    height: int = 100
    pattern_type: str = "simple"  # simple, circular, waves, checkerboard, other, word
    word: str | None = None
