questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Python", "B. Java", "C. C++", "D. SQL"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. string", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which database is commonly used with Python?",
        "options": ["A. SQLite", "B. HTML", "C. CSS", "D. XML"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
        "answer": "C"
    }
]


def start_quiz():
    score = 0
    answers = []

    print("\n--- QUIZ STARTED ---")

    for i, question in enumerate(questions, start=1):
        print("\nQuestion", i)
        print(question["question"])

        for option in question["options"]:
            print(option)

        user_answer = input("Enter your answer: ").upper()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

        answers.append((i, user_answer, question["answer"]))

    print("\n--- QUIZ COMPLETED ---")
    print("Your Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 60:
        print("Good performance!")
    elif percentage >= 40:
        print("Keep practicing!")
    else:
        print("Need more practice.")

    return answers


def view_score():
    print("\nScore is displayed after completing the quiz.")


def view_summary(answers):
    if not answers:
        print("\nNo quiz attempted yet.")
        return

    print("\n--- ANSWER SUMMARY ---")

    for question_no, user_answer, correct_answer in answers:
        print(
            "Question", question_no,
            "| Your Answer:", user_answer,
            "| Correct Answer:", correct_answer
        )


def main():
    answers = []

    while True:
        print("\n==============================")
        print("       QUIZ APPLICATION")
        print("==============================")

        print("1. Start Quiz")
        print("2. View Score")
        print("3. View Answer Summary")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            answers = start_quiz()

        elif choice == "2":
            view_score()

        elif choice == "3":
            view_summary(answers)

        elif choice == "4":
            print("Thank you for taking the quiz!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()