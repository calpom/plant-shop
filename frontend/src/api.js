// A config file for axios

import axios from 'axios';

const api = axios.create({
    baseURL: "http://18.208.248.13:8000/api",
});

export default api;