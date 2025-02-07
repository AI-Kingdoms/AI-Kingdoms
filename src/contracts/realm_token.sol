// src/contracts/realm_token.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title $REALM Token Contract
/// @notice ERC20 token used within the AI Kingdoms ecosystem for in-game transactions, staking, and governance.
contract RealmToken is ERC20, Ownable {
    
    /// @dev Initial supply is set to 1 billion $REALM tokens.
    uint256 private constant INITIAL_SUPPLY = 1_000_000_000 * (10 ** 18);

    constructor() ERC20("RealmToken", "REALM") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /// @notice Mint additional tokens (restricted to contract owner).
    /// @param to The address that will receive the newly minted tokens.
    /// @param amount The number of tokens to be minted.
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /// @notice Burn tokens to reduce total supply.
    /// @param amount The number of tokens to be burned.
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /// @notice Allow players or other contracts to transfer tokens on behalf of others.
    /// @param from The address to transfer tokens from.
    /// @param to The address to transfer tokens to.
    /// @param amount The amount of tokens to transfer.
    /// @return A boolean indicating the success of the transfer.
    function transferFrom(
        address from, 
        address to, 
        uint256 amount
    ) public override returns (bool) {
        return super.transferFrom(from, to, amount);
    }

    /// @dev Emergency function to withdraw accidentally sent ETH from the contract.
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
