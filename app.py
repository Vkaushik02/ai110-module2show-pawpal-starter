import streamlit as st
from pawpal_system import Frequency, Owner, Pet, Scheduler, Task

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

owner = st.session_state.owner  # always use this reference afterward

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Add a Pet")
with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=40, value=1)
    if st.form_submit_button("Add pet"):
        if pet_name.strip():
            owner.add_pet(Pet(name=pet_name.strip(), species=species, age=int(age)))
            st.success(f"Added {pet_name}!")
        else:
            st.error("Pet name is required.")

st.subheader("Schedule a Task")
if not owner.pets:
    st.info("Add a pet first.")
else:
    with st.form("add_task_form"):
        # select by index: st.selectbox returns a copy of object options, not the original
        pet_index = st.selectbox(
            "Pet", range(len(owner.pets)), format_func=lambda i: owner.pets[i].name
        )
        pet_choice = owner.pets[pet_index]
        description = st.text_input("Task description", value="Morning walk")
        task_time = st.time_input("Time")
        frequency = st.selectbox(
            "Frequency", list(Frequency), format_func=lambda f: f.value
        )
        due = st.date_input("Due date")
        if st.form_submit_button("Add task"):
            pet_choice.add_task(
                Task(
                    description=description,
                    time=task_time.strftime("%H:%M"),  # keeps string sorting chronological
                    frequency=frequency,
                    due_date=due,
                )
            )
            st.success(f"Scheduled '{description}' for {pet_choice.name}.")

st.divider()
st.subheader("Today's Schedule")
scheduler = Scheduler(owner)
schedule = scheduler.get_daily_schedule()

for conflict in scheduler.detect_conflicts(schedule):
    names = ", ".join(f"{t.pet.name}: {t.description}" for t in conflict)
    st.warning(f"⚠️ Conflict at {conflict[0].time}: {names}")

if schedule:
    for i, task in enumerate(schedule):
        col1, col2 = st.columns([4, 1])
        col1.write(f"**{task.time}** — {task.pet.name}: {task.description} ({task.frequency.value})")
        if col2.button("Done", key=f"done_{i}_{id(task)}"):
            task.mark_complete()  # queues the next occurrence for daily/weekly tasks
            st.rerun()
else:
    st.info("Nothing scheduled for today.")
