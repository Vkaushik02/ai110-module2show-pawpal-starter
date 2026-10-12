"""PawPal+ class skeletons: attributes and empty method stubs only."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    """A single care activity for a pet."""

    description: str
    time: str  # e.g. "08:30" (24-hour HH:MM keeps string sorting chronological)
    frequency: str  # e.g. "once", "daily", "weekly"
    is_complete: bool = False

    def mark_complete(self) -> None:
        """Mark this task as done."""
        pass

    def reschedule(self, new_time: str) -> None:
        """Change the time this task is scheduled for."""
        pass

    def is_due_today(self) -> bool:
        """Return True if this task belongs in today's schedule."""
        pass


@dataclass
class Pet:
    """An animal profile with its assigned tasks."""

    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Assign a task to this pet."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet."""
        pass

    def get_pending_tasks(self) -> list[Task]:
        """Return tasks that are not yet complete."""
        pass


@dataclass
class Owner:
    """Manages multiple pets and aggregates their tasks."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's profile."""
        pass

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's profile."""
        pass

    def get_all_tasks(self) -> list[Task]:
        """Collect every task across all of the owner's pets."""
        pass


class Scheduler:
    """Reads tasks from an Owner to build and check the daily schedule."""

    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_daily_schedule(self) -> list[Task]:
        """Return today's tasks, sorted chronologically."""
        pass

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return the given tasks ordered by their time."""
        pass

    def detect_conflicts(self, tasks: list[Task]) -> list:
        """Return groups of tasks that share the same time slot."""
        pass