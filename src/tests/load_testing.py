# src/tests/load_testing.py

"""
Load Testing Script for AI Kingdoms
This script simulates multiple users interacting with the game system simultaneously
to measure performance and detect bottlenecks.
"""

import threading
import time
import random
from src.agents.diplomacy_agent import DiplomacyAgent
from src.ai_utils import load_game_state, save_game_state

# Number of simulated users
NUM_USERS = 50

# Simulated user actions
def simulated_user_action(user_id):
    agent = DiplomacyAgent()
    agent.initialize_kingdom(f"User_{user_id}")

    for _ in range(10):  # Simulate 10 actions per user
        action = random.choice(["negotiate", "resource_management", "view_status"])
        if action == "negotiate":
            print(f"[User {user_id}] Initiating negotiation...")
            agent.negotiate()
        elif action == "resource_management":
            print(f"[User {user_id}] Managing resources...")
            # Placeholder for resource management logic
            time.sleep(random.uniform(0.1, 0.5))  # Simulate action time
        elif action == "view_status":
            print(f"[User {user_id}] Viewing kingdom status...")
            # Placeholder for status viewing logic
            time.sleep(random.uniform(0.1, 0.5))  # Simulate action time

def load_test():
    print("Starting load test with multiple users...")
    threads = []

    # Create threads for each user
    for i in range(NUM_USERS):
        thread = threading.Thread(target=simulated_user_action, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Load test completed.")

if __name__ == "__main__":
    load_test()
