from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from game import LiarsBar, Player


# instantiate the app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins=
                    ["http://localhost:5173", 
                     "https://liars-bar-irl-frontend-4bezc477a-iyxuans-projects.vercel.app"])

#initialise the game
game = LiarsBar()

#home page for joining the game, and also info and instructions
@app.route('/')
def home():
    return render_template('home.html')

@socketio.on('test')
def handle_message(data):

    msg = data.get('msg')

    print(f"received message: {msg}")
    emit('response', {'message': 'hello world!'})


#code for adding a player to the lobby
@socketio.on('add_player')
def handle_add_player(data):
    player_name = data.get('name')
    sid = request.sid
    print(sid)
    player = Player(player_name, sid)

    if game.add_player(player):
        emit('player_added', {'message': f"player {player_name} added to game"})
    else:
        emit('error', {'message': 'lobby is full'})

    emit('game_state', {'message': f'game is {game.state}'}, broadcast=True)


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
        emit('error', {'message: not enough players'})
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

if __name__ == '__main__':
    socketio.run(app, debug=True)