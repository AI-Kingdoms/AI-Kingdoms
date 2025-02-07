// src/contracts/staking_contract.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Staking Contract for $REALM Tokens
/// @notice This contract allows players to stake $REALM tokens and earn rewards over time.
contract StakingContract is Ownable {

    IERC20 public realmToken;
    uint256 public rewardRate;  // Reward rate per block
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastUpdated;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    /// @notice Event emitted when tokens are staked.
    event Staked(address indexed user, uint256 amount);

    /// @notice Event emitted when rewards are claimed.
    event RewardsClaimed(address indexed user, uint256 reward);

    /// @notice Event emitted when tokens are withdrawn.
    event Withdrawn(address indexed user, uint256 amount);

    /// @dev Constructor initializes the contract with the $REALM token and reward rate.
    /// @param tokenAddress Address of the $REALM token.
    /// @param initialRewardRate The initial reward rate per block.
    constructor(address tokenAddress, uint256 initialRewardRate) {
        realmToken = IERC20(tokenAddress);
        rewardRate = initialRewardRate;
    }

    /// @notice Stake $REALM tokens.
    /// @param amount The amount of tokens to stake.
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update the user's reward before modifying the stake amount
        updateRewards(msg.sender);

        // Transfer the tokens from the user to the contract
        realmToken.transferFrom(msg.sender, address(this), amount);

        // Update stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastUpdated = block.number;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Claim staking rewards.
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        realmToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /// @notice Withdraw staked tokens along with any earned rewards.
    /// @param amount The amount of tokens to withdraw.
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        updateRewards(msg.sender);

        user
