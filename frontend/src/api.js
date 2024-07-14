// A config file for axios

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the baseURL to match your Django API endpoint
});

export default api;