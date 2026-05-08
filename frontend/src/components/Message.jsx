import React from 'react';
import { User, Bot } from 'lucide-react';

export const Message = ({ message, isUser }) => {
  return (
    <div className={`flex gap-4 mb-6 animate-fadeIn ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="flex-shrink-0">
          <div className="flex items-center justify-center h-8 w-8 rounded-full bg-blue-600 text-white">
            <Bot size={20} />
          </div>
        </div>
      )}
      
      <div
        className={`max-w-xs lg:max-w-md xl:max-w-lg px-4 py-3 rounded-lg ${
          isUser
            ? 'bg-blue-600 text-white rounded-br-none'
            : 'bg-gray-100 text-gray-900 rounded-bl-none'
        }`}
      >
        <p className="break-words">{message}</p>
      </div>

      {isUser && (
        <div className="flex-shrink-0">
          <div className="flex items-center justify-center h-8 w-8 rounded-full bg-gray-300 text-gray-700">
            <User size={20} />
          </div>
        </div>
      )}
    </div>
  );
};
