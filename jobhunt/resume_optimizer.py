"""Suggest improvements for resumes based on job description."""

from typing import List

from .profile import UserProfile
from .job_matching import _tokenize


def missing_keywords(resume_text: str, job_description: str) -> List[str]:
    resume_tokens = set(_tokenize(resume_text))
    job_tokens = set(_tokenize(job_description))
    return sorted(job_tokens - resume_tokens)


def suggest_bullets(missing: List[str]) -> List[str]:
    return [f"Highlight experience with {kw}." for kw in missing]


class ResumeOptimizer:
    def __init__(self, profile: UserProfile):
        self.profile = profile

    def optimize_for(self, job_description: str) -> List[str]:
        missing = missing_keywords(self.profile.resume_text, job_description)
        return suggest_bullets(missing)
