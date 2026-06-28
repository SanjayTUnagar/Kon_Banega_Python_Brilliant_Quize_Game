# main.py - Run this file to start the game


from quiz_database import question_bank
from quiz_database import options

print("\n" + "=" * 40)
print("      🎯 Welcome to KBPB QUIZ GAME")
print("=" * 40)

score = 0

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

for question_num in range(len(question_bank)):

    print("=" * 40)
    print(question_bank[question_num]["question"])

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()

    is_correct = check_answer(guess, question_bank[question_num]["answer"]
    )

    if is_correct:
        print("✅ Correct Answer")
        score += 1
    else:
        print("❌ Wrong! Answer")
        print(f"Correct answer was: {question_bank[question_num]['answer']}")

    print(f"🌟 Your Correct Score is {score}/{question_num + 1}")
    print(f"👍 You have given to {score} Correct Answer")
    print(f"😊 Your Score is {(score/len(question_bank)) * 100}%")


print("\n" + "=" * 40)
print(" 📊 FINAL RESULTS")
print("Quiz Completed")
print(f"Your Score: {score}/{len(question_bank)}")
print("  THANK YOU.....")
print("=" * 40)




















'''def main():
    """Main function - game loop."""
    print("\n  Welcome to the Kon Banega Python Brilliant Quiz Game! 🎓")
    player_name = get_player_name()
    print(f"\n  Hello, {player_name}! Let's get started.")

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            questions = QUESTIONS
            print(f"\n  🎮 Starting quiz with all {len(questions)} questions...")

        elif choice == "2":
            questions = random.sample(QUESTIONS, 5)
            print("\n  🎮 Starting quiz with 5 random questions...")

        elif choice == "3":
            questions = QUESTIONS
            print(f"\n  ⏱️  Timed mode! {len(questions)} questions, 15 seconds each...")

        elif choice == "4":
            print(f"\n  👋 Thanks for playing, {player_name}! Goodbye!\n")
            break

        timed = (choice == "3")
        score, wrong_answers = run_quiz(questions, timed=timed)
        show_result(score, len(questions), wrong_answers)

        play_again = input("\n  Play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print(f"\n  👋 Thanks for playing, {player_name}! Goodbye!\n")
            break


if __name__ == "__main__":
    main()
'''