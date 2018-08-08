# Block class

import hashlib as hasher

class Block(object):
    
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def message(self):
        return str(str(self.index)
                    + str(self.timestamp)
                    + str(self.data)
                    + str(self.previous_hash)
                ).encode("utf-8")

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(self.message())
        return sha.hexdigest()
    
    
    