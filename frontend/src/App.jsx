import React, { useState, useEffect, useRef } from 'react';
import { ChatHeader } from './components/ChatHeader';
import { Message } from './components/Message';
import { ChatInput } from './components/ChatInput';
import { ToolsInfo } from './components/ToolsInfo';
import { LoadingDots } from './components/LoadingDots';
import { chatApi } from './api/chatApi';

function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  const handleSendMessage = async (question) => {
    // Add user message
    setMessages(prev => [...prev, { type: 'user', content: question }]);
    setIsLoading(true);
    setError(null);

    try {
      const response = await chatApi.sendMessage(question);
      
      // Add bot response
      setMessages(prev => [...prev, { type: 'bot', content: response.answer }]);
      
    } catch (err) {
      setError('Failed to get response. Make sure the backend is running on http://localhost:8000');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearHistory = () => {
    if (window.confirm('Are you sure you want to clear the chat history?')) {
      setMessages([]);
      setError(null);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      <ChatHeader onClearHistory={handleClearHistory} />
      
      {/* Main Chat Area */}
      <div className="flex-1 overflow-y-auto">
        <div className="max-w-4xl mx-auto w-full p-4">
          {messages.length === 0 ? (
            <div className="flex flex-col items-center justify-center h-full py-12">
              <div className="text-center mb-8">
                <h2 className="text-3xl font-bold text-gray-900 mb-2">Welcome to AI ChatBot!</h2>
                <p className="text-gray-600">Ask me anything - I can help with math, weather, web search, code execution, and more!</p>
              </div>
              <ToolsInfo />
            </div>
          ) : (
            <div>
              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-4">
                  {error}
                </div>
              )}
              {messages.map((msg, idx) => (
                <Message
                  key={idx}
                  message={msg.content}
                  isUser={msg.type === 'user'}
                />
              ))}
              {isLoading && <LoadingDots />}
              <div ref={messagesEndRef} />
            </div>
          )}
        </div>
      </div>

      {/* Chat Input */}
      <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
    </div>
  );
}

export default App;
