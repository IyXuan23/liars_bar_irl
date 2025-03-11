from flask import Flask, render_template
from flask.socketio import SocketIO, emit
from game import LiarsBar, Player


# instantiate the app
app = Flask(__name__)
socketio = SocketIO(app)

#initialise the game
game = LiarsBar()

#home page for joining the game, and also info and instructions
@app.route('/')
def home():
    return render_template('home.html')

@socketio.on('message')
def handle_message(data):
    print(f"received message: {data}")
    emit('response', {'message': 'hello world!'})


#code for adding a player to the lobby
@socketio.on('add_player')
def handle_add_player(player):
    player_name = data.get('name')
    player = Player(player_name)

    if game.add_player(player):
        emit('player_added', {'message': f"player {player_name} added to game"})
    else:
        emit('error', {'message': 'lobby is full'})

    emit('game_state', game.get_game_state(), broadcast=True)

@socketio.on('player_ready')
def handle_player_ready(data):
    game.readyNumber += 1
    if game.readyNumber == len(game.players):
        handle_start_game()

@socketio.on('player_unready')
def handle_player_unready(data):
    game.readyNumber -= 1

def handle_start_game():
    if len(game.players < 2):
        emit('error', {'message: not enough players'})
    else:
        game.start_game()
        emit('game_started', {'message': 'game start!'})
        emit('game_state', game.get_game_state(), broadcast=True)

if name == '__main__':
    socketio.run(app, debug=True)