# Block class

import hashlib as hasher

class Data(object):
    """
        Data structure of a 'data' in a block
    """

    def __init__(self, proof_of_work, transactions=[]):
         self.transactions = transactions
         self.proof_of_work = proof_of_work
    
    def add_transaction(self, transaction):
        """
            Add a transaction 
        """
        self.transactions.append(transaction)

    def create(self):
        """
            Returns block data
        """
        return {
            "proof_of_work": self.proof_of_work,
            "transactions": list(self.transactions)
        }
    

class Block(object):
    
    def __init__(self, index, timestamp, data, last_block_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.last_block_hash = last_block_hash
        self.hash = self.hash_block()

    def message(self):
        return str(str(self.index)
                    + str(self.timestamp)
                    + str(self.data)
                    + str(self.last_block_hash)
                ).encode("utf-8")

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(self.message())
        return sha.hexdigest()
    
    def to_json(self):
        return str({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        })

if __name__ == "__main__":
    b = Block(1, "2018-10-2025", "this is a data", "2233cdd-44dffd-33443dd-ddd332w")
    print(b.to_json() + "\n")
    
    
    