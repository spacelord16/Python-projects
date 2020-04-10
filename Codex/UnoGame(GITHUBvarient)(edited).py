from random import randint
class StandardCards:
   def __init__(self,c,n):
      self.color = c
      self.number = n
   def __str__(self):
       return self.color + " " + str(self.number)
   __repr__ = __str__
          
class WildCard:
    def __init__(self):
        self.is_draw_4 = False        
    def __str__(self):
        if self.is_draw_4 == False:
            return "Wild"
        else:
            return "Wild Draw 4"
    __repr__ = __str__
# never used card
class ReversCard:
   def __init__(self,c):
      self.color = c
   def __str__(self):
      return self.color + "Reverse"
   __repr__ = __str__
class SkipCard:
   def __init__(self,c):
      self.color = c
   def __str__(self):
      return self.color + "Skip"
   __repr__ = __str__
class DrawCard:
   def __init__(self,c):
      DrawCard.color = c
   def __str__(self):
      return self.color + " Draw 2 "
   __repr__ = __str__
class Player:
   def __init__(self,name,pid):
      self.name = name
      self.pid = pid
      self.cards = []
   def __str__(self):
      return '%s: %s' % (self.name, ', '.join(str(card) for card in self.cards))
   __repr__ = __str__
def create_deck():
   deck = []
   for i in range(10):
       for color in ['blue','green','red','yellow']:
           if i == 0:
               card  = StandardCards(color,i)
               deck.append(card)
           else:
               card = StandardCards(color,i)
               deck.append(card)
               card = StandardCards(color,i)
               deck.append(card)
   # makes the wild card
   for i in range(4):
       card = WildCard()
       deck.append(card)
   #makes wild card that is a draw 4
   for i in range(4):
       cards = WildCard() # never used
       card.is_draw_4 = True
       deck.append(card)
   return deck
def deal_one_card(p,deck):
   if len(deck)==0:
       return
   i = randint(0,len(deck)-1)
   p.cards.append(deck[i])
   deck.remove(deck[i])
def create_discard_pile(deck):
    discard_pile = []
    i = randint(0,len(deck)-1)
    discard_pile.append(deck[i])
    deck.remove(deck[i])
    return discard_pile
def deal(p1,p2,p3,p4,deck):
    for i in range(7):
        deal_one_card(p1,deck)
        deal_one_card(p2,deck)
        deal_one_card(p3,deck)
        deal_one_card(p4,deck)
if __name__ == '__main__':
    p1 = Player("Jim",1)
    p2 = Player("John",2)
    p3 = Player("sean",3)
    p4 = Player("james",4)
    deck = create_deck()
    deal(p1,p2,p3,p4,deck)
    discard_pile = create_discard_pile(deck)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(discard_pile[-1])
