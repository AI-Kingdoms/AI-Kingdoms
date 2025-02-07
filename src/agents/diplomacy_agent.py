# src/agents/diplomacy_agent.py

"""
Diplomacy Agent for AI Kingdoms: Realm of Diplomacy.
This module defines an AI agent responsible for managing diplomatic interactions
with other factions and providing recommendations to the player.
"""

import random

class DiplomacyAgent:
    def __init__(self):
        self.kingdom_status = {}
        print("Diplomacy Agent initialized.")

    def initialize_kingdom(self, player_name):
        """
        Initialize the player's kingdom with default diplomatic settings.
        :param player_name: The name of the player establishing the kingdom.
        """
        self.kingdom_status = {
            "player_name": player_name,
            "alliances": [],
            "hostilities": [],
            "neutral_factions": ["Northern Empire", "Eastern Tribes", "Western Kingdoms"]
        }
        print(f"Kingdom initialized for player: {player_name}")

    def negotiate(self):
        """
        Perform a diplomatic action with a random faction.
        The player chooses a negotiation strategy, and the AI responds dynamically.
        """
        if not self.kingdom_status["neutral_factions"]:
            print("No neutral factions available for negotiation.")
            return

        # Choose a random faction for negotiation
        target_faction = random.choice(self.kingdom_status["neutral_factions"])
        print(f"Negotiating with the {target_faction}...")

        # Player chooses a negotiation strategy
        player_strategy = input("Choose a strategy (peace/threat): ").strip().lower()
        if player_strategy not in ["peace", "threat"]:
            print("Invalid strategy. Defaulting to peace.")
            player_strategy = "peace"

        # AI randomly decides its response
        ai_response = random.choice(["peace", "retreat", "counter"])
        print(f"The {target_faction} responds with {ai_response}.")

        # Evaluate the outcome
        result = self.evaluate_diplomatic_outcome(player_strategy, ai_response, target_faction)
        print(result)

    def evaluate_diplomatic_outcome(self, player_strategy, ai_response, target_faction):
        """
        Evaluate the result of a diplomatic negotiation based on strategies and responses.
        :param player_strategy: The player's chosen strategy (peace/threat).
        :param ai_response: The AI's chosen response (peace/retreat/counter).
        :param target_faction: The faction involved in the negotiation.
        :return: A string summarizing the outcome of the negotiation.
        """
        if player_strategy == "peace" and ai_response == "peace":
            self.kingdom_status["alliances"].append(target_faction)
            self.kingdom_status["neutral_factions"].remove(target_faction)
            return f"Successful negotiation! You have formed an alliance with the {target_faction}."

        elif player_strategy == "threat" and ai_response == "retreat":
            self.kingdom_status["alliances"].append(target_faction)
            self.kingdom_status["neutral_factions"].remove(target_faction)
            return f"You dominated the negotiation! The {target_faction} has surrendered and joined your alliance."

        elif ai_response == "counter":
            self.kingdom_status["hostilities"].append(target_faction)
            self.kingdom_status["neutral_factions"].remove(target_faction)
            return f"Negotiation failed.
