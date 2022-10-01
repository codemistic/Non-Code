Blockchains are incredibly popular nowadays. What is blockchain? How do they work, what problems do they solve, and how can they be used? Like the name indicates, a blockchain is a chain of blocks that contains information. This technique was initially described in 1991 by a group of researchers. It was initially intended to timestamp digital documents so that it's not possible to backdate them or tamper with them, almost like a notary. However, it went by mostly unused until it was adopted by Satoshi Nakamoto in 2009 to create a digital cryptocurrency, Bitcoin.

https://lh3.googleusercontent.com/-UpK1_PdIZ3E/YL2rDCrltRI/AAAAAAAAD-8/44MwwWiCsR8Lf66EEiyVolpvF4n-HnxlwCNcBGAsYHQ/w612-h331/image.png


https://lh3.googleusercontent.com/-wZlhtcpryMI/YL2s3F2ZwWI/AAAAAAAAD_E/_hGzGwHECWY4n4oO9RbqVXtR6S7PX68uACNcBGAsYHQ/w333-h160/image.png


A blockchain is a distributed ledger that is entirely open to everyone. They have an attractive property: once some data has been recorded inside a blockchain, it becomes challenging to change it. So, how does that work? Well, let's take a closer look at a block. Each block contains some data, the hash of the block, and the previous block's hash. The data that is stored inside a block depends on the type of blockchain. For example, the Bitcoin blockchain stores the details about a transaction here, such as sender, receiver, and the number of coins.

                                 

A block also has a hash. You can compare a hash to a fingerprint. It identifies a block and all of its contents, and it's always unique, just as a fingerprint. Once a block is created, its hash is calculated, and changing something inside the block will cause the hash to change. So, in other words, hashed are very useful when you want to detect changes in blocks. If the fingerprint of the block changes, it no longer is the same block. The third element inside each block is the hash of the previous block. This effectively creates a chain of blocks, and it's this technique makes a blockchain so secure. 


https://lh3.googleusercontent.com/-W-j-98E_wrQ/YL2t1chbQwI/AAAAAAAAD_U/0spCw66eoq8v512sIxpKx0QcocBGi6fggCNcBGAsYHQ/w565-h256/image.png


Let's take an example; here, we have a chain of 3 blocks. As you can see, each block has a hash and the hash of the previous block. So block number 3 points to block number 2 and number 2 points to number 1. The first block is a bit special; it cannot point to previous blocks because it's the first one. We call this the genesis block. 

https://lh3.googleusercontent.com/-c8pUZKBHdC4/YL2v0W57cLI/AAAAAAAAD_c/5BCKfFEoHY44YtOijV7ereDZAxLxwLm8QCNcBGAsYHQ/w537-h247/image.png

Now let's say that you tamper with the second block, which causes the hash of the block to change. In turn, that will make block 3 and the following blocks invalid because they no longer store a valid hash of the previous block. So changing a single block will make all following blocks invalid. But using hashes is not enough to prevent tampering. Computers these days are high-speed and can calculate hundreds of thousands of hashes per second. You could effectively tamper with a block and recalculate all the hashes of the other blocks to make your blockchain valid again. So to mitigate this, blockchains have something called proof-of-work. 

https://lh3.googleusercontent.com/-wnHMsnLCZ8U/YL2wL_LYWmI/AAAAAAAAD_k/2vsnxZkEgzsyDytqCooPsSb4XpoyJW4LgCNcBGAsYHQ/w543-h319/image.png

Proof-of-work: It's a mechanism that slows down the creation of new blocks. In Bitcoin case: it takes about 10 minutes to calculate the required proof-of-work and add a new block to the chain. The mechanism makes it very hard to tamper with the blocks because if you tamper with 1 block, you need to recalculate the proof-of-work for all the following blocks. So the security of blockchain comes from its creative use of hashing and the proof-of-work and mechanism. But there is one more way that blockchains secure themselves, and that's by being distributed. Instead of using a central entity to manage the chain, blockchains use a peer-to-peer network, allowing anyone to join. When someone joins the network, he gets the full copy of the blockchain. The node can be used to verify that everything is still in order. 

https://lh3.googleusercontent.com/-rLXoEjGnGno/YL2xA5AJmdI/AAAAAAAAD_s/d3gSDXhdDOI6XW6kJKvAJXgInHlCGijCwCNcBGAsYHQ/w359-h140/image.png

https://lh3.googleusercontent.com/-5xlzaKAMuLA/YL2xvhp-k5I/AAAAAAAAD_8/zhHgsrlBmfYRUvOHWr75k0VmOlk3VWC1wCNcBGAsYHQ/w190-h140/image.png

Now let's see what happens when someone creates a new block. The new block is sent to everyone n the network. Each node then verifies the block to make sure that it hasn't been tampered with. If everything checks out, each node adds this to their own blockchain. All the nodes in the network create consensus. They agree about what blocks are valid and which aren't. Blocks that are tampered with will be rejected by other nodes in the network. So to successfully tamper with a blockchain, you'll need to tamper with all blocks on the chain, redo the proof-of-work for each block and take control of more than 50% of the peer-to-peer network. Only then does your tampered block become accepted by everyone else. This is almost IMPOSSIBLE to do! Blockchains are constantly evolving. One of the more recent developments is the creations of intelligent contracts. These contracts are simple programs stored on the blockchain and can be used to automatically exchange coins based on certain conditions. 


The creation of blockchain technology piqued a lot of people's interest. Soon, others realized that the technology could be used to store medical records, create a digital notary, and even collect taxes. So, you know what a blockchain is, how it works on a fundamental level and what problems it solves. 
