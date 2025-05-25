"""Simple job matching based on keyword overlap."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

from .profile import UserProfile


def _tokenize(text: str) -> List[str]:
    return [token.lower() for token in text.split()]


def _keyword_score(resume_tokens: List[str], job_tokens: List[str]) -> float:
    if not resume_tokens or not job_tokens:
        return 0.0
    resume_set = set(resume_tokens)
    job_set = set(job_tokens)
    intersection = resume_set & job_set
    return len(intersection) / len(job_set)


@dataclass
class JobPosting:
    id: int
    title: str
    location: str
    role: str
    industry: str
    description: str

    @property
    def tokens(self) -> List[str]:
        return _tokenize(self.description)


class JobMatcher:
    def __init__(self, jobs: List[JobPosting]):
        self.jobs = jobs

    @classmethod
    def from_json(cls, path: Path) -> "JobMatcher":
        data = json.loads(path.read_text())
        jobs = [JobPosting(**job) for job in data]
        return cls(jobs)

    def match(self, profile: UserProfile, top_n: int = 5) -> List[Tuple[JobPosting, float]]:
        resume_tokens = _tokenize(profile.resume_text)
        scored = []
        for job in self.jobs:
            score = _keyword_score(resume_tokens, job.tokens)
            scored.append((job, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]
