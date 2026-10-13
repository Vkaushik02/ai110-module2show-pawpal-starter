# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

Today's Schedule for Jordan
- 07:30  Morning walk       (Buddy)
- 08:00  Feed breakfast     (Whiskers)
- 12:15  Flea medication    (Whiskers)
- 18:00  Evening walk       (Buddy)

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time` | Orders tasks by their `HH:MM` time. Works because times are zero-padded 24-hour strings, so string order matches chronological order. Ties keep insertion order. |
| Filtering | `Scheduler.get_daily_schedule`, `Scheduler.filter_by_status` | `get_daily_schedule` keeps only incomplete tasks due today, sorted by time. `filter_by_status(completed)` returns all of the owner's pending or completed tasks. |
| Conflict handling | `Scheduler.detect_conflicts` | Groups tasks by exact `(due_date, time)` and returns every group with more than one task, for the same pet or different pets. It returns the groups rather than raising an error, and the UI shows them as warnings. It doesn't detect partial overlaps because tasks have no duration. |
| Recurring tasks | `Task.mark_complete`, `Frequency` | Completing a `DAILY` or `WEEKLY` task creates the next occurrence on the same pet, with the due date moved forward 1 or 7 days using `timedelta`. `ONCE` tasks just complete. |

## Implementation Summary

The PawPal+ core system architecture manages pet care schedules using object-oriented relationships between the Owner, Pet, Task, and Scheduler classes. An Owner can manage multiple Pet instances, each maintaining its own collection of Task objects defined by a specific Frequency enumeration. The system relies on the central Scheduler class to pull consolidated data from the Owner layer, allowing it to efficiently organize daily routines, sort items chronologically, and evaluate the schedule for potential timing conflicts.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
