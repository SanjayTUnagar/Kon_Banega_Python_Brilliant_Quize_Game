
    print("=" * 40)
    print(question_bank[question_num]['question'])

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()

    is_correct = check_answer(guess, question_bank[question_num]["answer"]
    )
