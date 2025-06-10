import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const messagesEndRef = useRef(null);

  const suggestedQuestions = [
    "What is your name?",
    "Tell me a joke",
    "What can you do?",
    "How does React work?",
    "Explain Django REST API",
    "How to improve coding skills?"
  ];

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const res = await axios.get('http://localhost:8000/api/history/');
        const formatted = res.data.map(item => ({
          user: item.user_message,
          bot: item.bot_response,
        }));
        setChatLog(formatted.reverse());
      } catch (error) {
        console.error("Failed to fetch chat history:", error);
      }
    };
    fetchHistory();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatLog]);

  const handleSend = async () => {
    if (!message.trim()) return;

    try {
      const res = await axios.post('http://localhost:8000/api/chat/', {
        user_message: message,
      });

      setChatLog([...chatLog, {
        user: message,
        bot: res.data.bot_response,
      }]);

      setMessage('');
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  const handleSuggestionClick = (question) => {
    setMessage(question);
    setTimeout(() => handleSend(), 100); // auto-send
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="bg-white shadow-xl rounded-lg w-full max-w-xl p-6 space-y-4">
        <h1 className="text-2xl font-bold text-center text-blue-600">💬 Chatbot Assistant</h1>

        {/* Suggested Questions */}
        <div className="flex flex-wrap gap-2">
          {suggestedQuestions.map((q, i) => (
            <button
              key={i}
              onClick={() => handleSuggestionClick(q)}
              className="bg-gray-200 hover:bg-gray-300 text-sm px-3 py-1 rounded-full"
            >
              {q}
            </button>
          ))}
        </div>

        {/* Chat Log */}
        <div className="h-96 overflow-y-auto border border-gray-300 rounded p-4 space-y-4 bg-gray-50">
          {chatLog.map((chat, idx) => (
            <div key={idx} className="space-y-1">
              <p className="text-sm"><strong>You:</strong> {chat.user}</p>
              <p className="text-sm"><strong>Bot:</strong> {chat.bot}</p>
              <hr className="border-gray-200" />
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="flex gap-2">
          <input
            type="text"
            value={message}
            onChange={e => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message..."
            className="flex-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            onClick={handleSend}
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
