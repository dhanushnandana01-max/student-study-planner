"""
Student Study Planner
---------------------
A simple beginner-friendly program that helps students
plan their study time before an exam.

Run this file to start the program:
    python main.py
"""

from study_planner import parse_subjects, display_timetable
from motivation import show_motivation_tip


def ask_positive_number(prompt, allow_zero=False):
    """
    Ask the user for a number until they enter a valid one.
    Returns the number as a float or int.
    """
    while True:
        answer = input(prompt).strip()

        try:
            value = float(answer)
            if value < 0:
                print("Please enter a number that is not negative.")
                continue
            if not allow_zero and value == 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("That is not a valid number. Please try again.")


def ask_subjects():
    """Ask for subjects until the user enters at least one."""
    while True:
        text = input("Enter your subjects (separated by commas): ").strip()
        subjects = parse_subjects(text)

        if subjects:
            return subjects

        print("Please enter at least one subject.")


def ask_weak_subjects(all_subjects):
    """
    Ask which subjects are weak.
    These will be studied first and get more hours.
    """
    print("\nWhich subjects do you find difficult or weak?")
    print("(Enter names separated by commas, or press Enter to skip)")

    text = input("Weak subjects: ").strip()
    weak_list = parse_subjects(text)

    # Only keep weak subjects that are actually in the student's subject list
    valid_weak = []
    for subject in weak_list:
        if subject in all_subjects:
            valid_weak.append(subject)
        else:
            print(f"  Note: '{subject}' is not in your subject list — skipped.")

    return valid_weak


def main():
    """Main program — asks questions and shows the study plan."""
    print("=" * 50)
    print("       WELCOME TO STUDENT STUDY PLANNER")
    print("=" * 50)
    print("Let's build your study timetable!\n")

    # 1. Ask student name
    name = input("What is your name? ").strip()
    if not name:
        name = "Student"

    # 2. Ask subjects
    subjects = ask_subjects()

    # Ask weak subjects (needed for requirement #6)
    weak_subjects = ask_weak_subjects(subjects)

    # 3. Ask study hours per day
    hours_per_day = ask_positive_number(
        "How many hours can you study per day? "
    )

    # 4. Ask days left until exam
    days_left = int(ask_positive_number(
        "How many days are left until your exam? "
    ))

    # 5 & 6. Create and show timetable (weak subjects prioritized inside)
    display_timetable(name, subjects, weak_subjects, hours_per_day, days_left)

    # 7. Show a motivational tip
    show_motivation_tip()

    print(f"\nGood luck with your studies, {name}!")
    print("You can run this program again anytime to update your plan.\n")


# This block runs only when you execute: python main.py
if __name__ == "__main__":
    main()
