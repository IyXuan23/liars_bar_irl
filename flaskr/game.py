import random

class LiarsBar:

    def __init__(self):

        #players contain list of active players, dead_players for players which are eliminated
        #and active_player means player whose turn it currently is
        self.players = []
        self.dead_players = []
        self.active_player = None    
        self.previous_player = None

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

    #function to remove a player from the game (for disconnect or game end)
    def remove_player(self, username):

        for player in self.players:
            if player.name == username:
                
                if player in self.dead_players:
                    self.dead_players.remove(player)
                self.players.remove(player)

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

    #function to check whether played hand is valid
    #if valid, return true, else return false
    def check_valid_hand(self):

        for card in self.active_cards:
            if card == 'Joker' or card == self.current_table_type:
                continue
            else:
                return False

        return True

    #if hand is valid, shoot current player
    #if invalid, shoot previous player
    #then reset the round
    def handle_move_call(self):
        
        if self.check_valid_hand():
            dead = self.active_player.shoot_self()
            if dead:
                self.dead_players.append(self.active_player)
        else:
            dead = self.previous_player.shoot_self()
            if dead:
                self.dead_players.append(self.previous_player)

        #reset round
        return

    #update played hand, then move to the next turn player
    def handle_move_play(self, data):

        played_hand = data['selected_cards']
        self.active_cards = played_hand
        
        self.previous_player = self.active_player
        self.active_player = self.get_next_player()
        
        #emit()

    #while there is still more than 1 player alive, continue out the rounds, until
    #the game is over
    def start_game(self):

        assert(self.players <= 4)

        while not self.check_end_game():

            self.start_round()

            #temporary break
            break
        #game has ended
        #emit(victory msg)

    def start_round(self):

        self.deck = self.create_deck()
        self.shuffle_deck()

        self.deal_cards()
        #if its the first round, player 1 starts, else continue in player (alive) order
        if self.active_player == None:
            self.active_player = self.players[0]
        else:
            self.active_player = self.get_next_player()

    def get_emit_data(self):

        data = {
            "players": self.get_players_name(),
            "dead_players": self.get_dead_players_name(),
            "players_handsize": self.get_players_hand_size(),
            "active_card_num": len(self.active_cards),
            "current_table_type": self.current_table_type
        }

    #helper function to get the names of players for emit
    def get_players_name(self):

        player_name_list = [x.name for x in self.players]
        return player_name_list
    #helper function to get names of dead players for emit
    def get_dead_players_name(self):

        dead_players_name_list = [x.name for x in self.dead_players]
        return dead_players_name_list
    #get handsize of all players (for front end rendering)
    def get_players_hand_size(self):

        handsize_list = [len(player.cards) for player in self.players]
        return handsize_list
            





class Player:

    def __init__(self, name, socket_id):
        self.name = name
        self.cards = []
        self.bullet_chances = 6
        self.socket_id = socket_id

    #player shoots self, if dies, return true
    #if not, decrease bullet_chance by 1, and return false
    def shoot_self(self):
        
        lst = range(0, self.bullet_chances)
        chosen = random.choice(lst)

        if chosen == 0:
            return True
        else:
            self.bullet_chances -= 1
            return False