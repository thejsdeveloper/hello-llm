import json;
from pathlib import Path

from pydantic import BaseModel, TypeAdapter

class JobPosting(BaseModel):
  title: str
  company: str
  salary_max: int
  remote: bool
  skills: list[str]

Posting_Adapter = TypeAdapter(list[JobPosting])

job_text = Path("jobs.json").read_text()

postings = Posting_Adapter.validate_json(job_text)

matches = [
  job for job in postings
  if job.remote and "python" in job.skills
]

top = sorted(matches, key=lambda job: job.salary_max, reverse=True)[:3]

lines = [
  f"{i}. {job.title} at {job.company}"
  f" (up to ${job.salary_max:,})"
  f" - skills {', '.join(job.skills)}"
  for i, job in enumerate(top, start=1)
]

jobs_block = "\n".join(lines);

prompt = f"""
You are a career coach for a full-stack TS developer moving into AI Engineering.

Here are their top {len(top)} matching job postings:

{jobs_block}

based only on these postings, which single skill should they learn next?

Answer in two sentences
"""

print(prompt)