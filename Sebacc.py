import numpy as np

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #self.index = None

class Table:
    def __init__(self):
        self.discardPile = []
        self.deck = []
        suits = ['Flasks','Sabers','Staves','Coins']
        ranks = np.arange(1,11)
        negranks = np.arange(-10, 0)
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
            for rank in negranks:
                self.deck.append(Card(suit, rank))

    def deal_card(self):
        card = self.deck.pop()
        return card

    def shuffle(self):
        np.random.shuffle(self.deck)

class Hand:
    def __init__(self):
        self.cards = []
        self.chips = []
        self.value = int(0)

    def add_card(self, card):
        self.cards.append(card)
        #card.index = len(self.cards)

    def reIndex(self):
        for card in self.cards:
            card.index = self.cards.index('')

    def displayCards(self):
        print("--- Cards in Hand ---")
        for i in range(len(self.cards)):
            print(f'{i+1}.', self.cards[i].suit, self.cards[i].rank)
        print('\n')

    def gain(self, deck: object):
        self.add_card(deck.deal_card())
        areDiscarding = input('Do you want to to discard a card?: ').lower() in ('yes','y')
        if areDiscarding:
            self.discard(deck)
            print(f'Card gained: {self.cards[-1].suit} {self.cards[-1].rank} ')
        return
    
    def discard(self, deck: object):
        discardIndex = int(input('Which card would you like to discard? (1,2,etc.): ')) 
        deck.discardPile.append(self.cards.pop(discardIndex - 1))

    def swap(self, deck: object):
        #swapIndex = int(input('Which card would you like to swap with? (1,2,etc.): '))
        self.discard(deck)
        self.add_card(deck.discardPile.pop(-2))


def startGame():
    deck = Table()
    deck.shuffle()
    hand = Hand()
    deck.discardPile.append(deck.deal_card())
    '''
    /// Print statement for checking cards in deck
    for i in range(80):
        print(deck.deck[i].suit)
        print(deck.deck[i].rank)
    '''
    hand.add_card(deck.deal_card())
    hand.add_card(deck.deal_card())
    return deck, hand


playing = True
while playing:
    rounds = np.arange(1,5)
    phases = ['Turn', 'Bet', 'Spike']
    for round in rounds:
        print(f'\n -------- Round {round} -------- \n')
        if round == rounds[0]: # Start of a game
            deck, hand = startGame()
            hand.displayCards()
        if round == rounds[-1]:
            print('--- Showdown ---')
            break
        

        for phase in phases:
            print(f'--- {phase} Phase ---')
            if phase == 'Turn':
                action = input('Gain, Swap, Stand, or Junk?: ')[:2].lower()
                if action == 'ga':
                    hand.gain(deck)

                if action == 'sw': # Swap cards with top card of discard pile
                    print('Swapping')
                    hand.swap(deck)

                if action == 'st':
                    print('Standing')
                    pass
            
                if action == 'ju': # Find a way 
                    print('Junking')
                    break
            hand.displayCards()
            
    playing = input('--- Want to play another round? (y/n) --- ').lower() in ('yes','y')


'''
/// Print statement for checking cards in hand
for i in range(2):
    #print('\n', i)
    #print(hand.hand[i-1].suit)
    #print(hand.hand[i-1].rank)
'''

#if __name__ == "__main__":
#    game()
