class StandardCards:
   def __init__(self,c,n):
      self.color = c
      self.number = n
   def as_string(self):
       return self.color + " " + str(self.number)
          
class WildCard:
    def __init__(self):
        self.is_draw_4 = False
    def as_string(self):
        if self.is_draw_4 == False:
            return "Wild"
        else:
            return "Wild Draw 4"
class ReversCard:
   def __init__(self,c):
      self.color = c
   def as_string(self):
      return self.color + "Reverse"
class SkipCard:
   def __init__(self,c):
      self.color = c
   def as_string(self):
      return self.color + "Skip"
class DrawCard:
   def __init__(self,c):
      DrawCard.color = c
   def as_string(self):
      return self.color + " Draw 2 "
class player:
   def as_string(self,name,pid):
      self.name = name
      self.pid = pid
      self.cards = []
   def as_string(self):
      results  = self.name
      for card in self.cards:
         results = results+ " " +self.card[0].as_string()
      return results
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
       cards = WildCard()
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
p1 = Player("Jim",1)
p2 = Player("John",2)
p3 = Player("sean",3)
p4 = Player("james",4)
deck = create_deck()
deal(p1,p2,p3,p4,deck)
discard_pile = create_discard_pile(deck)
print(p1.as_atring())
print(p2.as_String())
print(p3.as_string())
print(p4.as_atring())
print(discard_pile(-1).as_string())
