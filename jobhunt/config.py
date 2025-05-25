"""Configuration settings for the job hunting assistant."""

from dataclasses import dataclass


@dataclass
class Config:
    """Configuration options that may be tuned by the user."""

    similarity_threshold: float = 0.2
    top_n_matches: int = 5
