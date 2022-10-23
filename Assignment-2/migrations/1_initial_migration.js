const Migrations = artifacts.require("Banking");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};