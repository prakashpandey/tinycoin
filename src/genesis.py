# This is a special file containing a genesis block

import datetime as date
from block import Block

def create_genesis_block():
    # Manually crate a block with index zero
    # and arbitary previous hash
    print(f"Creating and initializing blockchain at { date.datetime.now() }\n")
    return Block(0, date.datetime.now(), "Genesis block", "0")