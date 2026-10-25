
from typing import Literal
from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    project_id: str = Field(min_length=1)
    language: Literal["java", "python"]
    test_code: str = Field(min_length=1)
    context_code: str | None = None
