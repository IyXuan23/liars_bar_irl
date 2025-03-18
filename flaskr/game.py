import random
from app import socketio


class LiarsBar:

    def __init__(self):

        #players contain list of active players, dead_players for players which are eliminated
        #and active_player means player whose turn it currently is
        self.players = []
        self.dead_players = []
        self.active_player = None    

        #active cards are the current played cards, used if called out by next player
        self.active_cards = []

        #current active card type, between Q, K, A
        self.current_table_type = None

        #cards in the deck, and gamestate
        self.deck = self.create_deck()
        self.state = 'waiting'

        #number to keep track of player readiness
        self.ready_number = 0

        #boolean for keeping track of ending round
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

    #randomly choose the table type, K, Q, A
    def generate_table_type(self):
        lst = ['Ace', 'King', 'Queen']
        chosen = random.choice(lst)
        return chosen

    #game currently only supports up to 4 players
    def add_player(self, player):

        if len(self.players) < 3:
            self.players.append(player)
            return True
        return False

    #check if there is only 1 remaining live player
    def check_end_game(self):

        if len(self.dead_players) + 1 == len(self.players):
            return True
        return False
    
    #get the next player
    def get_next_player(self):

        prev_active_player = self.active_player
        
        #get index of active player, then increment it by 1 (or reset to 0)
        new_player_index = self.players.index(self.active_player)
        new_player_index += 1
        if new_player_index == len(self.players):
            new_player_index = 0
        
        #iterate until we reach the next non-dead player
        while self.active_player == prev_active_player:
            if self.players[new_player_index] not in self.dead_players:
                return self.players[new_player_index]
            else:
                new_player_index+= 1
    
    def handle_move_call(self, data):
        return

    #update played hand, then move to the next turn player
    def handle_move_play(self, data):

        played_hand = data['selected_cards']
        self.active_cards = played_hand

        self.active_player = self.get_next_player()

        return

    def start_game(self):

        assert(self.players <= 4)

        self.deck = self.create_deck()
        self.shuffle_deck()

        self.deal_cards()
        
        active_player_index = 0
        self.active_player = self.players[active_player_index]

        while not self.check_end_game():
            #proceed with the game

            self.new_turn_emit()
            self.wait_player_move()
            
            break
        





class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.bullet_chances = 6