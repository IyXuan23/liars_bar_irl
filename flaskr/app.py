from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from game import LiarsBar, Player


# instantiate the app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=
                    ["http://localhost:5173", 
                     "https://liars-bar-irl-frontend.vercel.app"])

#initialise the game
game = LiarsBar()

#home page, just for testing
@app.route('/')
def home():
    return render_template('home.html')

#code for adding a player to the lobby
@socketio.on('add_player')
def handle_add_player(data):
    player_name = data.get('name')
    sid = request.sid
    player = Player(player_name, sid)

    if game.add_player(player):
        emit('player_added', {'message': f"player {player_name} added to game"})
    else:
        emit('error_full_lobby', {'message': 'lobby is full'})


#code to check for player ready or not ready
@socketio.on('player_ready')
def handle_player_ready(data):
    game.ready_number += 1
    if (len(game.players) > 1) and (game.ready_number == len(game.players)):
        handle_start_game()

@socketio.on('player_unready')
def handle_player_unready(data):
    game.ready_number -= 1

#once all players are ready, automatically start the game
def handle_start_game():
    if len(game.players) < 2:
        print('error, not enough players')
    else:
        game.start_game()
        emit('game_started', {'message': 'game start!'})
        emit('game_state', game.get_game_state(), broadcast=True)


#when player makes a move
@socketio.on('player_move')
def handle_move(data):
    if data['username'] != game.active_player:
        print('Error: incorrect player')
        return
    else:
        if data['move_type'] == 'call':
            game.handle_move_call(data)
        if data['move_type'] == 'play':
            game.handle_move_play(data)

@socketio.on('remove_player')
def handle_remove_player(data):
    game.remove_player(data['username'])

if __name__ == '__main__':
    socketio.run(app, debug=True)