# Application main file

import datetime as date
import genesis
from block import Block, Data
from generator import BlockGenerator
from transaction import Transaction
from flask import Flask
from flask import request
import json
import utils

node = Flask(__name__)

# Create a blockchain and initialize it with a genesis block
blockchain = [genesis.create_genesis_block()]
previous_block = blockchain[0]

# A completely random address of the owner of this node
miner_address = "ppdpp-dvfgf-fredgdsdf-gdsfgsd-35vr433-ee2eass4d"

# Max num of blocks to be written to initial test network
max_blocks = 20

# Transactions that this node is doing
nodes_transactions = []

# Link of peer nodes
peer_node = ['192.168.1.1:8080', '192.168.1.1:8081']

# If we are mining or not
mining = True 

# Mock the rest request
mock = False

@node.route("/transaction", methods=['POST'])
def transaction():
    transaction = request.get_json()
    nodes_transactions.append(transaction)
    # print transaction logs
    print("New Transaction")
    print(f"From: { transaction['from'] }")
    print(f"From: { transaction['to'] }")
    print(f"Amount: { transaction['amount'] }\n")

    return "Transaction submission successful\n"

@node.route("/blocks", methods=['GET'])
def get_blocks():
    chain_to_send = []
    for block in blockchain:
        transaction = {
            'index': str(block.index),
            'timestamp': str(block.timestamp),
            'data': str(block.data),
            'hash': str(block.hash)
        }
        chain_to_send.append(transaction)
    return json.dumps(chain_to_send)

def find_new_chains():
    other_chains = []
    for node_url in peer_node:
        if mock:
            # mock call
            chain = get_blocks()
        else:
            # real call
            chain = request.get(node_url + "/blocks").get_json()
        other_chains.append(chain)
    return other_chains

def consensus():
    """
        A simple consensus algorithm
        considering the longest chain as the most trusted chain
    """

    # Get other chains from peers 
    other_chains = find_new_chains()
    
    # Find the longest chain in other chain
    longest_chain = utils.find_longest_sub_list(other_chains)
    global blockchain
    if(len(longest_chain) > len(blockchain)):
        blockchain = longest_chain

def proof_of_work(last_proof):
    """
        This is a simple , sudo, not production ready proof of work
    """
    incrementor = last_proof + 1
    while not (incrementor % 31 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # Broadcast this number as proof that we have successfully performed proof of work
    return incrementor

@node.route("/mine", methods=['GET'])
def mine():
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data['proof-of-work']

    # Find proof of work for the current block being mined
    proof = proof_of_work(last_proof)

    # Ones the miner found out the proof of work
    # the network rewards the miner by adding a transaction
    nodes_transactions.append(Transaction("network", miner_address, 1).create())

    # Create a block
    new_block_data = Data(proof, nodes_transactions).create()
    new_block_index = previous_block.index
    last_block_hash = previous_block.hash
    new_block_timestamp = date.datetime.now()

    # Empty the current transaction as it is already processed
    nodes_transactions[:] = []
    # Creating new block
    mined_block = Block(new_block_index, new_block_timestamp, new_block_data, last_block_hash)
    blockchain.append(mined_block.hash)
    # Broadcast to the world that we have mined
    return mined_block.to_json() + "\n"
    


if __name__ == "__main1__":
    print("Tinycoin server started ...!\n")
    node.run()
    # for i in range(0, max_blocks):
    #     new_block = BlockGenerator(previous_block).next()
    #     blockchain.append(new_block)
    #     previous_block = new_block

    #     # Broadcast the newly added block to the world
    #     print(f"Block { new_block.index } has been added to the blockchain!")
    #     print(f"Hash: { new_block.hash }\n")