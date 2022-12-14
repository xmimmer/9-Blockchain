# Assignment 3 - Hyperledger Fabric 

## **Use-case: Electronic Voting Application** 

**Transparency** is an important part of the voting application use case. Both voters and auditors need to have an idea of what's happening. 
The application must be **secure** to avoid any misconduct from happening. We should avoid **double spending** as voters should not be allowed to vote more than once.
**Performance** and **scalability** are very important attributes as the voting system should be able to function quickly in different size environments. Without scale, the application won't be able to grow, and without performance, the traditional system is a better option. The system also has to be **simplistic** as it should be simple enough for ordinary users to participate. They should be able to vote by mail, without having to worrying about blockchain technology too much. We need **eligibility** to ensure that the ones casting the votes, are actually eligible to vote, otherwise it would be a disaster. The system should be **confidential** - voters should be identifiable, but votes should not. This will get rid of the double spending problem. In order to get meaningful results, **integrity** is very important. Voters should feel like they are being treated with full honesty. Finally, users should be able to cast a vote anytime (within the voting period) without having problems. This makes **availability** very important. The aggregated list of requirements is listed below.

* Transparency
* Security
* No double spending
* Performance
* Scalability
* Simplicity
* Eligibility
* Confidentiality / Integrity / Availability (CIA)


### **1. Evaluation Analysis**
| Architecture or Blockchain Characteristic | Weight | Subjective Percentage of Affirmation | Weight Affirmation |
|-------------------------------------------|--------|--------------------------------------|--------------------|
| Immutability                              | 8      | 75%                                  | 6                  |
| Transparency                              | 14     | 100%                                 | 14                 |
| Trust                                     | 16     | 75%                                  | 12                 |
| Identity                                  | 14     | 100%                                 | 14                 |
| Distribution                              | 5      | 100%                                 | 5                  |
| Workflow                                  | 5      | 15%                                  | 0.75               |
| Transactions                              | 10     | 100%                                 | 10                 |
| Historical Record                         | 10     | 50%                                  | 5                  |
| Ecosystem                                 | 10     | 100%                                 | 10                 |
| Inefficiency                              | 8      | 100%                                 | 8                  |
| Total Percentage of Fit                   | 100    | 81.5%                                | 84.75/100          |

### **2. Criteria Analysis**

* **Will this project require updates, mutability or deletion of records?**  
Most likely not. The voting system follows a simple transactional model without double spending. A change in law could potentially require an update to the architecture, but we find it very unlikely. 

* **Is there agreement that all blockchain participants should be able to view and validate    transaction details?**  
Yes, however, transaction details are obfuscated and unreadable. This means that there is no way to figure out what people have voted for.

* **Does this architecture fit well in an ecosystem of diverse participants?**  
Yes. Each participant should be able to vote by mail, so there is no difference between the participants. 

* **Are there adequate incentives for participants to continue to support the chain indefinitely?**  
Yes. Whenever there is a vote, each individual would like to use their vote just like they would in a traditional system. Voting by mail would also be a quicker option for the voter.

* **From an efficiency perspective, are there enough participants and sufficient complexity to buoy the consensus model, validate all transactions, and approve the authentication and authorization processes?**  
A voting system could have as many participants as the entire country's eligible voter population. It would also be hosted by the state, and funded through tax money, ensuring enough resources to process everything.

### **3. Suitability Analysis**
![Suitability Analysis](images/suitability_diagram.png)

Multi-party is a requirement since the political system requires political parties across the political spectrum to run for elections. There is no trusted authority required, as long as storage and computation is handled on-chain, where it is immutable which is definitely a requirement in order to run a fair vote. High performance is believed to be necessary since a lot of votes are expected at a very fast pace, depending on the voting environment (district, country etc.). High performance is usually not guaranteed in blockchain technology, however, with frameworks such as Hyperledger Fabric we can deploy permissioned high-performance blockchains. This is among more because we can choose consensus mechanisms depending on specific use-cases. Transparency is a requirement for voters to get insight in the voting process. Voters should be identifiable, but actual votes should not. Without transparency a blockchain implementation is no better than a traditional voting system from an end-user point of view. Finally we land on a blockchain implementation, and we can now suggest an architecture based on our use-case.

### **4. Designing the Hyperledger Fabric Blockchain**
![Design Process](images/design_diagram.png)

Now that we have somewhat argued for the suitability of blockchain, we can use the above design framework to figure out the architecture of the solution. With an e-voting system there is no need for a trusted authority, as long as all computation and storage is on-chain. On-chain is advantageous over off-chain both for storage and computation in high-risk voting systems, because then all votes and counts are immutable and transparent. Off-chain computation is faster than off-chain, however, we find the security aspect very essential. All participants are supposed to be identifiable while their votes should be unidentifiable. This speaks for a private/permissioned blockchain implementation. The block configuration would depend on the environment the blockchain is implemented in. The batch-size and batch-time should be configured so that the transactions per second (TPS) are high enough to finish the voting count within 24 hours of the individual votes.

**Hyperledger Fabric Architecture Design**

This diagram is made in collaboration with Steffen Buhl Kr??is. This diagram is our proposed network architecture of the Hyperledger Fabric voting application. The idea is that we have a channel for voting C1 and a channel for voting distribution C2. Each of these two channels has their own unique configuration CC1 and CC2. In this sample network we have three organizations R1, R2 and R3. They could potentially be political parties or individuals, so they are not limited. The organizations are invited before an election by the MSP. With each organization there is a peer node, a ledger and a smart contract. Each organization has a CA so that they are identifiable and legit in the network. The ordering node O is responsible for ordering all transactions. In this diagram the ordering node is very simple and connected to both C1 and C2. We can now attach external applications to each of the channels. We could for example have a voting application where eligble participant can easily vote. We could also have a distribution application for distributing votes, or an observation application where people can view current election results. The external applications should of course only be connected to the channels they need. All storage and computation happens on-chain as we believe election data is very important and of high risk.
![Fabric Architecture](images/Hyperledger%20architecture.drawio.png)
