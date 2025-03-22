<script setup>

import { getSocket, disconnectSocket } from '@/socket'
import { ref } from 'vue'

const socket = getSocket()

const testSend = () => {
    const data = {
        'msg': 'hello there'
    }
    socket.emit('test', data)
}

//for console testing
const logs = [
    {'id': 1, 'message': 'player has joined'},
    {'id': 2, 'message': 'player has left'}
]

const readyState = ref(false)
const readyMsg = ref('Ready')

const gameStart = ref(false)

function toggleReady() {
    
    if (!readyState.value) {
        readyState.value = true
        readyMsg.value = 'Waiting for other players...'
        // socket.emit('player_ready', {'message': 'ready'})
    }
    
    else {
        readyState.value = false
        readyMsg.value = 'Ready'
        // socket.emit('player_unready', {'message': 'unready'})
    }
}

</script>

<template>
    <div class="masterBox">
        <div class="playBox"></div>
        <div class="controlsBox">
            <div class="logBox">
                <div v-for="log in logs" :key="log.id">
                    {{ log.message   }}
                </div>
            </div>
            <div class="buttonBox">
                <button v-if='!gameStart' class="readyButton" @click="toggleReady">{{ readyMsg }}</button>
                <button v-if='gameStart' class="playButton">Play Cards</button>
                <button v-if='gameStart' class="callButton">Call</button>
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