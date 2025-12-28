def run_quiz():
    # Dictionary of Deus Ex (2000) trivia
    questions = {
        "What is the name of the protagonist?": "jc denton",
        "What is the name of the organization the protagonist works for at the start?": "unatco",
        "What is the name of the deadly virus plague?": "gray death",
        "What is the name of the protagonist's brother?": "paul"
    }

    score = 0
    print("--- 🕶️ Welcome to the Deus Ex Conspiracy Quiz 🕶️ ---")
    print("Trust no one. Answer carefully.\n")

    for question, answer in questions.items():
        user_answer = input(f"{question} ").lower().strip()
        if user_answer == answer:
            print("Access Granted. ✅")
            score += 1
        else:
            print(f"Access Denied. The correct data was: {answer}. ❌")

    print(f"\nSummary: You recovered {score}/{len(questions)} data fragments.")

if __name__ == "__main__":
    run_quiz()