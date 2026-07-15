from pathlib import Path

from models import JobPosting

FIXTURE = Path("fixtures/job_posting.json")


def test_fixture_parses():
    job = JobPosting.model_validate_json(FIXTURE.read_text())

    assert job.title == "Senior AI Engineer"
    assert job.company == "Acme Corp"
    assert job.remote is False
    assert job.salary_max == 185_000
    assert job.seniority == "senior"
    assert "Python" in job.skills
