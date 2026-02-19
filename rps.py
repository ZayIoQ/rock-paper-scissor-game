import random
while True:
    rules_dict = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper"
    }

    choices = list(rules_dict.keys())
    computer = random.choice(choices)
    player_choose = input("Enter rock, paper, or scissor (write 'exit' to quit): ").lower().strip()
    if player_choose == "exit":
        print("Thank you for playing!")
        break



    print(f"Computer chose: {computer}")

    if player_choose not in rules_dict:
        print("Invalid choice!")
    elif player_choose == computer:
        print("It's a tie!")
    elif rules_dict[player_choose] == computer:

        print("You win!")
    else:
        print("You lose!")