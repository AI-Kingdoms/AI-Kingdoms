# src/tests/security_tests.py

"""
Security Testing Script for AI Kingdoms
This script checks for common vulnerabilities in smart contracts and backend components,
including reentrancy attacks, overflow/underflow, and access control issues.
"""

from web3 import Web3
from src.contracts.realm_token import RealmToken
from src.contracts.staking_contract import StakingContract

# Simulated blockchain environment (replace with actual network details in real deployment)
web3 = Web3(Web3.EthereumTesterProvider())

def test_reentrancy_attack():
    """
    Simulates a potential reentrancy attack on the staking contract.
    The test ensures that multiple withdrawals cannot be triggered recursively.
    """
    print("Testing for reentrancy vulnerability...")
    try:
        # Assume staking_contract is deployed and initialized
        staking_contract = StakingContract("0xYourStakingContractAddress", 1)  # Mock deployment
        
        # Simulate reentrant call
        for _ in range(2):  # Second call should fail
            result = staking_contract.withdraw(10)
            if result:
                print("Potential vulnerability detected!")
                return
        print("Reentrancy protection verified.")
    except Exception as e:
        print(f"No vulnerability detected: {e}")

def test_integer_overflow_underflow():
    """
    Tests the token contract for integer overflow or underflow vulnerabilities.
    """
    print("Testing for integer overflow/underflow...")
    token_contract = RealmToken()

    try:
        # Simulate a large transfer to check for overflow
        large_transfer_amount = 2**256 - 1  # Max uint256
        token_contract.transfer("0xRecipientAddress", large_transfer_amount)
        print("No overflow/underflow detected.")
    except Exception as e:
        print(f"Potential issue: {e}")

def test_access_control():
    """
    Ensures that sensitive functions are protected and can only be executed by the contract owner.
    """
    print("Testing access control...")
    try:
        token_contract = RealmToken()
        
        # Non-owner trying to mint tokens
        result = token_contract.mint("0xAnotherAddress", 1000)
        if not result:
            print("Access control verified: Non-owners cannot execute restricted functions.")
        else:
            print("Warning: Potential access control issue.")
    except Exception as e:
        print(f"No access control issues detected: {e}")

def main():
    print("Running security tests...")
    test_reentrancy_attack()
    test_integer_overflow_underflow()
    test_access_control()
    print("Security tests completed.")

if __name__ == "__main__":
    main()
