# Transaction contains the data structure of transaction in a blockchain

class Transaction(object):
    """
        Data structure of a transaction in a blockchain

        E.g:
        {
            "from": "71238uqirbfh894-random-public-key-a-alkjdflakjfewn204ij",
            "to": "93j4ivnqiopvh43-random-public-key-b-qjrgvnoeirbnferinfo",
            "amount": 3
        }
    """
    def __init__(self, _from_, to, amount):
        self._from_ = _from_
        self.to = to
        self.amount = amount
    
    def create(self):
        transaction = {
            "from": self._from_,
            "to": self.to,
            "amount": self.amount
        }
        return str(transaction)



   