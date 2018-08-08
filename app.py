# Application main file

import datetime as date
import genesis
from block import Block
from generator import BlockGenerator

# Create a blockchain and initialize it with a genesis block
blockchain = [genesis.create_genesis_block()]
previous_block = blockchain[0]

# Max num of blocks to be written to initial test network
max_blocks = 20

if __name__ == "__main__":
    print("Tinycoin server started ...!")
    for i in range(0, max_blocks):
        new_block = BlockGenerator(previous_block).next()
        blockchain.append(new_block)
        previous_block = new_block

        # Broadcast the newly added block to the world
        print(f"Block { new_block.index } has been added to the blockchain!")
        print(f"Hash: { new_block.hash }\n")