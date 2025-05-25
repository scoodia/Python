"""Generate interview questions based on job description."""

from typing import Dict, List

from .job_matching import _tokenize


TECHNICAL_TEMPLATE = "Describe your experience with {keyword}."
BEHAVIORAL_QUESTIONS = [
    "Tell me about a time you overcame a challenge.",
    "Describe a situation where you showed leadership.",
]


def generate_role_specific(job_description: str, top_n: int = 3) -> List[str]:
    tokens = set(_tokenize(job_description))
    keywords = list(tokens)[:top_n]
    return [TECHNICAL_TEMPLATE.format(keyword=kw) for kw in keywords]


def categorize_questions(job_description: str) -> Dict[str, List[str]]:
    return {
        "Technical": generate_role_specific(job_description),
        "Behavioral": BEHAVIORAL_QUESTIONS,
    }


class InterviewPrep:
    def __init__(self, job_description: str):
        self.job_description = job_description

    def questions(self) -> Dict[str, List[str]]:
        return categorize_questions(self.job_description)
