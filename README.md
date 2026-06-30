# Student Study Planner

A simple **beginner-friendly** Python project that helps students plan study time before an exam.

## What it does

1. Asks for your name
2. Asks for subjects (comma-separated)
3. Asks how many hours you can study per day
4. Asks how many days are left until the exam
5. Asks which subjects are weak (studied first with more time)
6. Creates a daily study timetable
7. Shows a random motivational tip

## Project files

| File | Purpose |
|------|---------|
| `main.py` | Starts the program and asks questions |
| `study_planner.py` | Builds and displays the timetable |
| `motivation.py` | Shows motivational study tips |

## Requirements

- **Python 3.6 or newer** (no extra packages needed)

Check your version:

```bash
python --version
```

On some systems you may need `python3` instead of `python`.

## How to run

1. Open a terminal (Command Prompt or PowerShell on Windows).
2. Go to the project folder:

```bash
cd c:\Users\dhanu\OneDrive\Desktop\student-study-planner
```

3. Run the main file:

```bash
python main.py
```

4. Answer the questions when prompted.

### Example session

```
What is your name? Alex
Enter your subjects (separated by commas): Math, Physics, English
Weak subjects: Math, Physics
How many hours can you study per day? 4
How many days are left until your exam? 5
```

The program will print a day-by-day timetable and a motivation tip.

## How weak subjects are prioritized

- Weak subjects are listed **first** each day.
- Weak subjects receive **more total hours** than other subjects.
- In the timetable, weak blocks are marked with `[WEAK - study first]`.

## Tips for beginners

- Read the comments in each `.py` file to understand how the code works.
- Try changing the `TIPS` list in `motivation.py` to add your own messages.
- Run the program several times with different inputs to see how the plan changes.

## License

Free to use for learning and school projects.
