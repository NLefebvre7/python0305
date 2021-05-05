from hashlib import sha256
from datetime import datetime

def calculateHash(block):
    bloc = str(block.index) + str(block.previousHash) + str(block.timestamp) + str(block.data) + str(block.nonce)
    return(sha256(bloc.encode('utf-8')).hexdigest())

#recoder
def repeat(string, length):
    return (string * length)[:length]
    # repeated = (string * (int(length/len(string))+1))[:length]
    # return(string * (int(length/len(string))+1))[:length]

# dt = datetime.now()
# #strftime = date time to string + int()
# datetime = int(dt.strftime("%Y%m%d%H%M%S"))

class Block(object):
    def __init__(self, index, previousHash, difficulty, data):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = datetime.now()
        self.data = data
        self.nonce = 0
        self.hash = self.mineBlock(difficulty)
# self.hash = mineblock, le rajouter ds la fonction mineblock

    def mineBlock(self, difficulty):
        self.hash = calculateHash(self)
        # zeros = repeat("0", difficulty)
        self.nonce = 0
        while self.hash[0:difficulty] != "0000":
            self.nonce += 1
            self.hash = calculateHash(self)

class Blockchain(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
    
        genesisBlock = Block(0, None, difficulty, "Genesis block")
        self.blocks.append(genesisBlock)
    
    def newBlock(self, data):
        latestBlock = self.blocks[-1]
        block = (Block(latestBlock.index + 1, latestBlock.hash, datetime.now(), data))
        self.blocks.append(block)



    def isFirstBlockValid(self):
        firstBlock = self.blocks[0]

        if firstBlock.index != 0 and firstBlock.previousHash is not None and (firstBlock.hash is None or calculateHash(firstBlock) != firstBlock.hash) :
            return False

        return True

#concatener les 2 autres
    # def isValidBlock(self, block, previousBlock):
    #     if previousBlock.index+1 != block.index:
    #         return False

    #     if (block.previousHash is None or block.previousHash != previousBlock.hash):
    #         return False
        
    #     if (block.hash is None or calculateHash(block) != block.hash):
    #         return False
        
    #     return True
    
    def isBlockchainValid(self, block, previousBlock):
        if not self.isFirstBlockValid():
            return False
        
        for i in range(1, len(self.blocks)):
            previousBlock = self.blocks[i-1]
            block = self.blocks[i]
            if previousBlock.index+1 != block.index and (block.previousHash is None or block.previousHash != previousBlock.hash) and (block.hash is None or calculateHash(block) != block.hash) :
                return False 

        return True
    
#recoder 
    def display(self):
        for block in self.blocks:
            chain = "Ceci est le block a l'index:"+str(block.index)+"crée le : "+str(block.timestamp)+"\n le hash du block précédent celui ci est :"+str(block.previousHash)+" et il contient comme données: "+str(block.data)+"\n son hash est: "+str(block.hash)+"et le nombre de tentative est de : (nonce) "+str(block.nonce)+"\n"
            print(str(chain))

if __name__ == '__main__':
    bchain = Blockchain(4)

    blockn1 = bchain.newBlock("Second Block")


    blockn2 = bchain.newBlock("Troisieme Block")


    blockn3 = bchain.newBlock("Quatrieme Block")



    print("Validité de la blockchain :", bchain.isBlockchainValid())

    bchain.display()