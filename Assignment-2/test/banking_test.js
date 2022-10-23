const Banking = artifacts.require("Banking")

//Converting values
const ether = 10**18

contract("Banking - Deposit & Balance Functions", (accounts) => {
    const mads = accounts[1];
    const peffen = accounts[2]; 
    const lukas = accounts[3]; 

    it("Balance should be 0", async () => {
        const bankingInstance = await Banking.deployed();

        const balance_mads = await bankingInstance.getBalance({from: mads}); 
        assert.equal(balance_mads, 0, "Incorrect"); 

        const balance_peffen = await bankingInstance.getBalance({from: peffen}); 
        assert.equal(balance_peffen, 0, "Incorrect"); 

        const balance_lukas = await bankingInstance.getBalance({from: lukas}); 
        assert.equal(balance_lukas, 0, "Incorrect"); 
    });

 it("Verifying deposit function", async() => {
        const amount = 2*ether
        const bankingInstance = await Banking.deployed(); 

        await bankingInstance.deposit({from: mads, value: amount});
        const balance_mads = await bankingInstance.getBalance({from: mads});
        assert.equal(balance_mads, 2*ether, "Incorrect"); 

        const balance_peffen = await bankingInstance.getBalance({from: peffen}); 
        assert.equal(balance_peffen, 0, "Incorrect"); 

        const balance_lukas = await bankingInstance.getBalance({from: lukas});
        assert.notEqual(balance_lukas, ether*2, "Incorrect");
    });


contract("Banking - Withdrawal Function", (accounts) => {

    const mads = accounts[1];
    const amount = 2*ether

     it("Verifying simple withdrawal", async () => {
        const bankingInstance = await Banking.deployed(); 

        await bankingInstance.deposit({from: mads, value: web3.utils.toBN(amount)});
        await bankingInstance.withdraw(web3.utils.toBN(amount), {from: mads})

        const balance_mads = await bankingInstance.getBalance({from: mads});

        assert.equal(balance_mads, 0, "Incorrect"); 

    });
})
})