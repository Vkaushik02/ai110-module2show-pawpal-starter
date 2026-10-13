"""Basic tests for the PawPal+ core classes."""

from pawpal_system import Frequency, Pet, Task


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
