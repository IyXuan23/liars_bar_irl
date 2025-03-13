import { io } from "socket.io-client"

let socket = null

//temporary URL, to be replaced
export const getSocket = () => {
    // if (!socket) {
    //     socket = io('SOME_URL');
    // }
    return socket;
};

export const disconnectSocket = () => {
    if (socket) {
        socket.disconnect();
        socket = null;
    }
};