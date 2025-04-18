import random
import time

# Sample questions
questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": "Tuple"
    }
]

def run_quiz():
    score = 0
    print("📘 Welcome to Python Exam Prep! 🐍\n")

    for q in questions:
        print(f"\n{q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        answer = input("Your answer (1-4): ")
        selected_option = q["options"][int(answer) - 1]

        if selected_option == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct answer: {q['answer']}")

    print(f"\n📊 Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
