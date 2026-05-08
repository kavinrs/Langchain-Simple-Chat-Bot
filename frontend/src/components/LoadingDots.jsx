import React from 'react';

export const LoadingDots = () => {
  return (
    <div className="flex items-center gap-2 p-4">
      <div className="flex gap-1">
        <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0s' }}></div>
        <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
        <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
      </div>
      <span className="text-gray-600 text-sm">Processing your request...</span>
    </div>
  );
};
