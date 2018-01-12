#!/usr/bin/python

import hashlib
import json
from time import time
from uuid import uuid4

class BlockChain(object):
    def __init__():
        self.chain = []
        self.curren_transactions = []

        # create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        创建一个新的区块,并添加到区块链的链中
        :param proof: <int> 通过执行算法得到证据
        :param previous_path: (Optional) <str> 哈希前一个区块
        :return: <dict> 返回新的区块
        """
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions': self.curren_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transactions
        self.curren_transactions = []

        self.chain.append(block)
        return block

    def new_transactions(self, sender, recipicent, amount):
        """
        添加一个新的业务事件到事件列表
        :param sender: <str> 发送者标识
        :param recipient: <str> 接受者标识
        :param amount: <int> 事件涉及数量或者金额
        :return: <int> 当前事件对应区块的索引id
        """
        self.curren_transactions.append(
            {
                'sender': sender,
                'recipient':recipicent,
                'amount':amount
            }
        )

        return self.last_block['index']+1

    def proof_of_work(self, last_block):
        """
        工作的算法简单证明:
        - find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(self, last_proof, proof):
        """
        validates the proof: does hash(last_proof, proof) contain 4 leading zeroers?
        :param last_proof: <int> previous proof
        :param proof: <int> current proof
        :return: <bool> True if correct , False if not
        """
        guess = u'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash(block):
        """
        create a sha-256 hash of a block
        :param block: <dict> block
        :return: <str>
        """

        #we must make sure that the dictionary is ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        

    @property
    def last_block(self):
        # Returns the last block in the chain
        return self.chain[-1]



