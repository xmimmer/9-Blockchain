//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

contract Banking {

     mapping(address => uint256) private balances;   // balances, indexed by addresses

    function deposit() public payable returns(uint256) {
        balances[msg.sender] += msg.value;          // adjust the account's balance
        return balances[msg.sender];                // return remaining balance of user
    }

    function withdraw(uint256 amount) public {
        payable(msg.sender).transfer(amount);       // withdraw from user 
        balances[msg.sender] -= amount;             // adjust user balance

    }
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];                // display user balance
    }

}

