
Hashing is the most important part of Blockchain. Blockchain is built on the concept of blocks the those are linked to each other in the form of a ledger via the concept of Hashing.

Let's dive deep into the Hashing algorithm ->

The algorithm which converts input data of any length into a string of fixed size.
That string of fixed size is also called as hash value.

EX-> "I am Himanshu Sharma" --> Converted into 3C43B43K4353535H3LKKLH353L. (This value is called a hash)

Hashing has some unique properties ->

1) Irreversibility -> After hashing any data it can't be de-hashed easily. If we have to dehash the given Hash, 
                      then the underlying mathematical principle makes it very difficult to compute
                      (similar to solving a hard problem in computer terms.)
                      It is unlike, encryption and decryption scheme.
                      
2) Unique -> There are never two similar hash values. This property is also known as 'Deterministic'.
             If two hash are found to be same. Then, it is called as 'hash collision'.

3)Fast Computation -> A hash function can be used to substitute the data with a newly generated hash code. 
                      Hash algorithms are generally used to offee a digital fingerprint of a file's contents often used to 
                      provide that the file has not been changed by an intruder or virus.

4) WithStand Collisions -> The irreversibility property of the hash makes it very much secure against any kind of Cryptographic and Cyber attack.

5) Avalanche Effect -> If there is very minor change in the input data (say even a bit), then the whole hash value will change drastically. 
                      The Avalanching effect can also be co-related with with the concept of Bit-Dependency wherein every bit is dependent on every other bits change.
              
              
Types of Hashing techniques used in present day blockchain technology:

The Bitcoin Blockchain is based on the SHA-256 Algorithm and the Ethereum Blockchain is based on the Keccak-256 Hashing Algorithm.

SHA-256 ->  It stands for Secure Hashing Algorithms. It's a derived version of the NSA designed SHA-2 algorithm.
            Its a type of hashing algorithms thats used to convert data of any length into a fixed size of 
            strings of 256 bits(consisting of 0's and 1's) and then it provied the output those 256 bits in a 64 hexadecimal
            characters format. The Bitcoin Blockchain to verify its Transaction.

            To understand the SHA-256 algorithm better, delve into [Link Here](https://www.youtube.com/watch?v=DMtFhACPnTY) this brilliant video from 'Computerphile'.

Keccak-256 -> It belongs to the hashes from the SHA-3 family. Its used to hash the Transaction in the Ethereum Blockchain network. 
              It was published by NIST in 2015. Ethereum uses Keccak-256 in a consensus engine called Ethash.

              To delve into the Keccak-256 Algorithm follow [Link Here](https://medium.com/0xcode/hashing-functions-in-solidity-using-keccak256-70779ea55bb0) this article from 'Medium'. 

The concept of Hashing is a building block in the concept of Blockchain Technology.

If you'ld like to visualize the concept of Hashing and how it's implemented in the actual working of a Blockchain, then check out the practical and dynamic explanation by Anders BrownWorth. [Link Here](https://block-chain-visualization-kxrp.vercel.app/)
 
