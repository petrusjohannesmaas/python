// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.8.18;

contract SimpleMapping {
    // Mapping from a uint to a uint
    mapping(uint256 => uint256) public data;

    // Function to set a value in the mapping
    function set(uint256 key, uint256 value) public {
        data[key] = value;
    }

    // Function to get a value from the mapping
    function get(uint256 key) public view returns (uint256) {
        return data[key];
    }
}
