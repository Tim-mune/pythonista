import random
class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __repr__(self):
        return f'{self.value} of {self.suit}'
     

# Hearts", "Diamonds", "Clubs", or "Spades     
# "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
class Deck:
    def __init__(self):
        suits=["Hearts", "Diamonds", "Clubs",  "Spades"]
        values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards=[Card(value,suit) for suit in suits for value in values]
        print(self.cards)
    
    def __repr__(self):
       return f'Deck of {self.count()} cards'
        
    def count(self):
        return len(self.cards) 
    
    def deal(self,num):
        count=self.count()
        if(count==0):
            raise ValueError('no remaining cards') 
        actual=min([count,num])
        cards=self.cards[-actual:]
        self.cards=self.cards[:-actual]
        
    def deal_card(self):
            return self.deal(1)[0]
    def deal_hand(self,num):
        return self.deal(num)[0]  
    def shuffle(self):
        if(self.count<52):
            raise ValueError('deck should be full to shuffle')
        random.shuffle(self.cards)  
        return self
Deck()   
d=Deck()  
print(d.deal(2))   
print(d)        