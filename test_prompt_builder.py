import pytest
from prompt_builder import Job, build_prompt

JOBS = [
    Job(title="AI Engineer", company="Acme", remote=True, salary=195000),
    Job(title="Data Analyst", company="Beta", remote=False, salary=90000),
]


def test_keeps_remote_jobs_included():
    assert "AI Engineer" in build_prompt(JOBS)


def test_onsite_jobs_excluded():
    assert "Data analyst" not in build_prompt(JOBS)


def test_salary_get_thousand_separators():
    assert "195,000" in build_prompt(JOBS)


def test_empty_list_raises():
    with pytest.raises(ValueError):
        build_prompt([])


def test_all_onsite_raises():
    onsite = [Job(title="Data Analyst", company="Beta", remote=False, salary=90000)]
    with pytest.raises(ValueError):
        build_prompt(onsite)
