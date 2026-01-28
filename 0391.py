class Block:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        
    def function(self):
        w_up = self.word1.upper()
        w_low = self.word2.lower()
        print(w_up)
        print(w_low)
        
        
list = ["jaVA", "jAvaScRiPt"]

result = Block(list[0], list[1])
result.function()
