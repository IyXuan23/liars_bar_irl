import { io } from "socket.io-client"

let socket = null

//temporary URL, to be replaced
export const getSocket = () => {
    if (!socket) {
        socket = io('https://liars-bar-irl-backend.onrender.com/');
    }
    return socket;
};

export const disconnectSocket = () => {
    if (socket) {
        socket.disconnect();
        socket = null;
    }
};