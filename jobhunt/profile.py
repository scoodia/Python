"""User profile ingestion utilities."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class JobPreferences:
    location: Optional[str] = None
    role: Optional[str] = None
    industry: Optional[str] = None


@dataclass
class UserProfile:
    resume_text: str
    preferences: JobPreferences = field(default_factory=JobPreferences)
    skills: List[str] = field(default_factory=list)
    education: Optional[str] = None
    experience: Optional[str] = None

    @staticmethod
    def parse_resume(path: Path) -> str:
        """Parse resume text from a file.

        Currently supports plain text files. PDF or DOCX parsing is not
        implemented due to limited environment.
        """
        if not path.exists():
            raise FileNotFoundError(path)
        if path.suffix.lower() not in {".txt"}:
            raise NotImplementedError(
                "Only plain text resumes are supported in this environment"
            )
        return path.read_text(encoding="utf-8")

    @classmethod
    def from_file(cls, path: Path, preferences: JobPreferences) -> "UserProfile":
        text = cls.parse_resume(path)
        return cls(resume_text=text, preferences=preferences)
