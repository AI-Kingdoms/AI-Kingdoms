# src/game_main.py

"""
Main game logic for AI Kingdoms: Realm of Diplomacy.
This module initializes the game environment, connects to the blockchain,
and manages interactions between players and AI agents.
"""

import sys
from src.agents.diplomacy_agent import DiplomacyAgent
from src.contracts.blockchain_interface import BlockchainInterface
from src.ai_utils import load_game_state, save_game_state

# Initialize core components
blockchain = BlockchainInterface()
diplomacy_agent = DiplomacyAgent()

def main():
    print("Welcome to AI Kingdoms: Realm of Diplomacy!")
    
    # Load initial game state
    game_state = load_game_state()

    # Display starting options
    print("\nMain Menu:")
    print("1. Start New Game")
    print("2. Load Existing Game")
    print("3. Exit")

    # Get user input
    choice = input("Enter your choice: ")

    if choice == "1":
        start_new_game()
    elif choice == "2":
        load_existing_game(game_state)
    elif choice == "3":
        print("Thank you for playing AI Kingdoms!")
        sys.exit(0)
    else:
        print("Invalid choice. Please restart the game.")

def start_new_game():
    print("\nStarting a new game...")
    # Initialize player and kingdom settings
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}! Establishing your kingdom...")
    
    # Initialize blockchain connection for game transactions
    blockchain.initialize_player(player_name)
    diplomacy_agent.initialize_kingdom(player_name)

    print("Your kingdom is ready! The game begins...")
    # Main game loop
    run_game_loop()

def load_existing_game(game_state):
    print("\nLoading saved game state...")
    # Load player progress
    player_data = game_state.get('player_data', {})
    print(f"Welcome back, {player_data.get('player_name', 'Player')}!")
    run_game_loop()

def run_game_loop():
    while True:
        print("\nWhat would you like to do?")
        print("1. Negotiate with other kingdoms")
        print("2. Manage resources")
        print("3. View kingdom status")
        print("4. Save and Exit")

        action = input("Choose an action: ")

        if action == "1":
            diplomacy_agent.negotiate()
        elif action == "2":
            manage_resources()
        elif action == "3":
            view_kingdom_status()
       
