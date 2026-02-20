import random

def get_round_result(player, computer, rules_dict):
    if player == computer:
        return "tie"
    elif rules_dict[player] == computer:
        return "win"
    else:
        return "lose"

rules_dict = {"rock": "scissor", "paper": "rock", "scissor": "paper"}
choices = list(rules_dict.keys())


p_score = 0
c_score = 0

while True:
    player_choose = input("Enter rock, paper, or scissor (exit to quit): ").lower().strip()

    if player_choose == "exit":
        print(f"Final Score -> You: {p_score} | Computer: {c_score}")
        break

    if player_choose not in rules_dict:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    result = get_round_result(player_choose, computer, rules_dict)

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
        p_score += 1
    else:
        print("You lose!")
        c_score += 1

    print(f"Current Score -> You: {p_score} | Computer: {c_score}")
    print("-" * 20)
