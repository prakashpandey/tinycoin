# This is a special file containing a genesis block

import datetime as date
from block import Block

def create_genesis_block():
    # Manually crate a block with index zero
    # and arbitary previous hash

    return Block(0, date.datetime.now(), "Genesis block", "0")