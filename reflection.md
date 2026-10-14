# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- The app would let a user add a new pet profile, schedule a pet care task with specific time, priority, and frequency constraints, and generate a daily plan that chronologically sorts tasks and alerts the owner of time conflicts.
- My initial UML design organizes these actions across four primary classes:
    - Task: Represents a single activity, holding attributes for description, time, frequency, and completion status.
    - Pet: Represents an animal profile, storing pet details and a list of their specific assigned Tasks.
    - Owner: The central profile manager that links multiple pets together and uses a method to aggregate everything.
    - Scheduler: The system's brain that reads tasks from the Owner to sort the day's schedule chronologically and flag time conflicts.

**b. Design changes**

- Yes, I made changes: I added a frequency enum, a due date on tasks, and a pet reference on tasks, and I changed the mark complete logic.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- The scheduler considers time constraints: each task has a time, which is used to sort tasks and to detect conflicts. The date is also considered and used in conflict detection. I decided what mattered most by asking what a pet owner needs to know in order to know what to do. This led me to pick time and date as the two constraints.

**b. Tradeoffs**

- One tradeoff it makes is exact time matching instead of overlap detection. `detect_conflicts` groups tasks by time, and two tasks are in conflict only if their time strings are identical. This is reasonable because it is simple, fast, and predictable.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI for UML design and brainstorming. The most useful prompts were those with many details and clear goals, like this one: "I am designing a pet care app with Owner, Pet, Task, and Scheduler classes. Create a Mermaid.js class diagram based on these requirements." It gives the AI the exact steps and goals.

**b. Judgment and verification**

- The AI suggested a highly nested approach where the Scheduler directly accessed and manipulated individual task arrays inside the Pet instances by looping through them manually. I did not accept this suggestion. I evaluated it by comparing it against our system guidelines, and realized that the Scheduler should dynamically pull consolidated data from the Owner layer instead of managing individual pet objects directly. To verify my revised approach, I tested the code using test cases.

---

## 4. Testing and Verification

**a. What you tested**

- I tested four areas. One was the basics, like adding tasks and increasing the task count. I also tested sorting by time, recurrence (daily, weekly, and one-time), and conflict detection. These tests were important because sorting, conflict detection, and recurrence are the core of the program. If one of them is wrong, the owner would see a misleading plan.

**b. Confidence**

- I am confident in the scheduler because all the test cases passed. I would rate my confidence 4 out of 5, as that matches how I feel. If I had more time, I would test invalid times, and removing a task or pet and checking that the back reference is cleared.

---

## 5. Reflection

**a. What went well**

- I am satisfied with all the parts, as they all took a lot of time and effort.

**b. What you would improve**

- I would redesign the UI, as right now it is very simple and basic.

**c. Key takeaway**

- The most important thing I learned is that a UML diagram is a starting point, not a finished plan. My initial design changed as I built it. I added things and changed how methods worked.
