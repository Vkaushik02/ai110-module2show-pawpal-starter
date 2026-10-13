"""Demo script: build an owner with pets and tasks, then print today's schedule."""

from pawpal_system import Frequency, Owner, Pet, Scheduler, Task


def main() -> None:
    # Create the owner and two pets
    owner = Owner(name="Jordan")
    buddy = Pet(name="Buddy", species="Dog", age=4)
    whiskers = Pet(name="Whiskers", species="Cat", age=2)
    owner.add_pet(buddy)
    owner.add_pet(whiskers)

    # Add tasks at different times (added out of order to show sorting)
    buddy.add_task(Task("Evening walk", "18:00", Frequency.DAILY))
    buddy.add_task(Task("Morning walk", "07:30", Frequency.DAILY))
    whiskers.add_task(Task("Feed breakfast", "08:00", Frequency.DAILY))
    whiskers.add_task(Task("Flea medication", "12:15", Frequency.WEEKLY))

    # Build and print today's schedule
    scheduler = Scheduler(owner)
    schedule = scheduler.get_daily_schedule()

    print("=" * 40)
    print(f"Today's Schedule for {owner.name}")
    print("=" * 40)
    for task in schedule:
        print(f"{task.time}  {task.description:<18} ({task.pet.name})")

    # Report any conflicts
    conflicts = scheduler.detect_conflicts(schedule)
    if conflicts:
        print("\nConflicts:")
        for group in conflicts:
            names = ", ".join(f"{t.pet.name}: {t.description}" for t in group)
            print(f"  {group[0].time} -> {names}")


if __name__ == "__main__":
    main()
