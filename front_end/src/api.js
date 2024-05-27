// api.js

import axios from 'axios';

const API_URL = 'http://localhost:4000/api';

export const fetchNBAData = async (functionName, params = {}) => {
  try {
    const response = await axios.get(`${API_URL}/data/${functionName}`, { params });
    return response.data;
  } catch (error) {
    console.error('Error fetching NBA data:', error);
    throw error;
  }
};
