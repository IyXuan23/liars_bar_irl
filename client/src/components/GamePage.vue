<script setup>

import { getSocket, disconnectSocket } from '@/socket'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { Card } from './Card.vue'

const socket = ref(null)
const route = useRoute()
const username = ref(route.query.username);

const readyState = ref(false)
const readyMsg = ref('Ready')

const gameStart = ref(false)

const currentCards = ref([])
const selectedCards = ref([])

const players = ref(["P1", "P2", "P3", "P4"])

//mount the event listener for leaving the page
onMounted(() => {

    socket.value = getSocket()
    window.addEventListener('beforeUnload', handleBeforeUnload);
});

//if the player closes the page etc, send a disconnect request to the backend, and remove the player
const handleBeforeUnload = () => {

    const data = { 'username': username.value }
    if (socket.value) {
        // socket.emit('remove_player', data)
    }

}

//for console testing
const logs = [
    {'id': 1, 'message': 'player has joined'},
    {'id': 2, 'message': 'player has left'}
]

//function to toggle the ready button, and sends message to backend to tell game player is ready
function toggleReady() {

    const data = {'username': username.value }
    
    if (!readyState.value) {
        readyState.value = true
        readyMsg.value = 'Waiting for other players...'
        // socket.emit('player_ready', data)
    }
    else {
        readyState.value = false
        readyMsg.value = 'Ready'
        // socket.emit('player_unready', data)
    }
}

//function for when player makes a move
function playerMove(type) {

    if (type == 'call') {
        const data = {
            'username': username.value,
            'move_type': 'call'
        }
        // socket.emit('player_move', data)
    } 
    else if (type == 'play') {
        const data = {
            'username': username.value,
            'move_type': 'play',
            'played_hand': selectedCards.value
        }
        // socket.emit('player_move', data)
    }
}

</script>

<template>
    <div class="masterBox">
        <div class="playBox">
            <div class="upperPlayBox">
                <div class="corner">{{ players[0] }}</div>
                <div class="handBoxHorizontal"></div>
                <div class="corner">{{ players[1] }}</div>
            </div>
            <div class="middlePlayBox">
                <div class="handBoxVertical"></div>
                <div class="playBoxCentre"></div>
                <div class="handBoxVertical"></div>
            </div>
            <div class="lowerPlayBox">
                <div class="corner">{{ players[2] }}</div>
                <div class="handBoxPlayer">
                    <Card
                        v-for="(card, index) in currentCards"
                        :key = 'index'
                        :card = 'card.id'
                        :cardImage = 'card.image'
                    />
                </div>
                <div class="corner">{{ players[3] }}</div>
            </div>
        </div>
        <div class="controlsBox">
            <div class="logBox">
                <div v-for="log in logs" :key="log.id">
                    {{ log.message   }}
                </div>
            </div>
            <div class="buttonBox">
                <button v-if='!gameStart' class="readyButton" @click="toggleReady">{{ readyMsg }}</button>
                <button v-if='gameStart' class="playButton" @click="playerMove('play')">Play Cards</button>
                <button v-if='gameStart' class="callButton" @click="playerMove('call')">Call</button>
                <button v-if='gameStart' class="quitButton">Quit Game</button>
            </div>
        </div>
    </div>
</template>

<style>

body {
    margin: 0px !important;
}

.masterBox {
    display: flex;
    width: 90vw;
    height: 50vw;
}

.playBox {
    border: darkgreen 2px solid;
    height: 100%;
    width: 80%;
    border-radius: 6px;
}

.upperPlayBox {
    display: flex;
    height: 20%;
}

.middlePlayBox{
    display: flex;
    height: 60%;
}

.lowerPlayBox {
    display: flex;
    height: 20%;
}

.corner {
    height: 100%;
    width: 20%;
    border: solid red 1px;
}

.handBoxHorizontal {
    height: 100%;
    width: 60%;
    border: solid red 1px;
}

.handBoxVertical {
    height: 100%;
    width: 20%;
    border: solid red 1px;
}

.handBoxPlayer {
    height: 100%;
    width: 60%;
    border: solid red 1px;
}

.playBoxCentre {
    height: 100%;
    width: 60%;
    border: solid red 1px;
}

.controlsBox {
    height: 100%;
    width: 20%;
}

.logBox {
    height: 50%;
    width: 100%;
    padding: 4px;
    border-radius: 6px;
    background-color: darkolivegreen;
}

.buttonBox {
    height: 50%;
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 4px;
    gap: 4px;
}

button {
    flex: 1;
    border-radius: 6px;
    border: none;
    font-size: 24px;
}

.playButton {
    background-color: green;
}

.callButton {
    background-color: darkgoldenrod;
}

.quitButton {
    background-color: red;
}

.readyButton {
    background-color: yellowgreen;
}

button:hover {
    background-color: darkcyan;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    cursor: pointer;
}

</style>