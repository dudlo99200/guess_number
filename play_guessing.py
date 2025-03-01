import random

# Function to calculate the average of all guesses
def calculate_average(guesses):
    return sum(guesses) / len(guesses)

# Function to find the closest guess to the average
def find_winner(guesses, average):
    closest_player = None
    closest_diff = float('inf')
    
    for player, guess in guesses.items():
        diff = abs(guess - average)
        if diff < closest_diff:
            closest_diff = diff
            closest_player = player
    return closest_player

# Main game function
def play_game():
    print("Welcome to the Guessing Game!")

    # Get player name
    player_name = input("Enter your name: ")

    # Define bot names
    bot_names = ["Bot1", "Bot2", "Bot3", "Bot4"]

    # Store scores
    scores = {player_name: 0}
    for bot in bot_names:
        scores[bot] = 0

    # Play for 10 rounds
    rounds = 10

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        guesses = {}

        # Player's turn
        player_guess = int(input(f"{player_name}, guess a number between 0 and 100: "))
        guesses[player_name] = player_guess

        # Bots' turns (random guesses)
        for bot in bot_names:
            bot_guess = random.randint(0, 100)
            guesses[bot] = bot_guess
            print(f"{bot} guessed: {bot_guess}")

        # Calculate the average guess
        average = calculate_average(list(guesses.values()))
        print(f"Average guess: {average:.2f}")

        # Find the closest guess to the average
        winner = find_winner(guesses, average)
        print(f"{winner} wins this round and gets 10 points!")

        # Award points
        scores[winner] += 10

    # Find overall winner
    overall_winner = max(scores, key=scores.get)

    # Display final winner
    print(f"\nThe final winner is: {overall_winner} with {scores[overall_winner]} points!")

# Start the game
if __name__ == "__main__":
    play_game()