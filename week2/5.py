quiz = {
    "1. Which is the currency of Kazakhstan ? ": {"Tenge", "KZT"},
    "2. Name one of the past/present presidents of Kazakhstan: ": {"Nazarbayev", "Tokayev"},
    "3. What year Kazakhstan proclaim independence? ": "1991"
}

counter = 0
for question, answer in quiz.items():
    user_answer = input(question)
    if user_answer in answer:
        counter += 1

result_perc = (counter / len(quiz)) * 100
user_won = True if result_perc > 70 else False
if user_won:
    print(f"Congrats, you won with {result_perc:.2f}% correctness")
else:
    print(f"You lost! You got only {result_perc:.2f}% correctness")