from pydantic import BaseModel


class Job(BaseModel):
    title: str
    company: str
    remote: bool
    salary: int


def build_prompt(jobs: list[Job]) -> str:
    if not jobs:
        raise ValueError("No jobs to summarize")
    remote = [j for j in jobs if j.remote]
    if not remote:
        raise ValueError("no remote jobs to summarize")
    lines = [f"- {j.title} at {j.company} ({j.salary:,})" for j in remote]
    return "Summarize these remote AI roles for a job seeker: \n" + "\n".join(lines)
