# Homework 3 - Board Game System
# Name: Olivia Sulzle
# Date: 4/5/26

import random

WIN_POSITION = 30

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    raw_data = []
    try:
        with open(filename, "r") as file:
            for line in file:
                raw_data.append(line.strip())
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    state = {"turn": "", "players": {}, "events": {}}
    for line in raw_data:
        if "Turn:" in line:
            state["turn"] = line.split(": ")[1]
        elif ":" in line:
            parts = line.split(": ")
            pos = int(parts[0])
            label = parts [1]
            if "Player" in label:
                state["players"][label] = pos
            else:
                state["events"][pos] = label
    return state

def displayGame(state):
    """Displays the current game state."""
    print("\n" + "="*30)
    print(f"Current Turn: {state['turn']}")
    print("="*30)

    board_size = 30
    board = ["_"] * (board_size + 1)

    for pos, name in state["events"].items():
        board[pos] = "!"

    for name, pos in state["players"].items():
        board[pos] = name[6]

    print("Board: " + "".join(board))
    print("-" * 30)
    for name, pos in state["players"].items():
        print(f"{name} is at position {pos}")

def movePlayer(state):
    """Example function to simulate moving a player."""
    current_player = state["turn"]
    roll = random.randint(1, 6)
    old_pos = state["players"][current_player]
    new_pos = old_pos + roll

    if new_pos > WIN_POSITION:
        new_pos = WIN_POSITION
    
    state["players"][current_player] = new_pos
    print(f"\n{current_player} rolled a {roll} and moved to {new_pos}!")

    if new_pos in state["events"]:
        event = state["events"][new_pos]
        print(f"Event Triggered: {event}!")

    winner = None
    if new_pos == WIN_POSITION:
        winner = current_player
    else:
        if current_player == "Player1":
            state["turn"] = "Player2"
        else:
            state["turn"] = "Player1"

    return state, winner


def main():
    filename = "events.txt"   # Students can rename if needed

    game_state = loadGameData(filename)
    if game_state is None:
        return

    running = True
    while running:
        displayGame(game_state)
        choice = input("\nMove player? (y/n) or 'q' to quit: ")

        if choice == "y":
            game_state, winner = movePlayer(game_state)
            if winner:
                displayGame(game_state)
                print(f"\n{winner} wins the game!")
                running = False
        elif choice == "q" or choice == "n":
            print("Closing game. Goodbye!")
            running = False

if __name__ == "__main__":
    main()
