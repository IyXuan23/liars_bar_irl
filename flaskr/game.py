import random

class LiarsBar:

    def __init__(self):

        self.players = []
        self.deck = self.create_deck()
        self.state = 'waiting'
        self.active_player = None

        self.ready_number = 0

        self.round_end = False

    #creates deck of 6A, 6Q, 6K, 2Joker
    def create_deck(self):

        deck = []
        for i in range(0,6):
            deck.append('Ace')
            deck.append('Queen')
            deck.append('King')

        deck.append('Joker')
        deck.append('Joker')
        return deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        for player in self.players:
            player.cards = self.deck[0:5]
        
        self.deck = self.deck[5:]

    def add_player(self, player):

        if len(self.players) < 3:
            self.players.append(player)
            return True
        
        return False

    def start_game(self):

        while not self.round_end():

            active_player



class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.bullet_chances = 6