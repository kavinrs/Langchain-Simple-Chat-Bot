import React from 'react';
import { MessageCircle, RefreshCw, Trash2 } from 'lucide-react';

export const ChatHeader = ({ onClearHistory }) => {
  return (
    <div className="bg-gradient-to-r from-blue-600 to-blue-800 text-white p-4 shadow-lg">
      <div className="flex items-center justify-between max-w-4xl mx-auto">
        <div className="flex items-center gap-3">
          <MessageCircle size={28} />
          <div>
            <h1 className="text-2xl font-bold">AI ChatBot Agent</h1>
            <p className="text-blue-100 text-sm">Math • Weather • Web Search • Code • Email</p>
          </div>
        </div>
        <button
          onClick={onClearHistory}
          className="flex items-center gap-2 px-3 py-2 bg-blue-500 hover:bg-blue-400 rounded-lg transition-colors text-sm"
          title="Clear chat history"
        >
          <Trash2 size={18} />
          <span className="hidden sm:inline">Clear</span>
        </button>
      </div>
    </div>
  );
};
