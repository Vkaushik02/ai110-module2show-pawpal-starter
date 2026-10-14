"""Tests for the PawPal+ core classes and scheduler."""

from datetime import date, timedelta

import pytest

from pawpal_system import Frequency, Owner, Pet, Scheduler, Task


@pytest.fixture
def setup():
    owner = Owner("Sam")
    pet = Pet("Rex", "dog", 3)
    owner.add_pet(pet)
    return owner, pet, Scheduler(owner)


# --- Basic behavior --------------------------------------------------------

def test_mark_complete_changes_status():
    task = Task("Morning walk", "07:30", Frequency.ONCE)
    assert task.is_complete is False

    task.mark_complete()

    assert task.is_complete is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Buddy", species="Dog", age=4)
    assert len(pet.tasks) == 0

    pet.add_task(Task("Morning walk", "07:30", Frequency.ONCE))

    assert len(pet.tasks) == 1


# --- Sorting correctness ---------------------------------------------------

def test_daily_schedule_is_chronological(setup):
    owner, pet, scheduler = setup
    # Added deliberately out of order
    pet.add_task(Task("Dinner", "18:00", Frequency.ONCE))
    pet.add_task(Task("Walk", "07:30", Frequency.ONCE))
    pet.add_task(Task("Meds", "12:15", Frequency.ONCE))

    times = [t.time for t in scheduler.get_daily_schedule()]

    assert times == ["07:30", "12:15", "18:00"]


def test_sort_handles_zero_padded_morning_times(setup):
    _, _, scheduler = setup
    tasks = [Task("Late", "10:00", Frequency.ONCE), Task("Early", "09:05", Frequency.ONCE)]

    assert [t.time for t in scheduler.sort_by_time(tasks)] == ["09:05", "10:00"]


def test_sort_empty_list_returns_empty(setup):
    _, _, scheduler = setup
    assert scheduler.sort_by_time([]) == []


# --- Recurrence logic ------------------------------------------------------

def test_completing_daily_task_creates_next_day_task(setup):
    _, pet, _ = setup
    task = Task("Walk", "08:00", Frequency.DAILY)
    pet.add_task(task)

    next_task = task.mark_complete()

    assert task.is_complete
    assert next_task is not None
    assert next_task.due_date == task.due_date + timedelta(days=1)
    assert next_task.time == "08:00"
    assert next_task in pet.get_pending_tasks()
    assert len(pet.tasks) == 2


def test_completing_weekly_task_creates_task_seven_days_later(setup):
    _, pet, _ = setup
    task = Task("Bath", "10:00", Frequency.WEEKLY)
    pet.add_task(task)

    next_task = task.mark_complete()

    assert next_task.due_date == task.due_date + timedelta(days=7)


def test_completing_one_time_task_creates_no_followup(setup):
    _, pet, _ = setup
    task = Task("Vet visit", "14:00", Frequency.ONCE)
    pet.add_task(task)

    assert task.mark_complete() is None
    assert len(pet.tasks) == 1


# --- Conflict detection ----------------------------------------------------

def test_detects_duplicate_times(setup):
    owner, pet, scheduler = setup
    a = Task("Walk", "08:00", Frequency.ONCE)
    b = Task("Feed", "08:00", Frequency.ONCE)
    pet.add_task(a)
    pet.add_task(b)

    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

    assert len(conflicts) == 1
    assert a in conflicts[0] and b in conflicts[0]


def test_no_conflict_for_different_times(setup):
    owner, pet, scheduler = setup
    pet.add_task(Task("Walk", "08:00", Frequency.ONCE))
    pet.add_task(Task("Feed", "08:30", Frequency.ONCE))

    assert scheduler.detect_conflicts(owner.get_all_tasks()) == []


def test_same_time_on_different_dates_is_not_a_conflict(setup):
    owner, pet, scheduler = setup
    pet.add_task(Task("Walk", "08:00", Frequency.ONCE, due_date=date.today()))
    pet.add_task(Task("Walk", "08:00", Frequency.ONCE, due_date=date.today() + timedelta(days=1)))

    assert scheduler.detect_conflicts(owner.get_all_tasks()) == []


def test_conflict_detected_across_different_pets(setup):
    owner, pet, scheduler = setup
    other = Pet("Mia", "cat", 2)
    owner.add_pet(other)
    pet.add_task(Task("Walk", "08:00", Frequency.ONCE))
    other.add_task(Task("Feed", "08:00", Frequency.ONCE))

    assert len(scheduler.detect_conflicts(owner.get_all_tasks())) == 1
