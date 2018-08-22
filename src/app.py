# Application main file

import datetime as date
import genesis
import block
from block import Block, Data
from generator import BlockGenerator
from transaction import Transaction
from flask import Flask
from flask import request
import json
import utils
import os

node = Flask(__name__)

# Create a blockchain and initialize it with a genesis block
blockchain = [genesis.create_genesis_block()]
previous_block = blockchain[0]

# A completely random address of the owner of this node
miner_address = None

# Transactions that this node is doing
nodes_transactions = []

# Link of peer nodes
peer_nodes = None
# If we are mining or not
mining = True 

# Mock the rest request
mock = False

@node.route("/transaction", methods=['POST'])
def transaction():
    transaction_received = request.get_json()
    print(f"transaction_received: { transaction_received }")
    transaction = Transaction(
        transaction_received['from'], 
        transaction_received['to'], 
        transaction_received['amount']
    )
    
    # print transaction logs
    print("New Transaction")
    print(f"From: { transaction_received['from'] }")
    print(f"From: { transaction_received['to'] }")
    print(f"Amount: { transaction_received['amount'] }\n")
    
    if(transaction.is_valid()):
        nodes_transactions.append(transaction.to_json())
        return "Transaction submission successful\n"
    else:
        return "Invalid transaction\n"

@node.route("/blocks", methods=['GET'])
def get_blocks():
    return json.dumps(blockchain)

def find_new_chains():
    other_chains = []
    for node_url in peer_nodes:
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
    last_block = block.get_block_obj(blockchain[len(blockchain) - 1])
    last_proof = json.loads(last_block.data)['proof_of_work']

    # Find proof of work for the current block being mined
    proof = proof_of_work(last_proof)

    # Ones the miner found out the proof of work
    # the network rewards the miner by adding a transaction
    nodes_transactions.append(Transaction("network", miner_address, 1).to_json())

    # Create a block
    new_block_data = Data(proof, nodes_transactions).create()
    new_block_index = last_block.index + 1
    last_block_hash = last_block.hash
    new_block_timestamp = utils.get_string_datetime(date.datetime.now())

    # Empty the current transaction as it is already processed
    nodes_transactions[:] = []
    # Creating new block
    mined_block = Block(new_block_index, new_block_timestamp, new_block_data, last_block_hash)
    blockchain.append(mined_block.to_json())
    # Broadcast to the world that we have mined
    return mined_block.to_json() + "\n"
    


if __name__ == "__main__":
    print("Tinycoin server started ...!\n")
    miner_address = os.getenv("MINER_ADDRESS", None)
    if(not miner_address):
        print("Can not start application as valid miner address not found")

    peers = os.getenv("PEERS", None)
    if(peers):
        peer_nodes = peers.split(",")
    else:
        peer_nodes = []
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 5000))
    node.run(host = host, port = port)