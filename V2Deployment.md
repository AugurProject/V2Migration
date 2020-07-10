# Augur v2: REP Migration
__Deployment: July 28th, 2020__


## Table of Contents

### Overview:

<b>[1]</b> [Summary](#Summary)

<b>[2]</b> [Augur v2 Deployment](#Augur-v2-Deployment)

<b>[3]</b> [REP Naming Convention](#REP-Naming-Convention)

### REP Holders:

<b>[4]</b> [Users - REP Migration](#users---rep-migration)

<b>[5]</b> [Users - Use It Or Lose It](#users---use-it-or-lose-it)

### Exchanges:

<b>[6]</b> [Exchanges - REP Migration](#exchanges---rep-migration)

<b>[7]</b> [Exchanges - Use It Or Lose It](#exchanges---use-it-or-lose-it)

### DApps, Non-Custodial Exchanges:

<b>[8]</b> [DApps, Non-Custodial Exchanges - REP Migration](#dapps-non-custodial-exchanges---rep-migration)

<b>[9]</b> [DApps, Non-Custodial Exchanges - Use It Or Lose It](#dapps-non-custodial-exchanges---use-it-or-lose-it)

### Wallets, Block Explorers, Service Providers:

<b>[8]</b> [Wallets, Block Explorers, Service Providers - REP Migration](#wallets-block-explorers-service-providers---rep-migration)

<b>[9]</b> [Wallets, Block Explorers, Service Providers - Use It Or Lose It](#wallets-block-explorers-service-providers---use-it-or-lose-it)

### Resources / Extra:

<b>[10]</b> [REP Naming Convention In The Event Of A Fork](#rep-naming-convention-in-the-event-of-a-fork)

<b>[10]</b> [Migration & Deployment Resources](#Migration--Deployment-Resources)

<b>[11]</b> [Contact](#contact)

## Summary 

- Augur v2 requires users to manually migrate their current REP tokens <a href="https://etherscan.io/address/0x1985365e9f78359a9B6AD760e32412f4a445E862">(0x1985..)</a> to a new REP token (“REPv2”). 

- Augur v2 requires <b>mandatory participation</b> of all REP holders in the event of a 60-day network wide market fork.

- Exchanges that custody REP tokens will need to prepare for the new REPv2 token, and define a process of handling a fork. 

- REPv2 cannot be converted back to REP after it is initially migrated. 

## Augur v2 Deployment

Augur v2 is scheduled for deployment on July 28th, 2020. Augur v2 is an entirely new deployment of the Augur core protocol on Ethereum. Augur v1 will continue to exist as-is independently on the Ethereum blockchain, as it has no upgrade ability, escape hatch, or method of halting trading activity on the protocol or of the REP token.

Each deployment exists in their own "universe", unaware of each-other's existence. Augur v2 is a new universe for Augur traders and REP holders, and thus, requires a manual migration of the REP token if you wish to participate in the Augur v2 and future Augur universes. 

## REP Naming Convention

The following is proposed to be adopted as the REP naming convention for Augur v2’s deployment. 

a) The new REP token to be deployed upon launch to be named “REPv2”.

b) The current REP token <a href="https://etherscan.io/address/0x1985365e9f78359a9B6AD760e32412f4a445E862">(0x1985..)</a> to maintain the name "REP".

**After careful consideration and hearing from a variety of different users and entities that interact with REP, the overwhelming consensus and feedback is that the simplest and best path forward for REP holders and ecosystem participants is to simply maintain the current REP ticker name and not rename the current REP token to REPv1, as initally announced.** 

c) ~~Immediately, block explorers, exchanges, wallet providers, etc to rename the current REP token <a href="https://etherscan.io/address/0x1985365e9f78359a9B6AD760e32412f4a445E862">(0x1985..)</a> to “REPv1”.~~


## Users - REP Migration

Augur v2 is a new universe. New REP tokens are not minted, instead, Augur v2 will allow for a manual migration of Augur v1 REP tokens ("REP") to Augur v2 REP tokens ("REPv2"). If you wish to participate as a reporter in the Augur v2 universe, you will need REPv2. 

There is no immediate requirement to migrate REP to the new REPv2 upon deployment. However, migration should be encouraged, as the new Augur v2 universe needs active reporters with REPv2 tokens ensuring that markets resolve accurately.  A disputed market will take at least two months (8 weeks) to reach the state of a fork, and the forking period is also two months (8 weeks), meaning there is a minimum period of 4 months (16 weeks) for users to migrate their REP to REPv2, with a maximum possibility of forever / never technically needing to. 

> <b>Summary for REP holders:</b> Migrate your REP to REPv2 at some point after Augur v2's deployment. A migration tool will be provided within the Augur UI, and a full tutorial on doing so will be published. 

## Users - Use It Or Lose It

The primary change surrounding the REP token in Augur v2’s deployment is the reintroduction of the “use it or lose it” concept, described in the original Augur whitepaper. This addition requires that all REP holders (REP or REPv2) must participate in a network wide market fork on Augur v2. If and when a fork does occur, a 60-day forking window begins, and all REP holders (REP or REPv2) must pick an outcome and participate in the forking process. 

If you have REP or REPv2 and do not participate in the 60-day forking process, your REP or REPv2 will be indefinitely unable to migrate past the Augur v2 universe. In other words, Augur v2’s contracts restrict any migration to forking universes after the 60-day forking period ends. 

Forking is an extreme situation for the Augur oracle, required to maintain network security and ensure users can trade in a universe that accurately represents reality. Augur v1 did not have any market forks, nor did a market dispute get even remotley close to that state.

**It is currently estimated that a triggering a network wide market fork and fulfilling all prior dispute rounds would cost approximately ~$9,100,000 USD (~550k REPv2 at $16.50), with the "losing" side of the forks REPv2 being presumably worthless.**

> <b>Summary for REP holders:</b> You must be prepared to access your REP or REPv2 and participate in a fork, with a minimum time of four months notice, and a maximum time of never (if a fork never occurs on Augur v2).  

## Exchanges - REP Migration

Upon Augur v2’s deployment, exchanges will have to make a decision on how to handle REP and REPv2 for the users deposits and funds. Below we have outlined the plausible possibilities on how an exchange could handle the migration. 

a) Trade only REPv2 from the start, automatically migrate users REP to REPv2 for them / allow for REP withdrawals. 

b) Trade only REP from the start, giving users time to withdrawal and migrate, announce full migration of user balances on X date. 

c) Trade both REP and REPv2 for a bit, giving users time to withdraw and migrate, or support opt-in migration in the exchange/wallet directly.

> <b>Summary for Exchanges: </b> Define how the exchange will handle the migration, and proceed upon Augur v2's deployment. 

## Exchanges - Use It Or Lose It

Disputed markets provide an eight week prior notice of a potential fork. Fast disputing in Augur v2 is turned off if this occurs and defaults to weekly cycles at that time. The Augur community should detect this very early on and begin signaling to the rest of the ecosystem that a potential fork is looming. 

If and when a market does fork, you will have within 60 days of the start of the forking period to participate in the fork with your users REP (REP or REPv2) deposits / balances, else their tokens will be functionally useless within the Augur protocol. 

This is intended to be an extremely rare occurrence, a last resort, costing millions and millions of dollars to perform for the parties initiating the fork. No market has gotten close to a fork in current Augur v1, and REP holders have gotten quite good at resolving markets quickly and accurately. However, if and when a fork does occur, exchanges will need to handle the fork with their customers REP balances. The forking mechanism is the core of Augur's security model. 

**It is currently estimated that a triggering a network wide market fork and fulfilling all prior dispute rounds would cost approximately ~$9,100,000 USD (~550k REPv2 at $16.50), with the "losing" side of the forks REPv2 being presumably worthless.**

<b>Options:</b>

a) Pick an outcome and migrate your users REPv2 for them (or, if you still have REP, migrate REP to REPv2 to then participate in the fork). 

b) Allow users to pick an outcome from within your wallet and participate in the fork for them with their REP. 

Additionally, exchanges will have the 60-day forking period to allow users to withdraw their REP tokens if they wish to participate in the fork themselves.

> <b>Summary for Exchanges: </b> Define a process for how your exchange will handle a possible Augur REPv2 fork. 

## DApps, Non-Custodial Exchanges - REP Migration

Assuming your exchange or application does not take custody of users REP tokens, the migration should play out similar to the SAI to DAI migration by MakerDAO earlier this year. Users will need to withdraw the REP tokens and participate in the migration themselves, with no _immediate_ need to do so. To support the new REPv2 token upon deployment, you would need to list a new market or pool with the new REPv2 token, alongside the REP market or pool. 

> <b>Summary for DApps, Non-Custodial Exchanges: </b> Alert your users of Augur v2's upcoming deployment by using the FAQ for users above. 

## DApps, Non-Custodial Exchanges - Use It Or Lose It

Assuming your exchange **cannot** physically take custody of users REP tokens, there is nothing you can do in the event of a network wide fork outside of alerting your users and recommending they withdraw their tokens and participate in the Augur v2 fork.

> <b>Summary for DApps, Non-Custodial Exchanges: </b> There is nothing you can technically due during a fork if you do not have control over users REP tokens. Alert your users of Augur v2's upcoming deployment and the Use It or Lose It functionally. 

## Wallets, Block Explorers, Service Providers - REP Migration

Upon deployment of Augur v2, you can support the new REPv2 token simply by adding the new token contract, similar to any other Ethereum ERC-20 token. 

> <b>Summary for Wallets, Block Explorers, Service Providers: </b> Alert your users of Augur v2's upcoming deployment by using the FAQ for users above. 

## Wallets, Block Explorers, Service Providers - Use It Or Lose It

After a Augur v2 fork has occurred, you will need to update your products to reflect the new forked Augur universes. 

> <b>Summary for Wallets, Block Explorers, Service Providers: </b> Alert your users of Augur v2's upcoming deployment and the Use It or Lose It functionality. 

## REP Naming Convention In The Event Of A Fork

In the extremely rare occurance of a network wide market fork on Augur v2, below is how the REPv2 naming convention will be handled on a technical level. Note: In the event of a REPv2 fork, it is anticipated that the community will handle it very similar to how a conventional, say Bitcoin and Bitcoin Cash fork, occurred. While the technical names can be complex, depending how controversial the fork is, it is assumed one side of the fork will collectively be deemed the "winner", and thus named accordingly by the ecosystem. 

Naming Convention for Forked REP: <b>REPv2_(OUTCOME)_(FORK_INDEX)</b>

Where "FORK_INDEX" is the chronological order of forks. The first fork ever will have a "1" as its fork index and all child universes of the genesis universe will have "1" as their value. If another fork occurs in one of those children its fork index will be "2". If either one of its children or one of its siblings forks the fork index will be "3". This scheme means each fork has a unique identifier just based on chronological order.

Where "OUTCOME" is dependent on the type of market. In any market a payout of invalid is "INVALID" and a payout which is not expected is "MALFORMED" (for example if there is a partial payout to both "YES" and "NO"). In a Yes / No market the outcome will be "YES" or "NO". In a categorical the outcome will be the provided description of the outcome. In a scalar the number value of the long outcome.

While this extreme case of a network wide fork is anticipated not to happen, this convention will be followed in the event it does occur. 

## Migration & Deployment Resources

- Current REP token - <a href="https://etherscan.io/address/0x1985365e9f78359a9B6AD760e32412f4a445E862">Etherscan</a>

- New REPv2 token (to be live upon deployment) - <a href="https://github.com/AugurProject/augur/blob/master/packages/augur-core/src/contracts/reporting/ReputationToken.sol">Source Code</a>

- Augur v2 REP to REPv2 migration tools - <a href="https://github.com/AugurProject/V2Migration">Source Code</a>

- Augur v2 contracts (to be live upon deployment) - <a href="https://github.com/AugurProject/augur/tree/master/packages/augur-core/src/contracts">Source Code</a>

## Contact 

If you have any questions, comments or concerns, please reach out via one of the means below: 

- Augur Discord for questions - <a href="http://invite.augur.net">Discord</a>

- Augur Twitter for public communications - <a href="https://twitter.com/AugurProject">Twitter</a>

- Augur Email for questions - <a href="mailto:migrate@augur.net">Email</a>

A list of all the exchanges, dApps, wallets, etc public responses and plans to the migration will be aggregated and published in this repository. 
 
