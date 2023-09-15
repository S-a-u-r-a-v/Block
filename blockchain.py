import hashlib #it will provide sha256 function

def hashGenerator(data): #this function will generate hash for the given data
    result=hashlib.sha256(data.encode()) #encoding of data with the help of sha256 algo 
    return result.hexdigest() #it will return the encoded data in the form of haxadecimal with the help og hexidigit

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash
        

class Blockchain:
    def __init__(self):
      hashLast=hashGenerator('last_hash') #this data will go to hashgenerator function and it will be converted into hexadecimal
      hashStart=hashGenerator('own_hash')

      genesis=Block('gen-data',hashStart,hashLast)
      self.chain=[genesis] #genesis block will be added into the chain

    def add_block(self,data):
        prev_hash=self.chain[-1].hash #hash of genesis block 
        hash=hashGenerator(data+prev_hash) # data and pre hash of last block 
        block=Block(data,hash,prev_hash) #new block
        self.chain.append(block) # new block added into the chain

bc=Blockchain()
bc.add_block('saurav1')
bc.add_block('saurav2')
bc.add_block('saurav3')
bc.add_block('saurav4')

for block in bc.chain:
    print(block.__dict__) #printing of blocks in the form of dictionary 
