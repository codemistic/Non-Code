## What is The Merge? 


There is no doubt that Ethereum is the core of web3 as measured by total economic activity, user growth, and developer engagement. The Merge was an overhaul of Ethereum’s consensus mechanism, transitioning the network from Proof-of-Work (PoW) to Proof-of-Stake (PoS) consensus.

Under Proof-of-Work (PoW), miners confirm blocks by solving cryptographically complex computation problems – consuming energy along the way (literally, the ‘proof-of-work’). The total security of any given PoW public blockchain network is measured in hash power, or the total amount of computation (and hence energy) devoted to securing the network. Because mining requires specialized equipment and skills, the majority of hash power on Ethereum was previously controlled by a small number of privately operated mining pools.

Under Proof-of-Stake (PoS), however, rather than solving cryptographic problems, PoS consensus validators stake ether into a smart contract on Ethereum. This staked ether then acts as collateral that can be destroyed if the validator behaves dishonestly or unreliably. Because anyone can operate a validator under PoS as long as they have 32 ETH to leverage, control over the network is distributed amongst many more participants than under PoW. Individuals with less than 32 ETH can also enjoy yield from staking by participating in mining pools such as Rocket Pool, Lido, or with a centralized exchange.

**But what exactly was the “merging” process that occurred during The Merge?**

“The Merge” signified the merging of the Ethereum mainnet execution client with the Beacon Chain Proof-of Stake consensus client. Despite post-Merge Ethereum previously donning the colloquial term Eth2 or Ethereum 2.0, The Merge is really a network upgrade not the creation of a whole new token or new network as the term “Eth2” might imply. After The Merge, Ethereum nodes comprise of both an execution client (Eth1), and a consensus client (Eth2); both are needed to run a full Ethereum node.

* Eth1 → execution layer
* Eth2 → consensus layer
* Execution layer + consensus layer = Ethereum

The Execution Layer is responsible for state storage and management, state sync, virtual machine execution, transaction processing, mempools, etc. The Consensus Layer encompasses the upgrades that the Beacon Chain brought to the Ethereum blockchain, most importantly the transition from proof-of-work (PoW) to proof-of-stake (PoS). 

Because the Execution Layer relies on current Ethereum clients, maintaining it allowed for a smoother transition for dapp developers during the network’s move to proof-of-stake as no migration was necessary on their end.

## Why Go From Proof-of-Work (PoW) To Proof-of-Stake (PoS) 


There are three major reasons Ethereum switched from a PoW system to a PoS system:

* PoS results in a more secure, decentralized network.
* PoS enables scalability through sharding.
* PoS is more efficient, using ~99% less energy than PoW.

**PoS results in a more secure, decentralized network**

Transitioning the network to PoS was the first step to enabling sharding — an effort to split the network into “shard chains” that share the load of Ethereum, theoretically reducing network congestion and increasing transaction throughput. Instead of settling all operations on one single blockchain, these shard chains spread operations across 64 new chains. Sharding is planned to begin in 2023 and should enable giant leaps in scalability for the network.

A newer sharding design, called Danksharding, is gaining traction in the Ethereum community. Danksharding introduces significant simplifications to previous sharding designs and introduces the concept of Proposer/Builder Separation (PBS). We will discuss the potential effects of separating block building from block proposing later in this blog.

Once implemented, sharding is expected to increase Ethereum’s transaction throughput up to 100,000 transactions per second—higher throughput than all leading credit card companies.

**PoS is more efficient, using ~99% less energy than PoW**

Under PoS there is no need to use massive amounts of energy on proof-of-work computations. As a result, Ethereum’s switch to PoS resulted in a 99.9% reduction in energy used to secure the network.

## What changed after The Merge?


The Merge brings several key changes to Ethereum, notably:

* Miners were replaced by validators
* Increased time to block finality
* New penalties add stakes to staking
* Validators gained access to MEV via MEV-boost auctions
* Block building creates new economic actors
* The block reward subsidy was reduced by ~90%
* Fixed block times may influence MEV dynamics

**Miners are replaced by validators**

The move to PoS replaced miners with validators. Instead of needing a powerful mining rig, to participate as a validator all someone needs now is 32 ETH to stake and three separate pieces of software: an execution client, a consensus client, and a validator.

Validators propose new blocks, submit attestations (votes), and monitor for any slashable offenses (penalties).

A validator will stay active until:

* It voluntary exits
* Its balance drops below 16 ETH
* It gets SLASHED

**Increased time to block finality**

Today, Beacon Chain blocks take 64-95 slots (~15 minutes) to finalize—a significant increase from the less than five minutes it took to wait for 35 block confirmations, at which point it was generally agreed upon that a transaction is likely safe and finalized under PoW. Why does block finality take so much longer under PoS? To understand this, let’s take a high-level look at how block finality works after The Merge.

Under PoS, blocks are created every slot (12 seconds) even if they are empty. The network randomly selects one validator to be the proposer for each slot. If the validator misses the opportunity to propose a block during their assigned slot, the network will not have a block in that slot and it simply progresses to the next slot.

If a block is created, other validators on the network receive this new block, verify it is valid, and submit an attestation (vote) in favor of the block across the network. 

Every 32 slots (6.4 minutes)—also known as an epoch—each validator on the network also has the opportunity to submit one attestation (vote) in favor of the epoch. It takes two justified epochs (a “justified” epoch meaning the majority of validators agreed on it) for those epochs, and all the blocks inside of them, to be considered finalized. Once a block is finalized, reverting that block requires at least 1/3 of all validators to burn their deposits, which is estimated to cost over 3 million ETH.

While this new path to block finality may take longer, it is much more secure than the “longest-chain” rule found in PoW blockchains and is less likely to result in double-spend attacks or hard forks.

**New penalties like "Slashing" add stakes to staking**

In addition to proposing blocks and submitting attestations, validators can also monitor each other for malicious behavior and “slash” other validators for failing to uphold the security of the network. Slashable offenses are acts that are provably against the Ethereum network including double voting (e.g. proposing two blocks in the same slot) or submitting contradictory attestations (e.g. signing two different attestations in one epoch).

Validators that search for slashible events are called “whistleblowers” or “slashers.” When a whistleblower finds a slashable event, they will broadcast it to the network for the next block proposer to add the proof to their block. In turn, the block proposer will receive a reward for slashing the malicious validator. The whistleblower, however, does not receive a reward. This is because being a whistleblower is intended to be an altruistic action and not meant to be profitable.

It is also important to note that slashing does not always result from malicious intent. Validators can also be slashed for being lazy and not participating in the network. Likewise, a validator could be slashed as a result of completely accidental actions including not having slashing protection up to date on failover servers or using duplicate keys.

When a validator is slashed, they suffer a gradual loss of ETH. The actual amount will vary depending on network activity. Slashed validators can be barred from further participating in the protocol and forcibly exited from the network forever.

Slashing should not be confused with inactivity penalties which constitute the loss of funds incurred when a validator is offline or unable to perform its validation duties.

**Block building creates new economic actors**

Public blockchain networks ‘batch’ transactions into blocks. Blocks subsequently get confirmed (or validated) and added to the blockchain. The process of determining which transactions are included in a block, and in which order, is known as block building. And, as you might expect, transaction inclusion and ordering can have a big impact on how value moves – and to whom – within the network.

Under PoW, block building and mining (i.e.proposing and confirming a block) were all handled by the same network actor. Because mining requires specialized tools and knowledge, only a small set of mining pool operators ended up being responsible for the vast majority of block construction – making this both opaque and centralized.

This changed – fundamentally – with The Merge.

While block building and proposing are still under the same one person—the validator, the substantial influx of many new validators will likely result in many participants that lack the skill to build optimized, profitable blocks the same way miners could.

As a result, The Merge creates the conditions for a new class of core network economic actors to emerge: Block Builders. These block builders are specialist providers that compete in a real-time marketplace to perform block construction on behalf of validators. Eventually, this separation between block builders and proposers will be codified in the network under what is known as the Proposer/Builder Separation (PBS).

The separation of block building from proposing catalyzes entirely new categories of economic actors with far-reaching implications and potentially new, different, and perhaps even hidden power structures. Block building will likely have a more profound impact than many expect; for example, new dynamics created by block building may actually lead to your web3 wallet or dapp paying you to use it.

**Block reward subsidy is reduced by ~90%**

Just as miners received newly minted ETH as a reward for successfully adding a block to the blockchain under PoW, under PoS, the validators that successfully propose new blocks are also issued a block reward. However, under PoS this block reward is reduced by nearly 90% as validators do not incur the high cost associated with mining and therefore require less of a subsidy from the network.

As outlined by the Ethereum Foundation, ETH issuance under PoS greatly reduces sell pressure for Ethereum. According to Ethereum.org, the mining and stake reward comparison equates to the following:

* (Pre-Merge) PoW Mining rewards: ~13,000 ETH/day pre-merge.
* (Pre-Merge) Staking rewards: ~1,600 ETH/day pre-merge.
* (Post-Merge) Only the ~1,600 ETH per day remain, dropping total new ETH issuance by ~90%.

This impact is referred to as the triple halvening.

The implementation of the EIP-1559 upgrade during the London Hard Fork in August 2021 also introduced a burning mechanism into ETH gas fees. The reduction in block rewards on top of burning gas base fees may result in ETH becoming a deflationary asset post-Merge.

**Fixed block times may change the way some users transact**

A significant change to come out of The Merge is fixed block times. The previous PoW model used variable block times, which meant that blocks could be confirmed at any moment. Every millisecond was equally ‘valuable' under this system; miners and MEV searchers could not predict exactly when the next block would be confirmed. 

Under PoS, blocks are confirmed every 12 seconds, like clockwork. This means every millisecond is no longer equal to every other millisecond as those closer to the block confirmation hold more value for specific trading strategies so competitors have less time to respond. This can result in surge effects where the second or two before the block gets confirmed sees a spike in transactions.

There are tighter time horizons for various automated systems to compete with each other, creating competition for lower latency infrastructure to detect and respond. This will likely have an impact on gas fees, but more data will need to be collected. 

A vast amount of capital is being allocated toward researching and discovering how fixed block times will impact gas fees. We at Blocknative believe that we will see a new phenomenon, post-Merge, that will affect the entire network and the nature of the gas marketplace.

## What stays the same after The Merge?



While The Merge caused substantial changes to the way Ethereum works under the hood, on the surface users didn’t see any substantial changes in regards to gas or transaction throughput.

* The Merge did not affect the current gas pricing model—Ethereum continues to use EIP-1559.
* The Merge did not lower gas fees. However, Blocknative is keeping a close eye on how fixed block times influence transactional patterns and how these new patterns are impacting the gas market.
* The Merge did not increase the transaction throughput of Ethereum. This is not expected until the introduction of sharding in 2023.

## The Merge impacts all network participants. Are you prepared for the post-Merge future?



In addition to the transition to Proof-of-Stake, The Merge included multiple upgrades to how the Ethereum network operates, as covered by this article. Many of these upgrades make pre-chain data more important than ever when navigating a post-Merge world to ensure your users can transact with confidence.