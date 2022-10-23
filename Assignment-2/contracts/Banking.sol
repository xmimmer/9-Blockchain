//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

contract Banking {

    /*
    TODO
    Hold a number of accounts and balances       []
    Deposit and withdraw money                   []
    Get the balance of the requesters account    [x]
    Write JS code to test the contract           []
     Optionally write web-app using web3.js      []
    */

    mapping(address => uint256) private balances;   // balances, indexed by addresses

    function deposit() public payable returns(uint256) {
        balances[msg.sender] += msg.value;          // adjust the account's balance
        return balances[msg.sender];                // return remaining balance of user
    }

    function withdraw(uint256 amount) public {
        payable(msg.sender).transfer(amount);
        balances[msg.sender] -= amount; 

    }
    function getBalance() public view returns (uint256) {
        return balances[msg.sender]; 
    }

}

