import axios from 'axios';

// Use strict relative path because backend and frontend are now served from the exact same port/domain.
const API_BASE = '/api/v1';

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
