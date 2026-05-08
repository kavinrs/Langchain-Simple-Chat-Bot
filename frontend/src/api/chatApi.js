import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chatApi = {
  sendMessage: async (question) => {
    try {
      const response = await api.post('/chat', { question });
      return response.data;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  },

  sendEmail: async (question) => {
    try {
      const response = await api.post('/email', { question });
      return response.data;
    } catch (error) {
      console.error('Error sending email:', error);
      throw error;
    }
  },

  // Optional: Add endpoint to clear history
  clearHistory: async () => {
    try {
      const response = await api.post('/clear-history');
      return response.data;
    } catch (error) {
      console.error('Error clearing history:', error);
      throw error;
    }
  },
};

export default api;
