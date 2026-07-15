import os
from pathlib import Path

from openrouter import OpenRouter

from models import JobPosting

api_key = os.getenv("OPEN_ROUTER_KEY")

RAW_AD = """
Acme Corp is hiring an senior AI Engineer! Build LLM-powered features
end to end. Must know Python, FastAPI, and RAG patterns.
Hybrid role (2 days onsite). Up to $185k.
"""


def main() -> None:
    with OpenRouter(api_key=api_key) as client:
        response = client.chat.send(
            model="anthropic/claude-haiku-4.5",
            messages=[
                {"role": "user", "content": f"Extract the job posting details:\n\n{RAW_AD}"}
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "job_posting",
                    "strict": True,
                    "schema": JobPosting.model_json_schema(),
                },
            },
        )

        raw = response.choices[0].message.content

        Path("fixtures").mkdir(exist_ok=True)
        Path("fixtures/job_posting.json").write_text(raw)

        job = JobPosting.model_validate_json(raw)
        print(f"{job.title} @ {job.company}")
        print(f"remote: {job.remote}, salary_max: {job.salary_max}")
        print(f"skills: {', '.join(job.skills)}")
        print(f"Seniority {job.seniority}")


if __name__ == "__main__":
    main()
