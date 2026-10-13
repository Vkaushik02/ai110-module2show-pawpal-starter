# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

- So it would be add a new pet profile, scheduling a pet care task with specific time, priority, and frequency constraints, and generating a daily plan that chronologically sorts tasks and alerts the owner of time conflicts.
- My initial UML design organizes these actions across four primary classes:
    - Task: Represents a single activity, holding attributes for description, time, frequency, and completion status.
    - Pet: Represents an animal profile, storing pet details and a list of their specific assigned Tasks.
    - Owner: The central profile manager that links multiple pets together and uses a method to aggregate everything.
    - Scheduler: The system's brain that reads tasks from the Owner to sort the day's schedule chronologically and flag time conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
- yes the changes made were adding frequency enum, due date on tasks, pet refrence on taks, and changed mark complete logic.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

- I used AI for design of uml and brainstorming. The most useful prompt were the those with many detials and clear goals. Like this one "I am designing a pet care app with Owner, Pet, Task, and Scheduler classes. Create a Mermaid.js class diagram based on these requirements." as this gives the AI the exact steps and goals. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

- The AI suggested a highly nested approach where the Scheduler directly accessed and manipulated individual task arrays inside the Pet instances by looping through them manually. I did not accept this suggestion. I evaluated the suggestion by comparing it against our system guidelines, realizing that the Scheduler should dynamically pull consolidated data from the Owner layer instead of managing individual pet objects directly. To verify my revised approach I tested need code using test cases. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
