<script setup>

import { io } from 'socket.io-client'

const socket = io('http://localhost:5000')

const testSend = () => {
    const data = {
        'msg': 'hello there'
    }
    socket.emit('test', data)
}

</script>

<template>
    <div>
        <button @click="testSend">Test Button</button>
    </div>
</template>