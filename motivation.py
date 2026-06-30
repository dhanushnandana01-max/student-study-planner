"""
Motivational tips for students.
This file stores tips and shows a random one to the user.
"""

import random


# List of simple motivational tips for students
TIPS = [
    "Study in short blocks (25–30 minutes), then take a 5-minute break.",
    "Start with your hardest subject when your mind is fresh.",
    "Write down what you learned today — it helps memory.",
    "Sleep well! Your brain stores information while you rest.",
    "Turn off notifications while studying to stay focused.",
    "Teach a topic to a friend — if you can explain it, you know it.",
    "Review yesterday's notes before starting something new.",
    "Keep water nearby and stay hydrated during study sessions.",
    "Set a small daily goal. Finishing it builds confidence.",
    "Believe in yourself — every expert was once a beginner!",
]


def show_motivation_tip():
    """Pick and print one random motivational tip."""
    tip = random.choice(TIPS)
    print("\n--- Motivation Tip ---")
    print(tip)
    print("----------------------")
