"""
Study timetable logic.
Creates a daily plan that puts weak subjects first and gives them more time.
"""


def parse_subjects(subjects_text):
    """
    Turn a comma-separated string into a clean list of subject names.
    Example: "Math, Science, English" -> ["Math", "Science", "English"]
    """
    subjects = []
    for name in subjects_text.split(","):
        cleaned = name.strip()
        if cleaned:
            subjects.append(cleaned)
    return subjects


def get_priority_order(subjects, weak_subjects):
    """
    Put weak subjects at the front of the list.
    Other subjects follow in their original order.
    """
    priority = []

    # Add weak subjects first (only if they are in the main subject list)
    for subject in subjects:
        if subject in weak_subjects:
            priority.append(subject)

    # Add remaining subjects
    for subject in subjects:
        if subject not in priority:
            priority.append(subject)

    return priority


def calculate_hours_per_subject(subjects, weak_subjects, total_hours):
    """
    Split total study hours across subjects.
    Weak subjects get double weight (more study time).
    """
    if not subjects:
        return {}

    weights = {}
    for subject in subjects:
        if subject in weak_subjects:
            weights[subject] = 2  # weak = more time
        else:
            weights[subject] = 1

    total_weight = sum(weights.values())
    hours_map = {}

    for subject in subjects:
        share = (weights[subject] / total_weight) * total_hours
        hours_map[subject] = round(share, 1)

    return hours_map


def build_daily_schedule(priority_subjects, hours_per_day, weak_subjects):
    """
    Build one day's timetable as a list of (subject, hours) pairs.
    Weak subjects appear first in the day.
    """
    daily_hours = calculate_hours_per_subject(
        priority_subjects, weak_subjects, hours_per_day
    )

    schedule = []
    for subject in priority_subjects:
        hours = daily_hours.get(subject, 0)
        if hours > 0:
            schedule.append((subject, hours))

    return schedule


def create_timetable(student_name, subjects, weak_subjects, hours_per_day, days_left):
    """
    Create a full study plan for all days until the exam.
    Returns a list of day plans; each day plan is a list of (subject, hours).
    """
    priority = get_priority_order(subjects, weak_subjects)
    timetable = []

    for day_number in range(1, days_left + 1):
        day_plan = build_daily_schedule(priority, hours_per_day, weak_subjects)
        timetable.append((day_number, day_plan))

    return timetable


def display_timetable(student_name, subjects, weak_subjects, hours_per_day, days_left):
    """Print the study timetable in a readable format."""
    timetable = create_timetable(
        student_name, subjects, weak_subjects, hours_per_day, days_left
    )

    total_hours = hours_per_day * days_left
    hours_per_subject = calculate_hours_per_subject(subjects, weak_subjects, total_hours)

    print("\n" + "=" * 50)
    print(f"  STUDY PLAN FOR {student_name.upper()}")
    print("=" * 50)
    print(f"Exam in: {days_left} day(s)")
    print(f"Study time per day: {hours_per_day} hour(s)")
    print(f"Subjects: {', '.join(subjects)}")

    if weak_subjects:
        print(f"Weak subjects (priority): {', '.join(weak_subjects)}")
    else:
        print("Weak subjects: none marked")

    print("\n--- Total hours per subject (all days) ---")
    for subject in get_priority_order(subjects, weak_subjects):
        print(f"  {subject}: {hours_per_subject.get(subject, 0)} hours")

    print("\n--- Daily Timetable ---")
    for day_number, day_plan in timetable:
        print(f"\nDay {day_number}:")
        if not day_plan:
            print("  (No study blocks — check your inputs.)")
            continue

        for subject, hours in day_plan:
            label = " [WEAK - study first]" if subject in weak_subjects else ""
            print(f"  -> {subject}: {hours} hour(s){label}")

    print("\n" + "=" * 50)
