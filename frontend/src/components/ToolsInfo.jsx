import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';

export const ToolsInfo = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const tools = [
    {
      category: 'Mathematics',
      items: ['Add', 'Subtract', 'Multiply', 'Divide', 'Exponent', 'Differentiate', 'Integrate', 'Scientific Calculator']
    },
    {
      category: 'Information',
      items: ['Weather', 'Web Search']
    },
    {
      category: 'Execution',
      items: ['Python Execution', 'CSV Analysis', 'Final Answer']
    },
    {
      category: 'Communication',
      items: ['Gmail Integration', 'Send Email']
    }
  ];

  return (
    <div className="bg-blue-50 border-l-4 border-blue-600 p-4 mb-4 rounded">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="flex items-center justify-between w-full text-left"
      >
        <h3 className="font-semibold text-gray-900">Available Tools</h3>
        {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
      </button>
      
      {isExpanded && (
        <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
          {tools.map((tool, idx) => (
            <div key={idx}>
              <h4 className="font-semibold text-sm text-blue-900 mb-2">{tool.category}</h4>
              <ul className="text-sm text-gray-700 space-y-1">
                {tool.items.map((item, itemIdx) => (
                  <li key={itemIdx} className="flex items-center gap-2">
                    <span className="w-1.5 h-1.5 bg-blue-600 rounded-full"></span>
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
