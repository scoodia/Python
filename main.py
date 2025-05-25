"""Example CLI for the job hunting assistant."""

import argparse
from pathlib import Path

from jobhunt import (
    Config,
    InterviewPrep,
    JobMatcher,
    JobPreferences,
    ResumeOptimizer,
    UserProfile,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Job hunting assistant demo")
    parser.add_argument("resume", type=Path, help="Path to resume text file")
    args = parser.parse_args()

    prefs = JobPreferences()
    user = UserProfile.from_file(args.resume, prefs)
    matcher = JobMatcher.from_json(Path("jobhunt/data/jobs.json"))
    matches = matcher.match(user, top_n=Config.top_n_matches)

    print("Top job matches:")
    for job, score in matches:
        print(f"- {job.title} ({score:.2f})")

    if matches:
        selected_job = matches[0][0]
        optimizer = ResumeOptimizer(user)
        suggestions = optimizer.optimize_for(selected_job.description)
        print("\nResume suggestions:")
        for s in suggestions:
            print(f"* {s}")

        prep = InterviewPrep(selected_job.description)
        questions = prep.questions()
        print("\nInterview questions:")
        for category, qs in questions.items():
            print(f"{category}:")
            for q in qs:
                print(f"- {q}")


if __name__ == "__main__":
    main()
