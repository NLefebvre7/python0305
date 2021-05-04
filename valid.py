
#valider le premier block :
    def isFirstBlockValid(self):
        firstBlock = self.blocks[0]

        if firstBlock.index != 0:
            return False
        
        if firstBlock.previousHash is not None:
            return False

        if (firstBlock.hash is None or calculateHash(firstBlock) != firstBlock.hash):
            return False

        return True

#valider 1 block
    def isValidBlock(self, block, previousBlock):
        if previousBlock.index+1 != block.index:
            return False

        if (block.previousHash is None or block.previousHash != previousBlock.hash):
            return False
        
        if (block.hash is None or calculateHash(block) != block.hash):
            return False
        
        return True


#valider la blockchain ;:
    def isBlockchainValid(self):
        if not self.isFirstBlockValid():
            return False
        
        for i in range(1, len(self.blocks)):
            previousBlock = self.blocks[i-1]
            block = self.blocks[i]
            if not self.isValidBlock(block, previousBlock):
                return False 

        return True
