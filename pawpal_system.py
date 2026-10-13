"""PawPal+ class skeletons: attributes and empty method stubs only."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum


class Frequency(Enum):
    """How often a task repeats."""

    ONCE = "once"
    DAILY = "daily"
    WEEKLY = "weekly"


@dataclass
class Task:
    """A single care activity for a pet."""

    description: str
    time: str  # e.g. "08:30" (24-hour HH:MM keeps string sorting chronological)
    frequency: Frequency
    due_date: date = field(default_factory=date.today)
    pet: Pet | None = field(default=None, repr=False, compare=False)
    is_complete: bool = False

    def mark_complete(self) -> Task | None:
        """Mark this task as done; for DAILY/WEEKLY tasks, queue the next
        occurrence on the same pet and return it (None for ONCE tasks)."""
        self.is_complete = True
        if self.frequency is Frequency.ONCE:
            return None
        days = 1 if self.frequency is Frequency.DAILY else 7
        next_task = Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            due_date=self.due_date + timedelta(days=days),
        )
        if self.pet is not None:
            self.pet.add_task(next_task)
        return next_task

    def reschedule(self, new_time: str) -> None:
        """Change the time this task is scheduled for."""
        self.time = new_time

    def is_due_today(self) -> bool:
        """Return True if this task belongs in today's schedule."""
        return self.due_date == date.today() and not self.is_complete


@dataclass
class Pet:
    """An animal profile with its assigned tasks."""

    name: str
    species: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Assign a task to this pet and set the task's back-reference."""
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet (matched by identity, not equality)."""
        for i, existing in enumerate(self.tasks):
            if existing is task:
                del self.tasks[i]
                task.pet = None
                return

    def get_pending_tasks(self) -> list[Task]:
        """Return tasks that are not yet complete."""
        return [t for t in self.tasks if not t.is_complete]


@dataclass
class Owner:
    """Manages multiple pets and aggregates their tasks."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's profile (ignored if already added)."""
        if not any(p is pet for p in self.pets):
            self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's profile (matched by identity)."""
        self.pets = [p for p in self.pets if p is not pet]

    def get_all_tasks(self) -> list[Task]:
        """Collect every task across all of the owner's pets."""
        return [task for pet in self.pets for task in pet.tasks]


class Scheduler:
    """Reads tasks from an Owner to build and check the daily schedule."""

    def __init__(self, owner: Owner) -> None:
        """Store the owner whose pets' tasks this scheduler reads."""
        self.owner = owner

    def get_daily_schedule(self) -> list[Task]:
        """Return today's tasks, sorted chronologically."""
        due = [t for t in self.owner.get_all_tasks() if t.is_due_today()]
        return self.sort_by_time(due)

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return the given tasks ordered by their time."""
        return sorted(tasks, key=lambda t: t.time)

    def detect_conflicts(self, tasks: list[Task]) -> list[list[Task]]:
        """Return groups of tasks that share the same date and time slot."""
        slots: dict[tuple[date, str], list[Task]] = {}
        for task in tasks:
            slots.setdefault((task.due_date, task.time), []).append(task)
        return [group for group in slots.values() if len(group) > 1]