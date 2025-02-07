# src/ai_utils.py

"""
Utility functions for AI Kingdoms: Realm of Diplomacy.
This module provides support for loading and saving game states,
as well as utility functions for AI agent interactions.
"""

import json

# Placeholder for the game state storage location
GAME_STATE_FILE = "game_state.json"

def load_game_state():
    """
    Load the saved game state from a JSON file.
    If no saved state exists, return an empty dictionary.
    """
    try:
        with open(GAME_STATE_FILE, "r") as file:
            game_state = json.load(file)
            print("Game state loaded successfully.")
            return game_state
    except FileNotFoundError:
        print("No saved game state found. Starting fresh.")
        return {}

def save_game_state(game_state=None):
    """
    Save the current game state to a JSON file.
    :param game_state: Dictionary containing the current game state.
    """
    if game_state is None:
        game_state = {
            "player_data": {
                "player_name": "Player",
                "kingdom_status": "stable",
                "resources": {"gold": 500, "food": 300, "energy": 200},
            }
        }
    
    try:
        with open(GAME_STATE_FILE, "w") as file:
            json.dump(game_state, file, indent=4)
            print("Game state saved successfully.")
    except IOError as e:
        print(f"Error saving game state: {e}")

def calculate_resource_growth(current_resources, growth_rate=0.05):
    """
    Calculate the resource growth based on a growth rate.
    :param current_resources: Dictionary of current resource amounts.
    :param growth_rate: The growth rate to apply.
    :return: Updated resource dictionary with growth applied.
    """
    return {resource: amount + int(amount * growth_rate) for resource, amount in current_resources.items()}

def evaluate_diplomatic_outcome(player_choice, ai_response):
    """
    Evaluate the outcome of a diplomatic negotiation based on player and AI decisions.
    :param player_choice: The player's chosen negotiation strategy.
    :param ai_response: The AI's response to the player's strategy.
    :return: A result summary indicating success or failure.
    """
    if player_choice == "peace" and ai_response == "peace":
        return "Successful negotiation! Alliance formed."
    elif player_choice == "threat" and ai_response == "retreat":
        return "You dominated the negotiation!"
    else:
        return "
