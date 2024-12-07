import React, { useEffect, useState } from 'react';

const wsChannel = new WebSocket('');

export type ChatMessageType = {
    message: string;
    photo: string;
    userId: number;
    userName: string;
};


const Chat: React.FC = () => {
    return (
        <div>
            <Messages />
            <AddMessageForm />
        </div>
    );
};

const Messages: React.FC = () => {
    const [messages, setMessages] = useState<ChatMessageType[]>([]);

    useEffect(() => {
        wsChannel.addEventListener('message', (e: MessageEvent) => {
            let newMessages = JSON.parse(e.data);
            setMessages((prevMessages) => [...prevMessages, ...newMessages]);
        });
    }, []);

    return (
        <div>
            {messages.map((message, index) => (
                <Message key={index} message={message} />
            ))}
        </div>
    );
};

const Message: React.FC<{ message: ChatMessageType }> = ({ message }) => {
    return (
        <div>
            <img src={message.photo} style={{ width: '30px' }} alt={message.userName} />
            <b>{message.userName}</b>
            <br />
            {message.message}
            <hr />
        </div>
    );
};

const AddMessageForm: React.FC = () => {
    const [message, setMessage] = useState('');

    const sendMessage = () => {
        if (message) {
            wsChannel.send(message);
            setMessage('');
        }
    };

    return (
        <div>
            <textarea
                onChange={(e) => setMessage(e.currentTarget.value)}
                value={message}
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chat;
