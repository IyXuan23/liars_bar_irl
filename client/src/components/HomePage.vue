<script setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { getSocket, disconnectSocket } from '@/socket';

const currRouter = useRouter()
const username = ref("")
const isError = ref(false)
const errorMsg = ref("Username cannot be empty")

//check for empty name, and proceed to game page if the playerName is valid
function joinGame() {

    if (username.value.trim() === '') {
        isError.value = true
    }

    else {
        isError.value = false

        // get the global socket from socket.js
        const socket = getSocket()

        //send the join request
        const data = {'name': username}
        // socket.emit('add_player', data)
        
        //prevent stack error
        if (currRouter.currentRoute.value.path !== '/game') {
            currRouter.push({ path: '/game', query: {username: username} });
        }
    }
}

</script>

<template>
    <div class="columnbox">
        <div class="columntitle">
            <div class="title">
                Liar's Bar
                <div class="subtitle">
                    An Online Recreation
                </div>
            </div>
        </div>
        <div class="columnbuttons">
            <p v-if="isError" class="errorMsg">{{ errorMsg }}</p>
            <input class='username' :class="{'inputerror': isError}" v-model="username" placeholder="Enter username"></input>
            <button class="button" @click="joinGame">Join Game</button>
            <button class="button" @click="currRouter.push({path:'/about'})">About</button>
        </div>
    </div>
</template>

<style scoped>

.columnbox{
    display: flex;
    flex-direction: row;
    gap: 32px;
    width: 80vw;
}

.columntitle{
    flex: 0 0 75%;
}

.title{
    display: flex;
    flex-direction: column;
    font-size: 100px;
}

.subtitle{
    font-size: 40px;
}

.columnbuttons{
    display: flex;
    flex: 0 0 20%;
    flex-direction: column;
    padding: 4px;
    gap: 8px;

    justify-content: center;
}

.username{
    background-color: lightgray;
    font-size: 20px;
    padding: 8px;
    border: none;
    border-radius: 6px;
}

.button{
    background-color: lightgreen;
    font-size: 20px;
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 4px;
    padding-right: 4px;
    border: none;
    border-radius: 6px;
}

.button:hover{
    background-color: lightblue;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    cursor: pointer;
}

.inputerror{
    border: 2px red solid;
    background-color: #f8d7da;
}

.errorMsg {
    color: red;
    font-size: 14px;
    margin-top: 5px;
}

</style>