import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "player" if wins[player] == computer else "computer"

def display_result(player, computer, result):
    symbols = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    print(f"\n  You:      {symbols[player]}   {player.capitalize()}")
    print(f"  Computer: {symbols[computer]}  {computer.capitalize()}")  # ✅ Bug 1 Fixed
    print()
    if result == "tie":
        print("  🤝 It's a tie!")
    elif result == "player":
        print("  🎉 You win!")
    else:
        print("  💻 Computer wins!")

def play():
    print("=" * 35)
    print("   🎮 Rock Paper Scissors Game")
    print("=" * 35)

    player_score = 0
    computer_score = 0
    ties = 0
    round_num = 0

    while True:
        print(f"\n Score ➜  You: {player_score} | CPU: {computer_score} | Ties: {ties}")
        print("\n Choose: ")
        print("  [1] 🪨  Rock")
        print("  [2] 📄 Paper")
        print("  [3] ✂️  Scissors")
        print("  [q] Quit")

        choice = input("\n Enter choice: ").strip().lower()

        mapping = {"1": "rock", "2": "paper", "3": "scissors",
                   "rock": "rock", "paper": "paper", "scissors": "scissors"}

        if choice == "q":
            break
        elif choice not in mapping:
            print(" Error: ⚠️  Invalid choice. Please enter 1, 2, 3, or q.")
            continue

        player = mapping[choice]
        computer = get_computer_choice()
        result = determine_winner(player, computer)
        round_num += 1

        print(f"\n--- Round {round_num} ---")
        display_result(player, computer, result)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1  # ✅ Bug 2 Fixed
        else:
            ties += 1

    # ✅ Bug 3 Fixed — outside the loop
    print(f"\n{'=' * 35}")
    print("         📊 Final Results")
    print("=" * 35)
    print(f"    Rounds Played: {round_num}")  # ✅ Bug 4 Fixed
    print(f"    Your Wins    : {player_score}")
    print(f"    CPU Wins     : {computer_score}")
    print(f"    Ties         : {ties}")

    if player_score > computer_score:
        print("\n  🏆 Overall Winner: YOU!")
    elif computer_score > player_score:
        print("\n  🤖 Overall Winner: Computer!")
    else:
        print("\n 🤝 Overall Result: It's a tie!")

    print("=" * 35)
    print("  Thanks for playing!\n")

if __name__ == "__main__":
    play()