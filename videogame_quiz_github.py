def run_quiz():
    # Dictionary of questions and their simple answers
    questions = {
        "What is the name of Mario's dinosaur friend?": "yoshi",
        "Which game features 'Master Chief' as the main hero?": "halo",
        "What is the name of the electric yellow Pokémon?": "pikachu",
        "In Minecraft, what is the green exploding monster called?": "creeper"
    }

    score = 0
    print("--- 🎮 Welcome to the Video Game Quiz! 🎮 ---")

    for question, answer in questions.items():
        user_answer = input(f"{question} ").lower().strip()
        if user_answer == answer:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong. The answer was {answer}. ❌")

    print(f"\nGame Over! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()