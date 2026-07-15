from typing import Literal

from pydantic import BaseModel


class JobPosting(BaseModel):
    title: str
    company: str
    remote: bool
    skills: list[str]
    salary_max: int
    seniority: Literal["junior", "mid", "senior"]
