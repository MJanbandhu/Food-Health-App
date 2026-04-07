import axios from 'axios';

// Use Vite env var if provided, otherwise default to relative path for Nginx or absolute for dev
const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Examples of API calls
export const getDashboardData = () => apiClient.get('/food/dashboard');
export const trackFood = (data) => apiClient.post('/food/track', data);
export const scanFood = (data) => apiClient.post('/scanner/scanner', data);
export const getRecommendations = () => apiClient.get('/recommendations/recommendations');

export default apiClient;
