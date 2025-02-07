# src/tests/integration_tests.py

"""
Integration Testing Script for AI Kingdoms
This script tests the integration of core components, including the interaction
between the game logic, AI agents, and blockchain contracts.
"""

from src.game_main import main as game_main
from src.agents.diplomacy_agent import DiplomacyAgent
from src.contracts.realm_token import RealmToken
from src.contracts.staking_contract import StakingContract

def test_game_startup():
    """
    Tests the game startup process to ensure the main components initialize correctly.
    """
    print("Testing game startup...")
    try:
        game_main()
        print("Game startup test passed.")
    except Exception as e:
        print(f"Game startup test failed: {e}")

def test_agent_blockchain_interaction():
    """
    Tests the interaction between AI agents and blockchain contracts, such as
    staking $REALM tokens and handling NFT-based assets.
    """
    print("Testing agent-blockchain interaction...")
    try:
        # Initialize AI agent
        agent = DiplomacyAgent()
        agent.initialize_kingdom("IntegrationTestUser")

        # Initialize blockchain interactions
        realm_token = RealmToken()
        staking_contract = StakingContract("0xYourStakingContractAddress", 1)  # Mock deployment

        # Simulate staking tokens
        realm_token.mint("0xIntegrationUserAddress", 1000)
        print("Minting successful.")

        staking_contract.stake(500)
        print("Staking interaction test passed.")
    except Exception as e:
        print(f"Agent-blockchain interaction test failed: {e}")

def test_diplomatic_action_flow():
    """
    Tests the complete flow of a diplomatic action from user input, AI response,
    and resulting game state updates.
    """
    print("Testing diplomatic action flow...")
    try:
        agent = DiplomacyAgent()
        agent.initialize_kingdom("DiplomaticTestUser")

        print("Simulating negotiation...")
        agent.negotiate()
        print("Diplomatic action flow test passed.")
    except Exception as e:
        print(f"Diplomatic action flow test failed: {e}")

def main():
    print("Running integration tests...")
    test_game_startup()
    test_agent_blockchain_interaction()
    test_diplomatic_action_flow()
    print("Integration tests completed.")

if __name__ == "__main__":
    main
