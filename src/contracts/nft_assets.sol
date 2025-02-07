// src/contracts/nft_assets.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFT Contract for In-Game Assets
/// @notice This contract manages the tokenization of in-game assets like territories and buildings within the AI Kingdoms ecosystem.
contract NFTAssets is ERC721URIStorage, Ownable {

    uint256 private nextTokenId;

    /// @notice Event emitted when a new NFT is minted.
    event AssetMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /// @dev Constructor initializes the NFT collection name and symbol.
    constructor() ERC721("AIKingdomAsset", "AIA") {
        nextTokenId = 1;  // Start token IDs from 1
    }

    /// @notice Mint a new NFT representing an in-game asset.
    /// @param recipient The address to receive the newly minted NFT.
    /// @param tokenURI A URI pointing to the metadata of the NFT.
    /// @return The token ID of the newly minted NFT.
    function mintAsset(address recipient, string memory tokenURI) public onlyOwner returns (uint256) {
        uint256 currentTokenId = nextTokenId;
        _mint(recipient, currentTokenId);
        _setTokenURI(currentTokenId, tokenURI);

        emit AssetMinted(recipient, currentTokenId, tokenURI);
        
        nextTokenId++;  // Increment the token ID for the next asset
        return currentTokenId;
    }

    /// @notice Burn an existing NFT to remove it from circulation.
    /// @param tokenId The ID of the token to be burned.
    function burnAsset(uint256 tokenId) public {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner or approved");
        _burn(tokenId);
    }

    /// @notice Get the current supply of minted NFTs.
    /// @return The total number of NFTs minted so far.
    function getTotalM
